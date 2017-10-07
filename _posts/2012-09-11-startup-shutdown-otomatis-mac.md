---
layout: post
title: Menjadwalkan Start up dan Shutdown Secara Otomatis di Mac OS X
date: 2012-09-11 10:00:32.000000000 +07:00
type: post
published: true
status: publish
permalink: /mac/startup-shutdown-otomatis-mac/
categories:
- Mac
tags:
- how to
- Mac OS
- to twit
meta:
  _edit_last: '1'
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
[![Schedule Start up dan Shutdown]({{ site.baseurl }}/assets/Screen-shot-2012-09-11-at-8.04.54-AM-300x216.png "Schedule Start up dan Shutdown di System Preferences")]({{ site.base_url }}/assets/Screen-shot-2012-09-11-at-8.04.54-AM.png)

Mac OS X menyediakan sebuah fitur untuk secara otomatis Start up (Wake) dan Shutdown (Restart atau Sleep) di Mac pada waktu tertentu. Mari kita simak tips singkat berikut ini.

Berikut langkah-langkahnya:

1.  Buka "System Preferences" melalui logo Apple -> `System Preferences...`
2.  Buka menu `Energy Saver` (icon lampu neon)
3.  Klik `Schedule...`
4.  Centang `Start up or wake` lalu set waktu untuk menghidupkan Mac secara otomatis, misalnya Anda ingin menghidupkan Mac pada pagi hari saat Anda bangun
5.  Centang untuk dropdown list (Sleep, Restart atau Shutdown) untuk otomatis Sleep, Restart atau Shutdown (mematikan) Mac secara otomatis

Sangat mudah bukan untuk melakukannya. Mac OS X memberikan fitur default untuk melakukannya. Kita juga bisa melakukannya menggunakan Terminal. Karena Mac OS X merupakan turunan dari UNIX maka kita juga dapat menggunakan command "shutdown" milik UNIX. Namun ini hanya berlaku untuk Shutdown atau Restart. Caranya

1.  Buka Terminal dari Applications -> Utilities -> Terminal
2.  Ketik `sudo shutdown -h 09:00` lalu masukkan password untuk melakukan Shutdown pada jam 9 pagi. Waktu ditulis dengan format 24 jam
3.  Untuk melakukan Restart, ganti opsi `-h` dengan `-r`

Sekian tips singkat dari saya, sebagai pelengkap tips yang ditulis oleh rekan saya Hendy dari [GearCheck.net](http://gearcheck.net/ "GearCheck.net Personally Checked") pada post [Tips & Tricks: Scheduling auto shutdown for Windows 7, XP, Vista](http://gearcheck.net/scheduling-auto-shutdown-for-windows-7-xp-vista/ "Tips & Tricks: Scheduling auto shutdown for Windows 7, XP, Vista")

Semoga bermanfaat.
