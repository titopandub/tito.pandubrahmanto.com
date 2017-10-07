---
layout: post
title: Tutorial Belajar JavaScript - Loop
date: 2012-11-24 09:00:27.000000000 +07:00
type: post
published: true
status: publish
permalink: /web-development/tutorial-belajar-javascript-loop/
categories:
- Web Development
tags:
- how to
- Internet
- javascript
- to twit
meta:
  _edit_last: '1'
  _yoast_wpseo_linkdex: '67'
  _syntaxhighlighter_encoded: '1'
  image: ''
  _yoast_wpseo_focuskw: belajar javascript loop
  _yoast_wpseo_title: Tutorial Belajar JavaScript - Loop - Blog of Tito Pandu
  _yoast_wpseo_metadesc: Pada tutorial kali ini, kita akan belajar JavaScript mengenai
    Loop. Beberapa fungsi yang dipelajari yaitu while, do .. while dan for.
  _series_part: '10'
  _spost_short_title: ''
comments: true
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---
<p><img class="size-thumbnail wp-image-1446" title="JSconf_logo" alt="JavaScript JSconf logo" src="{{ site.baseurl }}/assets/JSconf_logo-150x150.png" width="150" height="150" /></p>
<p>Pada tutorial sebelumnya, yaitu <a title="Tutorial Belajar JavaScript – Control Flow" href="http://tito.pandubrahmanto.com/web-development/tutorial-belajar-javascript-control-flow/" target="_blank">Tutorial Belajar JavaScript - Control Flow</a>, kita telah mempelajari banyak hal tentang Control Flow dalam pemrograman JavaScript. Kita akan mempelajari Loop pada kesempatan kali ini.</p>
<p>Setiap bahasa pemrograman pasti memiliki fungsi ini. Tanpa fungsi ini, maka akan sangat sulit untuk menulis sebuah program. Fungsi Loop (seperti namanya) digunakan untuk mengeksekusi suatu baris kode berulang-ulang sesuai dengan kondisi yang diberikan. Dalam JavaScript dikenal beberapa fungsi Loop, yaitu <code>while</code>, <code>do while</code> dan <code>for</code>. Kita akan mengulasnya bersama-sama.<br /></p>

## 1. `while` Loop

Loop yang paling simpel adalah `while`. Kita hanya membutuhkan parameter kondisi yang jika kondisi tersebut terpenuhi (true) maka baris kode yang ada di dalam while akan dieksekusi. Berikut contoh sederhana dari while.

```javascript
var i = 0;
while (i < 7) {
  i++;
  console.log(i);
}
```

note: Cobalah kode di atas dengan menghidupkan console pada web browser. Untuk referensi cek post mengenai <a title="Cara Lain untuk Menjalankan JavaScript" href="http://tito.pandubrahmanto.com/web-development/cara-menjalankan-javascript/" target="_blank">Cara Lain Menjalankan JavaScript</a>. Jangan pernah lupa untuk memberikan *iterator* di dalam blok perulangan, dalam hal ini adalah `i++`

## 2. `do .. while` Loop

Dengan sintaks yang mirip (dengan tambahan `do`), namun memiliki karakteristik yang berbeda. Perbedaannya adalah sintaks ini akan selalu mengeksekusi blok satu kali pada saat mulai baru mengecek parameter kondisi untuk melakukan looping. Berikut contohnya.

```javascript
var i = 7;
do {
  i++;
  console.log(i);
}
while (i < 7)
```

Bila kita menjalankan kode di atas, maka akan muncul hasil 8. Meskipun nilai parameter `false`, looping ini akan tetap menjalankan blok satu kali.

Untuk kedua sintaks di atas jangan pernah lupa untuk membuat *iterator* (penghitung) dan memberi *increment* untuk nilai tersebut. Jika tidak, maka akan terjadi [infinite loop](http://en.wikipedia.org/wiki/Infinite_loop "Infinite Loop") (perulangan yang tidak terbatas atau tidak akan berhenti)

## 3. `for` Loop

Untuk melakukan looping yang lebih kompleks, sangat disarankan untuk memakai sintaks ini. Sintaks ini membutuhkan parameter _iterator_ (penghitung), kondisi, dan _incremental_. Berikut contoh sederhana.

```
for (i = 0; i < 10; i++) {
  console.log(i);
}
```

Kode di atas untuk menulis 0-9 ke console. Namun, jika kita ingin melakukan iterasi untuk elemen dalam Array, kita dapat menggunakan properti `length` yang disediakan oleh type data Array. Berikut contohnya.

```javascript
arrayNama = ['Tito', 'Pandu', 'Brahmanto'];

for (i = 0; i < arrayNama.length; i++) {
  console.log(arrayNama[i]);
}
```

Cara paling mudah adalah menggunakan for loop sesuai contoh di atas, tapi cara tersebut kurang baik. Karena `length` properti dari arrayNama akan di hitung disetiap iterasi. Mungkin hal ini adalah hal yang sepele untuk sepotong kode seperti di atas, tapi bila kita bekerja untuk aplikasi yang besar dan iterasi tidak hanya 10 kali, maka hal tersebut bisa memberatkan aplikasi yang kita buat.

Berikut contoh `for` loop untuk array yang lebih baik.

```javascript
arrayNama = ['Tito', 'Pandu', 'Brahmanto'];

for (i = 0, j = arrayNama.length; i < j; i++) {
  console.log(arrayNama[i]);
}
```

## 4. `for .. in` Loop

Tidak jauh berbeda dengan `for` Loop sebelumnya, jenis loop ini biasanya dipakai untuk menyebutkan properti dari suatu Objek satu per satu. Berikut adalah contoh sederhananya.

```javascript
nama = {
  firstName: 'Tito',
  middleName: 'Pandu',
  lastName: 'Brahmanto'
};

for (i in nama) {
  console.log(i + ' : ' + nama[i]);
}
```

Bagi yang jarang membaca sintaks JavaScript, pasti heran dengan `nama[i]`. Mengapa properti dalam Objek pada JavaScript dapat diakses dengan cara mengakses isi dari Array? Jawabannya bisa dan hal tersebut adalah salah satu feature dalam JavaScript.

Sekian tutorial yang sangat singkat mengenai `Loop` dalam JavaScript. Banyak yang bisa kita gali dari bahasan ini. Selanjutnya kita akan mempelajari mengenai Window Object dalam JavaScript secara detail .

Jangan lupa subscribe [RSS](http://feeds.feedburner.com/TitoPanduPersonalBlog "Subscribe to RSS") atau [email](http://eepurl.com/lFtwn "Subscribe by Email"), agar Anda dapat mengikuti tutorial selanjutnya. Silahkan tinggalkan komentar Anda, kritik dan saran sangat saya harapkan.

Sumber: [Tuts+ Premium Course: JavaScript Fundamentals 101](http://tutsplus.com/course/javascript-fundamentals/ "Tuts+ Premium Course: JavaScript Fundamentals 101") oleh Jeremy McPeak
