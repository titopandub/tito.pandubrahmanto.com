---
layout: post
title: Pengalaman Menggunakan OS untuk Desktop
description: Dari Windows, Linux, Mac dan kembali ke Linux
date: 2017-11-30 20:05:00.000000000 +07:00
type: post
published: true
status: publish
permalink: /2017-11-30-pengalaman-menggunakan-os/
categories:
- Computer
tags:
- review
comments: true
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---
# Windows 98 - Pertama mengenal PC

Saya pertama mengenal PC pada saat kelas 2 SMP. Saat itu saya membeli PC dari hadiah memenangkan kuis Galileo. Tepatnya pada tahun 2002. Menurut saya Windows 98 adalah OS paling bagus disaat itu. Windows XP sudah ada, namun belum stabil (masih terlalu berat juga untuk PC pertama saya).

Sebagian waktu saya di PC saat itu hanyalah bermain game.

# Windows XP - Warnet

Sekitar tahun 2003, saya dan Ibu saya mendirikan warnet di rumah. Kita menggunakan Windows XP, karena networking di Windows XP lebih stabil dan lebih mudah.

Windows XP ini juga saya gunakan sebagai router di warnet, karena sudah memiliki fitur sharing network. Hal ini dikarenakan cable TV modem saat itu belum ada fungsi router.

# Debian - SMK Telkom

Saat saya masuk SMK Telkom, sebenarnya saya masih menggunakan Windows. Saya mulai mempelajari Linux bersama guru Networking saya. Saat itu pilihan menggunakan Linux hanyalah dual boot atau VM.

Karena saya memiliki PC yang cukup RAM-nya, maka saya memilih untuk mempelajari desktop Linux dengan menggunakan VM. Sebenarnya Linux cukup baik digunakan untuk desktop, namun memiliki masalah saat saya memerlukan office untuk belajar kelompok. Teman-teman dan guru saya masih menggunakan Microsoft Office, sehingga cukup sulit bagi saya untuk berbagi file.

# Windows XP - Pertama kali bekerja

Saya kembali ke Windows XP saat saya bekerja. By default, seluruh OS dari laptop atau PC kantor menggunakan Windows XP.

# Windows 7 - IT Support

Saat saya bekerja menjadi IT Support dan Network, saya menggunakan Windows 7 untuk PC di kantor. Saat itu kebanyakan PC di kantor masih menggunakan Windows XP atau Windows 2000. Masalah terbesar yang saya temui adalah infeksi virus di Windows. Hal ini jarang terjadi di Windows 7, karena secara default Windows 7 menggunakan [UAC](https://en.wikipedia.org/wiki/User_Account_Control "User Account Control"). UAC mirip seperti `sudo` di Linux.

Solusi yang sangat sederhana adalah membuat seluruh user di kantor menjadi user 'biasa' dan mengunci account administrator. Hasilnya menjadi lebih sedikit (atau hampir tidak pernah) ada infeksi virus. Hal ini membawa masalah baru, yaitu beberapa program menjadi tidak bisa digunakan, karena program tersebut membutuhkan akses administrator. Kita perlu meneliti setiap program seperti ini, file apa saja yang dibutuhkan, sehingga kita bisa memberikan hak akses file tersebut kepada Group `users` di Windows.

# Mac OS X - Freelance

Hadiah dari Ibu saya, saat saya memulai freelance adalah sebuah Macbook Pro 2011. Saat itu saya mulai menggunakan MacOS dan sangat menyukainya. Mac memiliki memory management yang lebih baik daripada Windows saat itu dan pastinya MacOS merupakan varian dari Unix. Kita bisa menjalankan program Unix di Mac. Memang kekurangannya kita harus meng-install package manager seperti [Homebrew](https://brew.sh/).

Di OS inilah saya mempelajari programming lebih mendalam. Saya mempelajari PHP, Ruby dan beberapa functional programming language seperti Elixir. Kemudahan untuk meng-install programming language menjadi kelebihan tersendiri dari OS ini.

Di sisi lainnya, UI dari MacOS sangat bagus dan halus. Di MacOS juga ada Microsoft Office, sehingga memudahkan saat saya perlu membuat document dan membagikannya kepada client.

Saya menggunakan MacOS hingga saya masuk ke KMK dan membeli Macbook Pro 2015.

# Windows 10 - KMKLabs

Setelah saya menjual Macbook Pro saya, karena mungkin merasa bosan dengan environment MacOS, saya memutuskan untuk membeli Surface Pro. Saya cukup terpana mencoba Windows 10. UI yang sangat halus, touch screen integration yang sangat baik dan presisi, membuat Windows 10 menjadi OS yang terbaik yang dibuat Microsoft.

Disamping itu Windows 10 juga memiliki fitur [Windows Subsystem for Linux (WSL)](https://msdn.microsoft.com/en-us/commandline/wsl/about) yang sangat membantu saat kita membutuhkan tools dari Unix. Sayangnya WSL masih memiliki banyak kelemahan dan keterbatasan saat yang kita butuhkan benar-benar Unix dan bukan Windows.

Di OS ini saya belajar banyak hal, terutama mencoba Visual Studio Code yang menurut saya editor yang sangat baik. Dengan Vim mode, VS Code menjadi editor yang sangat mudah digunakan (bagi saya) di Windows.

# Ubuntu - KMKLabs sampai hari ini

Pertama kali saya interview di KMK, saya sangat terheran-heran. Kenapa perusahan yang sudah mapan dari sisi Software Engineering practice menggunakan Linux (tepatnya Ubuntu). Padahal di beberapa tempat lainnya sewaktu saya interview, kebanyakan menggunakan MacOS. Entah kenapa di dunia software saat itu, Mac adalah simbol 'cool'.

Setelah bekerja di sini, saya baru sadar, ternyata Ubuntu (dan distro Linux lainnya) hari ini sudah cukup mapan dalam implementasi UI. Memang masih ada glitch di sana sini, namun dari sisi performance dan kemudahan development, saya rasa tidak ada yang mengalahkan Linux.

Dahulu saya memiliki kesulitan dalam berbagi dokumen jika saya menggunakan OS Linux, namun sekarang kemudahan dari Google Docs dan Microsoft Office Online, memberikan solusi untuk hal tersebut. Saat ini saya lebih memilih untuk berbagi dokumen via online platform, daripada membuatnya di offline lalu mengunggahnya.

Sebagai seorang developer, Linux sangatlah membantu saya dalam pekerjaan development. Saya sempat frustasi dengan Windows, karena beberapa tools development yang biasa saya gunakan menjadi sulit untuk mengaksesnya di Windows.

Saat post ini ditulis, saya menggunakan Ubuntu 17.10 dengan Emacs markdown-mode.

Itulah pengalaman saya menggunakan Desktop OS sejak saya belajar komputer hingga hari ini. Bagaimana pengalaman kalian? Silahkan tinggalkan komentar. Terima kasih telah membaca blog saya.
