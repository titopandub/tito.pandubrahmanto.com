---
layout: post
title: Masalah Suspend pada Ubuntu 20.04 karena NVIDIA Driver 510 dan CUDA
description: Masalah suspend pada Ubuntu 20.04 karena upgrade NVIDIA Driver ke versi 510 (juga karena instalasi CUDA).
date: 2022-02-12 21:30:00.000000000 +07:00
type: post
published: true
status: publish
permalink: /2022-02-12-masalah-suspend-ubuntu-karena-nvidia-driver-cuda/
categories: 
- Computer
tags:
- linux
- ubuntu
- nvidia
comments: true
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---

# Komputer tidak bisa suspend setelah upgrade NVIDIA driver 510 di Ubuntu 20.04

Saya memiliki PC dengan RTX GPU dan menggunakan OS Ubuntu 20.04. Beberapa minggu yang lalu, pada saat weekend, seperti biasanya saya melakukan update (`sudo apt update`) dan upgrade (`sudo apt upgrade`) package. Saat itu muncul pemberitahuan terdapat update untuk NVIDIA driver. Tanpa pikir panjang, langsung saya ketik `y` dan mulailah proses upgrade. Proses upgrade berjalan lancar dan tidak ada masalah. Siang berganti malam, saya suspend PC dan tidur.

Di pagi harinya, ternyata PC saya tidak ter-suspend, masih menyala dan ada di menu login. Saya kaget, kenapa PC saya tidak bisa suspend. Saya coba login dan saya lihat semua aplikasi yang berjalan (Chrome, Slack dan aplikasi lainnya) sudah di-close oleh OS. Seperti saat setelah restart. Saya mencoba melakukan suspend pada PC, ternyata yang terjadi adalah monitor mati sebentar seakan-akan PC melakukan proses suspend akan tetapi setelahnya menyala kembali ke menu login.

# Mencari akar permasalahan

Saya mencoba mencari akar permasalahannya melalui log seperti `less /var/log/syslog` dan `dmesg`, namun saya tidak menemukan sesuatu yang aneh. Selanjutnya saya mencoba mencari di internet apakah ada yang mengalami masalah yang sama. Penyebab dari masalah ini semakin sulit ditemukan karena saya juga mengupgrade kernel.

Saat itu saya tidak bisa menemukan permasalahan yang sama di driver versi 510 ataupun di kernel yang baru saya upgrade. Setelah berjam-jam tidak ditemukan, akhirnya saya coba untuk kembali ke versi sebelumnya, siapa tahu akan normal kembali. Pertama yang saya coba adalah kembali ke versi kernel sebelumnya. Saya melakukannya melalui setting GRUB. Setting default GRUB yang ada pada PC saya tidak menampilkan pilihan Safe Boot ke kernel versi sebelumnya. Saya perlu menggantinya di sini.

### /etc/default/grub

```
```

# Solusi Pertama, Revert

Setelah boot ke versi kernel sebelumnya dan melakukan suspend, hasilnya tetap sama. PC tetap tidak bisa suspend, kembali ke login dan semua aplikasi yang tadinya terbuka, jadi ditutup oleh OS. Karena Ubuntu otomatis menyimpan 3 versi kernel, saya mencoba ketiga-tiganya. Hasilnya tetap sama.

Saya mencoba untuk mengembalikan versi NVIDIA. Saya menggunakan menu Software Update Settings pada Ubuntu untuk mengembalikan NVIDIA driver dari versi 510 ke 495. Hasilnya OS bisa suspend seperti biasa. Saat itulah saya tahu bahwa akar permasalahannya adalah NVIDIA driver terbaru. Tapi pertanyaannya kenapa? Kenapa NVIDIA driver terbaru tiba-tiba memiliki behavior yang berbeda dari sebelumnya? Apakah repository ppa yang saya gunakan memiliki masalah?

> Pada percobaan pertama saya mengalami masalah pada saat `apt update`, karena repository Ubuntu di Indonesia sedang bermasalah. Akhirnya dengan mengkonfigurasi ke repository internasional, downgrade NVIDIA driver baru berjalan.

# Solusi Selanjutnya

Saya menemukan solusi untuk masalah yang mirip dengan yang saya alami di [bmcbm's gist](https://gist.github.com/bmcbm/375f14eaa17f88756b4bdbbebbcfd029), akan tetapi gagal untuk diimplementasi, karena saya tidak memiliki file di `TMPL_PATH` dan tidak bisa menemukan apa isinya.

Setelah mencari lagi mengenai masalah yang serupa, saya menemukannya di pertanyaan [christophe.p.bernard](https://forums.developer.nvidia.com/t/ubuntu-20-04-installing-cuda-changes-nvidia-drivers-and-breaks-suspend/196220) di NVIDIA forum. Dia menyatakan bahwa masalah tersebut terjadi karena dia memasang CUDA di sistemnya, yang saya juga melakukannya. Saya mencoba melakukan solusi yang ditulisnya dan hasilnya PC saya bisa melakukan suspend kembali. Berikut ini gejala dari masalahnya dan script yang perlu di-install (saya copy dari post tersebut).

## Gejala

```bash
/etc/systemd/system$ ls -l nvidia-*
lrwxrwxrwx 1 root root 9 nov.  25 10:55 nvidia-hibernate.service -> /dev/null
lrwxrwxrwx 1 root root 9 nov.  25 10:55 nvidia-resume.service -> /dev/null
lrwxrwxrwx 1 root root 9 nov.  25 10:55 nvidia-suspend.service -> /dev/null
```

```bash
$ systemctl status nvidia-suspend
● nvidia-suspend.service
     Loaded: masked (Reason: Unit nvidia-suspend.service is masked.)
     Active: inactive (dead)
```

## Script yang perlu di-install

### fix-nvidia-suspend.sh

```bash
TMP_PATH=/var/tmp
TMPL_PATH=/home/user/missing-scripts

echo "options nvidia NVreg_PreserveVideoMemoryAllocations=1 NVreg_TemporaryFilePath=${TMP_PATH}" | sudo tee /etc/modprobe.d/nvidia-power-management.conf 

sudo rm -f /etc/systemd/system/nvidia-suspend.service # if /dev/null
sudo rm -f /etc/systemd/system/nvidia-resume.service # if /dev/null
sudo rm -f /etc/systemd/system/nvidia-hibernate.service # if /dev/null

sudo install --mode 644 "${TMPL_PATH}/nvidia-suspend.service" /lib/systemd/system
sudo install --mode 644 "${TMPL_PATH}/nvidia-hibernate.service" /lib/systemd/system
sudo install --mode 644 "${TMPL_PATH}/nvidia-resume.service" /lib/systemd/system

sudo install --mode 755 "${TMPL_PATH}/nvidia" /lib/systemd/system-sleep
sudo install --mode 755 "${TMPL_PATH}/nvidia-sleep.sh" /usr/bin

sudo systemctl enable nvidia-suspend.service
sudo systemctl enable nvidia-hibernate.service
sudo systemctl enable nvidia-resume.service
```

### nvidia-suspend.service

```ini
[Unit]
Description=NVIDIA system suspend actions
Before=systemd-suspend.service

[Service]
Type=oneshot
ExecStart=/usr/bin/logger -t suspend -s "nvidia-suspend.service"
ExecStart=/usr/bin/nvidia-sleep.sh "suspend"

[Install]
RequiredBy=systemd-suspend.service
```

### nvidia-resume.service

```ini
[Unit]
Description=NVIDIA system resume actions
After=systemd-suspend.service
After=systemd-hibernate.service

[Service]
Type=oneshot
ExecStart=/usr/bin/logger -t suspend -s "nvidia-resume.service"
ExecStart=/usr/bin/nvidia-sleep.sh "resume"

[Install]
RequiredBy=systemd-suspend.service
RequiredBy=systemd-hibernate.service
```

### nvidia-hibernate.service

```ini
[Unit]
Description=NVIDIA system hibernate actions
Before=systemd-hibernate.service

[Service]
Type=oneshot
ExecStart=/usr/bin/logger -t hibernate -s "nvidia-hibernate.service"
ExecStart=/usr/bin/nvidia-sleep.sh "hibernate"

[Install]
RequiredBy=systemd-hibernate.service
```

### nvidia

```bash
#!/bin/sh

case "$1" in
    post)
        /usr/bin/nvidia-sleep.sh "resume"
        ;;
esac
```

### nvidia-sleep.sh

```bash
#!/bin/bash

if [ ! -f /proc/driver/nvidia/suspend ]; then
    exit 0
fi

RUN_DIR="/var/run/nvidia-sleep"
XORG_VT_FILE="${RUN_DIR}"/Xorg.vt_number

PATH="/bin:/usr/bin"

case "$1" in
    suspend|hibernate)
        mkdir -p "${RUN_DIR}"
        fgconsole > "${XORG_VT_FILE}"
        chvt 63
        if [[ $? -ne 0 ]]; then
            exit $?
        fi
        echo "$1" > /proc/driver/nvidia/suspend
        exit $?
        ;;
    resume)
        echo "$1" > /proc/driver/nvidia/suspend 
        #
        # Check if Xorg was determined to be running at the time
        # of suspend, and whether its VT was recorded.  If so,
        # attempt to switch back to this VT.
        #
        if [[ -f "${XORG_VT_FILE}" ]]; then
            XORG_PID=$(cat "${XORG_VT_FILE}")
            rm "${XORG_VT_FILE}"
            chvt "${XORG_PID}"
        fi
        exit 0
        ;;
    *)
        exit 1
esac
```

Dan setelah memasang beberapa script tersebut, PC saya bisa suspend dengan normal seperti sediakala. Sekian dari saya. Terima kasih.