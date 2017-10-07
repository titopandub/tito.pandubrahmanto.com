---
layout: post
title: Solusi WordPress 3.4.1 Error "Missed schedule"
date: 2012-07-28 10:00:11.000000000 +07:00
type: post
published: true
status: publish
permalink: /web-development/wordpress-missed-schedule/
categories:
- Web Development
tags:
- how to
- Internet
- to twit
- Wordpress
meta:
  _edit_last: '1'
  _syntaxhighlighter_encoded: '1'
  image: ''
  seo_follow: 'false'
  seo_noindex: 'false'
  _spost_short_title: ''
comments: true
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---
Dalam beberapa minggu terakhir, saya mengalami error dalam mempublikasikan post yang terjadwal. Setiap kali saya menjadwalkan waktu untuk mempublikasikan post, maka pada saat seharusnya post tersebut dipublikasikan muncul pesan error "Missed schedule".

Saya berusaha mencari solusi atas masalah ini, memang beberapa solusi dapat dengan mudah kita temukan dengan hanya mengetik pesan error, namun tidak selalu dapat menyelesaikan masalah. Berikut ini saya sampaikan beberapa solusi terbaik dan solusi yang berhasil untuk blog saya.

## Menggunakan plugin [WP Missed Schedule Fix Future Posts Scheduled Failed](http://wordpress.org/extend/plugins/wp-missed-schedule/ "WP Missed Schedule Fix Future Posts Scheduled Failed")

Anda dapat memasang plugin ini ke dalam blog jika memiliki masalah ini. Plugin ini akan mencari post dengan status "Missed schedule" dan mempublikasikan post tersebut kembali. Proses ini berjalan setiap 5 menit untuk mencari post yang bermasalah dan akan membetulkan 5 post dalam setiap lima menit tersebut. Hal ini agar tidak membebani server.

Menurut sumber yang saya baca, plugin ini tidak akan secara otomatis mengerjakan action yang menyertai publikasi post (via plugin atau perubahan core file). Misalnya kita memiliki plugin untuk men-tweet secara otomatis bila kita mempublikasikan post, maka hal ini tidak akan terjadi bila post kita mengalami error "Missed schedule" dan kita memakai plugin ini sebagai solusinya.

Plugin ini sangat bagus, namun bila Anda memiliki plugin dengan cara kerja seperti yang disebutkan sebelumnya, maka hal ini tidak akan terjadi secara otomatis.

## Merubah timeout pada cron.php

Dalam folder `wp-includes` ada sebuah file bernama `cron.php` (File ini akan otomatis kembali seperti semula saat Anda mengupdate  WordPress) di dalamnya terdapat nilai `timeout` untuk menjalankan proses cron. Jika nilai tersebut terlalu kecil, kemungkinan cron tidak dapat menyelesaikan seluruh pekerjaannya dalam waktu yang singkat.

Ubahlah file tersebut, temukan line ke 248, Anda dapat mengubah nilai `timeout` dari `0.01` menjadi `1.00`.

[![Screenshot editing cron.php pada folder wp-includes]({{ site.baseurl }}/assets/Screen-shot-2012-07-27-at-11.28.22-PM.png "Screen shot 2012-07-27 at 11.28.22 PM")]({{ site.baseurl }}/assets/Screen-shot-2012-07-27-at-11.28.22-PM.png)

## Menggunakan alternatif WP_Cron

Solusi ini yang saya pakai dan sukses. Anda dapat menggunakan fungsi alternatif yang disediakan oleh WordPress bila fungsi utama error atau tidak dapat dipakai. Kita tinggal menambahkan sebaris kode ke dalam `wp-config.php`.

```
define('ALTERNATE_WP_CRON', true);
```

Sekali lagi, solusi yang berhasil untuk saya, belum tentu berhasil untuk Anda. Karena masalah ini bisa terjadi dikarenakan oleh misconfiguration dari hosting atau dari plugin lain dalam instalasi blog WordPress Anda. Jika Anda ingin mencoba me-non-aktifkan seluruh plugin, lalu mengaktifkan satu persatu, mungkin Anda dapat mengatasi masalah ini tanpa "mengoprek" blog Anda. Tapi untuk menghemat waktu, solusi yang saya berikan mungkin dapat membantu Anda.
