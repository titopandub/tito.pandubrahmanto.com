---
layout: post
title: Ciri-ciri Seorang Software Engineer yang Sangat Baik
description: Tiga hal yang menurut saya adalah ciri-ciri software engineer yang sangat baik.
date: 2022-02-22 22:22:22.222222222 +07:00
type: post
published: true
status: publish
permalink: /2022-02-22-ciri-software-engineer/
categories: 
- Software Engineer
tags:
- trait
- timeboxing
- learning
comments: true
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---

## Apa ciri-ciri seorang Software Engineer yang sangat baik?

Saya sering mendapatkan pertanyaan ini dari teman-teman, terutama pada saat one-on-one. Ini menunjukan orang tersebut ingin mengetahui ekspektasi dari seorang atasan atau mentornya terhadap dirinya sendiri. Jawaban dari pertanyaan ini kemungkinan besar berbeda dari setiap orang. Saya akan mencoba memberikan jawaban yang menurut saya merupakan ekspektasi saya untuk seorang Software Engineer yang sangat baik.

![Photo by Martin Shreder on Unsplash]({{ site.baseurl }}/assets/martin-shreder-5Xwaj9gaR0g-unsplash.jpg "Photo by Martin Shreder on Unsplash")
<p align=center>Photo by <a href="https://unsplash.com/@martinshreder?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Martin Shreder</a> on <a href="https://unsplash.com/s/photos/technology?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a></p>

## Apakah skill pada bahasa pemrograman tertentu?

Mungkin. Skill yang sangat dalam pada suatu bahasa pemrograman menunjukan kualitas seorang programmer pada bahasa tersebut. Meskipun itu adalah hal yang baik, namun tuntutan kita saat ini (terutama untuk full-cycle engineer) adalah menguasai beberapa bahasa pemrograman. Sangatlah tidak praktis jika kita harus menguasai (sampai dalam) semua bahasa yang kita butuhkan sehari-hari. Biasanya dalam satu waktu, seseorang hanya fokus pada satu atau dua bahasa pemrograman untuk di dalami. Meskipun tidak menutup kemungkinan orang tersebut juga memahami bahasa pemrograman lainnya.

Jika seseorang memiliki skill yang dalam pada suatu bahasa pemrograman bukan berarti tidak baik, karena hal ini pondasi dalam meniti karir sebagai software engineer.

## Apakah skill pada disiplin tertentu?

Mungkin. Dari pengalaman saya bekerja, biasanya sebuah perusahaan akan membagi disiplin dari software engineer menjadi beberapa bagian. Misalnya back-end, front-end (web), mobile app (Android, iOS, dll), data engineer, dev ops, data scientist, machine learning engineer dan banyak lagi. Skill yang dikembangkan oleh seseorang biasanya akan berfokus kepada disiplin yang dia inginkan, sukai atau memang ditugaskan. Beforkus pada disiplin kita adalah hal penting untuk dilakukan apalagi dalam konteks karir yang ingin kita raih. Akan tetapi hal ini bukanlah ciri-ciri yang menentukan seseorang itu adalah Software Engineer yang sangat baik. Ini lebih kepada pondasi dari apa yang kita kerjakan.

Mengapa saya merasa ini bukanlah ciri-ciri yang menentukan? Karena Software Engineer yang menurut saya mempunyai predikat sangat baik, selalu bisa beradaptasi dengan cepat di manapun dia ditempatkan. Seakan-akan mereka menguasai semua bahasa pemrograman dan disiplin dalam software engineer.

## Kalau bukan dua itu, lalu apa?

Saya ingin mengajukan tiga ciri yang menurut saya hampir selalu saya dapati pada orang-orang yang memiliki predikat ini, yaitu:

### Keberanian, kemauan dan kemampuan untuk menyelesaikan masalah sampai pada akarnya.

Seorang engineer bisa kita ukur kualitasnya saat mereka menghadapi sebuah masalah. Seringkali saat menghadapi masalah, kita menyelesaikannya dengan cara menambahkan "work-around". Work-around ini menurut [Merriam-Webster](https://www.merriam-webster.com/dictionary/work-around) adalah sebuah rencana atau metode untuk melewati atau menyelesaikan masalah tanpa menghilangkan penyebabnya. Meskipun hal ini tidak buruk, di mana seringkali kita perlu melihat "effort" yang dibutuhkan jika dibandingkan dengan "impact"-nya, akan tetapi jika masalah tersebut datang untuk kedua kalinya, itu merupakan tanda agar kita fokus untuk mencari cara menghilangkan sebab atau akar dari masalah tersebut.

Saat kita mengambil keputusan untuk menyelesaikan masalah tersebut, kita sendiri seringkali mendapatkan kebuntuan. Karena saat kita periksa, kita merasa hal tersebut sudah baik akan tetapi "work-around" yang kita pasang tidak bisa menyelesaikan masalahnya. Jika itu terjadi, kemungkinan masalah tersebut ada di bawah layer yang kita kerjakan. Nah, keberanian, kemauan dan kemampuan untuk "nyemplung" ke layer di bawahnya inilah yang menentukan apakah kita seorang yang memiliki kualitas.

Misalnya kita menemukan aplikasi kita mendapatkan timeout dari aplikasi lain. Padahal aplikasi yang kita panggil ini, latency internalnya tidak seburuk dari yang kita dapatkan. Ping ke IP tersebut, juga tidak menunjukan network latency yang besar. Masalah bisa terjadi di banyak tempat, misalnya connection yang dibuat terlalu banyak (tidak menggunakan HTTP persistent connection), ada masalah pada network, load balancer, atau aplikasi lain ini sebenarnya sudah pada limitnya, namun tidak terlihat, karena instrumentasinya tidak menyertakan Request Queue. Hal-hal ini yang harus kita periksa dan analisa sampai kita menemukan penyebabnya. Akan tetapi, seringkali ini bukanlah merupakan "expertise" kita. Kita jadi ragu untuk memeriksa ke sana dan lebih menyerahkan hal tersebut ke orang lain yang mungkin tidak mengetahui konteksnya.

Saran dari saya, cobalah pelajari tools yang bisa membantu melihat lebih dalam. Seperti `tcpdump`, `strace`, `lsof` (saya pernah menulisnya [di sini](https://blog.kmkonline.co.id/belajar-strace-gdb-and-lsof-6a5fd49d9947)), `wireshark` dan banyak lagi. Dan ajak pair orang yang kita minta untuk memeriksa hal tersebut. Dengan pairing, kita bisa melihat dan belajar prosesnya, di sisi lain kita juga bisa memberikan masukan di sisi mana lagi yang perlu diperiksa atau di-analisa.

Selanjutnya, bersiaplah untuk membaca dokumentasi (lagi dan lagi), github issue dan source code dari library yang kita gunakan (jika kita curiga masalahnya ada di library). Dengan begitu, kita bisa lebih mengerti masalah yang kita hadapi dan mudah-mudahan bisa menemukan solusinya. Hal ini perlu, karena kebanyakan dari kita berdiri (membuat software) menggunakan abstraksi yang sudah dibuat sebelumnya oleh orang lain. Dari CPU instruction set ke assembly, lalu ke kernel, lalu ke syscall, lalu ke virtual machine (kalau bahasa pemrograman kita menggunakan ini), lalu ke bahasa pemrograman, lalu ke standard library, lalu ke library, lalu ke framework, baru sampai pada code kita. Kita tidak harus mengetahui semuanya, tapi kita perlu keberanian untuk mencari diantara abstraksi tersebut.

### Kemampuan untuk membatasi waktu dalam setiap penyelesaian masalah (timeboxing).

Ciri yang kedua adalah membatasi waktu untuk menyelesaikan masalah. Dalam pekerjaan kita, kita sering merasa mentok atau "stuck". Apakah itu karena dokumentasinya tidak jelas, kita coba sebuah snippet namun tidak bisa, mendapatkan error yang kita tidak mengerti maksudnya dan banyak "roadblock" lainnya. Menghadapi ini, sebagai engineer, kadang ada rasa tertantang, kita akan cari StackOverflow, bongkar dokumentasi, baca source code library dan melakukan aktifitas lainnya untuk mencari tahu. Hal ini pasti menyita waktu kita. Karena rasa tertantang ini seringkali kita juga lupa bahwa kita memiliki rekan-rekan yang ada di perusahaan, di group sosial media atau di tempat lain, yang sebenarnya mungkin sudah pernah menyelesaikan masalah ini atau lebih mengerti tentang masalah ini. Timeboxing ini berguna agar kita membatasi waktu kita untuk fokus mencari dan mulai bertanya, pairing, meminta bantuan atau bahkan "give up" untuk saat ini.

Dengan timeboxing ini, kita bisa membatasi waktu untuk kita "spike" sebuah solusi, mencari solusi dari masalah yang kita hadapi, "slack time" untuk mengeksplor sesuatu. Dan dengan komunikasi yang baik, timeboxing akan menjadikan kita seorang software engineer yang accountable. Bukan seseorang yang "bertapa" berhari-hari, berminggu-minggu bahkan berbulan-bulan yang pada akhirnya memberikan solusi yang sebenarnya sudah tidak relevan lagi. Dalam Agile kita dituntut untuk bisa memberikan working software agar mendapatkan umpan balik secepat mungkin. Timeboxing merupakan skill yang dibutuhkan oleh seorang software engineer.

### Selalu belajar, siap belajar

Ciri yang ketiga adalah selalu belajar dan siap untuk belajar. Selalu belajar merupakan sifat yang harus tertanam di dalam diri kita sebagai seorang profesional. Hal ini agar kita tetap relevan di dunia pekerjaan yang memiliki perkembangan sangat cepat. Kita juga perlu memfokuskan topik yang ingin kita pelajari, karena waktu yang ada pasti selalu tidak cukup. Saran saya, usahakan dalam satu waktu selalu ada buku yang kita fokus baca, course yang kita fokus pelajari dan kerjakan. Kita boleh mengikuti blog dan podcast, akan tetapi kedalaman ilmu sebuah buku atau course menurut saya tidak sebanding dengan sebuah artikel atau podcast.

Untuk siap belajar maksudnya adalah kita siap untuk belajar sesuatu yang baru yang kita temukan dalam proses menyelesaikan masalah yang kita hadapi. Belajar tools, library, buku atau hal lain yang dibutuhkan saat kita mengupas lapisan-lapisan dari abstraksi. Hal ini cukup jarang saya temukan, karena biasanya orang hanya mau fokus ke hal yang dia sukai. Padahal sebagai seorang profesional dan "knowledge worker", skill kita untuk cepat beradaptasi dan belajar hal yang baru sangatlah dibutuhkan.

Tips dari saya, cobalah berlangganan ACM. Untuk Indonesia, berlangganan ACM ini sekitar USD 25 per tahun. Pilih negara Indonesia di [link ini](https://services.acm.org/public/qj/proflevel/countryListing.cfm?promo=PWEBTOP&form_type=Professional) untuk mendaftar. Menurut saya USD 25 ini sangat murah dibandingkan manfaat yang didapat untuk mengakses [OReilly](https://www.oreilly.com/). Dengan ini proses untuk selalu belajar dan siap belajar akan dapat dengan mudah kita jalani.

## Kesimpulan

Ketiga ciri yang saya sampaikan bukan berarti hanya itu yang dibutuhkan. Penguasaan terhadap bahasa pemrograman, disiplin, patterns, framework, Agile software development dan skill lainnya, akan tetap menjadi pondasi ilmu kita. Namun ketiga ciri ini perlu juga kita miliki dengan cara mengasah, melatih dan menggunakannya saat ada kesempatan. Saya belum pernah melihat seorang software engineer yang memiliki kualitas sangat baik yang tidak memiliki ketiga ciri tersebut. Apakah saya kurang gaul? Mungkin.

Terima kasih sudah membaca, jika ada komentar, kritik dan saran, boleh ditulis dikolom komentar.