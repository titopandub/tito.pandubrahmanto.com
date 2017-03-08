---
layout: post
title: Tutorial Belajar JavaScript - String
date: 2012-07-07 10:00:33.000000000 +07:00
type: post
published: true
status: publish
permalink: /web-development/tutorial-belajar-javascript-string/
categories:
- Web Development
tags:
- how to
- Internet
- javascript
meta:
  _syntaxhighlighter_encoded: '1'
  _edit_last: '1'
  image: ''
  seo_follow: 'false'
  seo_noindex: 'false'
  _yoast_wpseo_linkdex: '64'
  _series_part: '6'
  _yoast_wpseo_focuskw: tutorial belajar javascript string
  _yoast_wpseo_title: Tutorial Belajar JavaScript - String - Blog of Tito Pandu
  _yoast_wpseo_metadesc: Pada tutorial kali ini, kita akan belajar JavaScript mengenai
    tipe data String. Kita akan mengenal beberapa properti dan metode dari String.
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---
[![JavaScript JSconf logo]({{ site.baseurl }}/assets/JSconf_logo-150x150.png "JSconf_logo")]({{ site.baseurl }}/assets/JSconf_logo.png)

Pada tutorial yang lalu mengenai [Scope pada JavaScript]({{ site.baseurl }}/web-development/tutorial-belajar-javascript-scope/ "Tutorial Belajar JavaScript – Scope"), kita telah mempelajari banyak hal tentang Scope dalam pemrograman JavaScript. Saat ini kita akan membahas mengenai objek dengan menggunakan String. Bagi para pembaca yang pernah mempelajari bahasa pemrograman lainnya pasti sudah familiar dengan objek String. Beberapa fungsi bahkan mungkin sama dengan fungsi dalam objek String di bahasa pemrograman lainnya, tapi Anda perlu membaca pembahasan ini, karena mungkin penggunaannya yang berbeda di dalam pemrograman JavaScript.

Dalam JavaScript, String adalah Objek dan karena kita sudah familiar dengan konsep String, kita akan mempelajarinya sebagai dasar dalam mempelajari Objek. Objek selalu memiliki dua hal, yaitu Properti dan Metode. Properti adalah data yang berhubungan dengan Objek. Sedangkan Metode adalah operasi yang melakukan sesuatu kepada Objek tersebut atau data (properti). Sebagai contoh sederhana sebuah Objek, misalnya kipas angin. Kipas angin memiliki baling-baling, motor listrik, on/off switch, dan stop kontak. Itu semua adalah properti dari sebuah kipas angin. Sedangkan sebagai metode, kipas angin tersebut dapat memutar baling-baling dalam kecepatan tertentu.

* * *

## Properti

Salah satu properti dalam setiap objek string adalah `length`. `length` adalah jumlah karakter dalam objek string. Berikut contohnya.

```javascript
var objek = "Ini adalah objek string";
var length = objek.length; // 23

alert(length);
```

Akan muncul popup dengan angka 23.

* * *

## Metode

Selain properti, objek string juga memiliki banyak metode. Beberapa dari metode yang ada pada objek String akan kita bahas pada tutorial ini.

### 1\. indexOf

Metode yang kita bahas pertama adalah `indexOf`. Metode ini akan mencari karakter atau gabungan karakter di dalam string, lalu mengembalikan nilai indeks dari karakter atau gabungan karakter tersebut. Berikut adalah contohnya.

```javascript
var objek = "Ini adalah objek string";
var indeks = objek.indexOf("I"); // 0

alert(indeks);
```

Popup akan menampilkan angka 0\. Mengapa 0 dan bukan 1? Karena dalam pemrograman, indeks akan selalu dimulai dari 0\. Maka indeks dari "I" adalah 0, karena merupakan karakter pertama.

`indexOf` akan mengembalikan nilai indeks dari karakter atau gabungan karakter yang pertama, jadi saat mencari karakter atau gabungan karakter, fungsi ini akan langsung mengembalikan nilai indeks dan berhenti dalam mencari. Maka kita akan melihat hanya satu nilai indeks yang dihasilkan dari fungsi ini.

`indexOf` secara default dapat mencari mulai dari indeks pertama (dalam hal ini 0). Namun kita dapat menentukan indeks dimulainya pencarian. Kita hanya perlu menambahkan parameter kedua yang berupa angka. Berikut contohnya.

```javascript
var objek = "Ini adalah objek string";
var indeks = objek.indexOf("i", 3); // 20

alert(indeks);
```

Angka 3 digunakan sebagai awal, karena "i" dengan huruf kecil pertama ada di indeks ke-2\. Oh ya, `indexOf` mencari string secara case sensitive atau memperhatikan besar kecilnya huruf. Berikut contoh sederhana.

```javascript
var objek = "Ini adalah objek string";
var indeks = objek.indexOf("In"); // 0
var indeks2 = objek.indexOf("in"); // 20

alert(indeks);
alert(indeks2);
```

* * *

### 2\. lastIndexOf

Ada metode lain selain `indexOf` yang sangat mirip cara kerjanya, namun kebalikan dari `indexOf`, metode atau fungsi ini mencari dari kanan ke kiri. Fungsi/metode ini adalah `lastIndexOf`. Berikut contohnya.

```javascript
var objek = "Ini adalah objek string";
var indeks = objek.lastIndexOf("i"); // 20
var indeks2 = objek.lastIndexOf("i", indeks - 1); // 2

alert(indeks);
```

Hasil dari kode di atas adalah 20\. Karena fungsi ini memulai pencarian dari kanan ke kiri. Sedangkan pada indeks2, kita memakai indeks sebagai parameter kedua dan memulai pencarian dari indeks sebelumnya (indeks - 1), sehingga akan didapat hasil 2.

* * *

### 3\. substr dan substring

Selanjutnya kita akan membahas metode string yang mungkin sangat familiar yaitu substring. Dalam JavaScript terdapat dua metode yang memiliki fungsi mengambil bagian string dari string, yaitu `substr` dan `substring`. Perbedaan dari keduanya terdapat dalam parameter yang kita berikan. Mari kita lihat contoh agar lebih mudah dalam memahaminya.

```javascript
var objek = "Ini adalah objek string";
var substr = objek.substr(0, 3);
var substring = objek.substring(0,3);

alert(substr);
alert(substring);
```

Metode `substr` membutuhkan dua parameter, parameter pertama adalah indeks awal dari string yang mau diekstrak, parameter kedua adalah jumlah huruf yang akan diekstrak/diambil. Kita memakai 0 sebagai parameter pertama dan 3 sebagai parameter kedua, maka string yang terekstrak adalah "Ini".

Sedangkan metode `substring` membutuhkan parameter pertama sebagai indeks awal dan parameter kedua sebagai akhir dari indeks string yang diekstrak. Namun kita harus berhati-hati, karena karakter yang berada pada indeks parameter kedua tidak akan diekstrak oleh metode ini.

* * *

### 4\. replace

Metode selanjutnya adalah `replace`. Metode atau fungsi ini berguna untuk mengganti karakter atau kata di dalam sebuah string dengan karakter atau kata yang sudah kita tentukan. Namun dalam prosesnya, tidak akan mengganti string yang sebelumnya (original). Mari kita lihat pada contoh berikut ini.

```javascript
var objek = "Ini adalah objek string";
var hasil = objek.replace("string", "dalam JavaScript");

alert(hasil);
alert(objek);
```

Pada contoh di atas akan muncul "Ini adalah objek dalam JavaScript" dan yang kedua muncul "Ini adalah objek string". Hal ini menunjukan bahwa string yang aslinya tidak berubah. Proses yang tidak merubah variable yang diproses disebut proses yang _"non-destructive method"_. Metode ini case sensitive, sehingga besar kecilnya huruf adalah hal yang berbeda.

* * *

### 5\. toUpperCase dan toLowerCase

Metode ini ada hampir disetiap bahasa pemrograman. Metode ini berguna untuk merubah semua huruf menjadi huruf besar (`toUpperCase`) atau huruf kecil (`toLowerCase`). Metode ini tidak merubah variable original. Mari kita lihat pada contoh berikut.

```javascript
var objek = "Ini adalah objek string";
var hasil = objek.toUpperCase();
alert(hasil);

hasil = objek.toLowerCase();
alert(hasil);
```

* * *

Sekian tutorial yang sangat singkat mengenai Objek dan String dalam JavaScript. Banyak yang bisa kita gali dari bahasan ini. Selanjutnya kita akan mempelajari mengenai tipe data "_Object_" secara mendetail.

Jangan lupa subscribe [RSS](http://feeds.feedburner.com/TitoPanduPersonalBlog "Subscribe to RSS") atau [email](http://eepurl.com/lFtwn "Subscribe by Email"), agar Anda dapat mengikuti tutorial selanjutnya. Silahkan tinggalkan komentar Anda, kritik dan saran sangat saya harapkan.

Sumber: [Tuts+ Premium Course: JavaScript Fundamentals 101](http://tutsplus.com/course/javascript-fundamentals/ "Tuts+ Premium Course: JavaScript Fundamentals 101") oleh Jeremy McPeak
