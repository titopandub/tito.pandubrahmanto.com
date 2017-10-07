---
layout: post
title: Solusi Mencari Driver Komputer atau Laptop
date: 2014-11-13 11:27:53.000000000 +07:00
type: post
published: true
status: publish
permalink: /computer/solusi-mencari-driver-komputer-atau-laptop/
categories:
- Computer
tags:
- driver
- komputer
- laptop
meta:
  _spost_short_title: ''
  _yoast_wpseo_title: Solusi Mencari Driver Komputer - Blog of Tito Pandu
  _yoast_wpseo_metadesc: Bagaimana cara mencari driver komputer atau laptop yang website
    vendornya tidak menyediakan driver dengan akurat.
  _yoast_wpseo_focuskw: driver komputer
  _yoast_wpseo_linkdex: '75'
  _edit_last: '1'
  dsq_thread_id: '5554018376'
comments: true
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---
Bingung mencari driver komputer atau laptop? CD/DVD Driver hilang dan vendor dari laptop tersebut tidak menyediakan driver di websitenya? Simak cerita singkat dari saya dalam menemukan driver VGA untuk laptop yang tidak menyediakan driver di websitenya.

## Pencarian Driver yang Hilang

Pagi ini saya menerima laptop dari teman saya. Dia bertanya apakah laptop dia bisa dipakai untuk browsing internet dengan lancar?

Saya cek spesifikasi laptop tersebut dan menemukan bahwa driver VGA tidak terinstall. Saya coba search di Google dengan keywords **"#{merk laptop} #{tipe} driver"**, ternyata tidak ada satu entry pun di page pertama dan kedua yang menyediakan driver komputer atau laptop itu. Bahkan saat saya cek website vendornya, entah kenapa tidak ada menu untuk download driver.

Kecewa dengan cara yang selama ini berhasil untuk mencari driver, saya mengintip properties dari device tersebut. Di bagian **"Details"**, lalu pada Property, saya melihat ada dropdown dengan pilihan Hardware ID / Instance ID. Saya lihat disitu ada keterangan seperti ini `PCI\VEN_...&DEV_...&......"`. Saya merasa penasaran apakah angka setelah `VEN_` dan `DEV_` dapat digunakan untuk mencari driver dari pembuat hardware-nya. Saya coba search dengan keywords **"looking driver from device instance id"** dan saya menemukan kita dapat mencarinya di beberapa situs yang memang menyediakan database vendor dan device.
Setelah membuka situs <a title="PCI Database" href="http://www.pcidatabase.com/" target="_blank">PCI Database</a>, akhirnya saya menemukan device apa yang saya butuhkan drivernya. Di situ kita langsung diberitahu merk dan type-nya, sehingga kita bisa langsung ke website vendor untuk mendownload driver. Namun sayangnya setelah saya download dan copy ke flashdisk untuk di-install di laptop teman, ternyata laptop tersebut terkena virus yang menghapus file di dalam flashdisk dan me-replace-nya dengan file virus. Akhir cerita, laptop saya kembalikan dan saya beritahukan masalah yang dihadapi.

## Kesimpulan

Untuk menutup post ini, saya akan berikan step-by-step untuk mencari driver komputer atau laptop:

1.  Search di Google menggunakan keywords **"#{merk laptop} #{tipe} driver"**
2.  Jika cara pertama berhasil, maka download dan install driver dari website vendor
3.  Jika cara pertama gagal, maka buka Control Panel, masuk ke Device Manager (Windows 7), lalu klik kanan dan klik Properties pada device yang belum terdeteksi
4.  Lalu klik tab **"Details"**
5.  Pada dropdown **"Property"**, pilih pilihan Instance ID atau Hardware ID
6.  Lihat angka setelah `VEN_` dan `DEV_`, angka setelah `VEN_` menunjukan Vendor ID dan angka setelah `DEV_` menunjukan Device ID
7.  Buka situs <a title="PCI Database" href="http://www.pcidatabase.com/" target="_blank">PCI Database</a>, search Vendor ID dengan angka yang Anda miliki, lalu search dalam halaman tersebut Device ID (menggunakan **Ctrl + F** atau **CMD + F**)
8.  Lihat Chip Description, lalu ke website vendor dari device tersebut dan carilah driver dari device sesuai keterangan ini
9.  Download dan install driver tersebut

Sekian post dari saya, terima kasih.
