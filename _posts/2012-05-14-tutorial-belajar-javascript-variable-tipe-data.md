---
layout: post
title: Tutorial Belajar JavaScript - Variable dan Tipe Data
date: 2012-05-14 11:00:40.000000000 +07:00
type: post
published: true
status: publish
permalink: /web-development/tutorial-belajar-javascript-variable-tipe-data/
categories:
- Web Development
tags:
- how to
- javascript
- learning
meta:
  _edit_last: '1'
  _syntaxhighlighter_encoded: '1'
  image: ''
  seo_follow: 'false'
  seo_noindex: 'false'
  dsq_thread_id: '689503112'
  _yoast_wpseo_linkdex: '56'
  _series_part: '2'
  _yoast_wpseo_focuskw: tutorial belajar javascript variable dan tipe data
  _yoast_wpseo_title: Tutorial Belajar JavaScript - Variable dan Tipe Data - Blog
    of Tito Pandu
  _yoast_wpseo_metadesc: Pada tutorial kali ini, kita akan belajar JavaScript mengenai
    variable dan tipe data. Kita akan fokus pada deklarasi variable dan tipe data.
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---
[![JavaScript JSconf logo]({{ site.baseurl }}/assets/JSconf_logo-150x150.png "JSconf_logo")]({{ site.baseurl }}/JSconf_logo.png)

Dalam tutorial ini, kita akan mengenal mengenai bagaimana memakai variable dalam JavaScript. JavaScript memiliki beberapa cara untuk mendeklarasikan variable dan kita akan mempelajarinya dalam tutorial ini. Saya akan membuatnya singkat, agar tidak menyita waktu Anda untuk membacanya.

Jika Anda belum membaca tutorial sebelumnya mengenai penggunaan JavaScript, saya sangat menyarankan untuk membaca post sebelumnya mengenai [Tutorial Belajar JavaScript - Pengenalan](http://tito.pandubrahmanto.com/web-development/tutorial-belajar-javascript-pengantar/ "Tutorial Belajar Javascript – Pengantar").

* * *

## Deklarasi Variable

JavaScript memiliki sifat [“Weakly Typed”](http://en.wikipedia.org/wiki/Weak_typing "Weak typing"). Artinya, JavaScript tidak membutuhkan pendeklarasian tipe data, kita hanya perlu mendeklarasikan nama variable dan isinya, sedangkan tipe data seperti string, integer atau float tidak perlu kita sebutkan. Berikut contoh pendeklarasian variable pada JavaScript.

```javascript
var helloWorld;

alert(helloWorld);
```

Hanya itu? Ya, hanya itu yang dibutuhkan untuk mendeklarasikan variable, tidak diperlukan pendeklarasian tipe data seperti pada bahasa pemrograman [Java](http://en.wikipedia.org/wiki/Java_(programming_language) "Java Programming Language") (tidak ada hubungan antara Java dengan JavaScript, hanya nama saja yang mirip). Namun saat kita menjalankan html pada browser, maka muncul kata undefined, karena tidak ada value di dalam variable tersebut. [Undefined](http://en.wikipedia.org/wiki/Undefined "Undefined") artinya tidak ada value di dalam variable atau dalam matematikan disebut tidak terdefinisi. Jangan khawatir, selanjutnya kita akan memasukkan value ke dalam variable tersebut.

* * *

## Variable Assignment

Kita sudah mempelajari bagaimana mendeklarasikan variable. Lalu bagaimana menaruh data di dalam variable, atau yang populer disebut “Assignment”. Caranya sangat mudah, yaitu.

```javascript
var helloWorld;
helloWorld = "Hello, World!";

alert(helloWorld);
```

Di dalam JavaScript kita dapat mendeklarasikan variable sekaligus memberi variable tersebut nilai. Berikut contoh sederhananya.

```javascript
var helloWorld = "Hello, World!";

alert(helloWorld);
```

Selalu ingat untuk menaruh titik koma (;) pada akhir setiap LINE pada JavaScript. Jika kita lupa untuk menaruhnya, JavaScript tidak menyatakan error, namun akan menyulitkan kita dalam memeriksa program, karena JavaScript akan memasukkan secara otomatis titik koma tersebut yang belum tentu di tempat yang kita inginkan.

* * *

## Tipe Data

Kita dapat menaruh berbagai tipe data dalam variable JavaScript, mulai dari String, Integer, Float, Array dan Object. Bahkan function juga dapat kita assign di dalam sebuah variable (sabar, kita akan mempelajarinya pada tutorial khusus mengenai function). Berikut contoh tipe data dasar pada JavaScript.

```javascript
var hello = "Hello"; // String
var world = 'World!'; // String
var x = 5; // Integer
var pi = 3.14; // Float

alert(hello);
alert(world);
alert(x);
alert(pi);
```

* * *

## Komentar pada Kode

Oh ya, sebelum saya tutup, tanda dua garis miring (double slash) digunakan untuk memberikan komentar pada kode. Dua garis miring dipakai untuk komentar satu baris, sedangkan garis miring bintang-bintang garis miring dipakai untuk komentar yang melebihi dari satu baris. Berikut contoh komentar pada JavaScript.

```javascript
// Ini komentar untuk satu baris
/*
Ini komentar untuk lebih dari satu baris
Anda dapat menaruh komentar dari Anda, sebagai penanda kode
Jangan khawatir akan mempengaruhi kode
*/
```

Komentar digunakan untuk memberikan komentar kita di dalam kode, bisa sebagai dokumentasi agar mudah dalam pemeliharaan kode tersebut bagi kita atau orang lain yang dikemudian hari mengedit kode tersebut.

* * *

Sangat mudah bukan. Kita sudahi dahulu tutorial singkat mengenai variable dan tipe data dasar pada JavaScript. Selain mempelajari pendeklarasian variable dan assignment untuk data, kita juga mengenal penggunaan komentar pada JavaScript. Di tutorial selanjutnya kita akan mempelajari mengenai “Operator” pada JavaScript.

Jangan lupa subscribe [RSS](http://feeds.feedburner.com/TitoPanduPersonalBlog "Subscribe melalui RSS") atau [email](http://eepurl.com/lFtwn "Subscribe melalui Email"), agar Anda dapat mengikuti tutorial selanjutnya. Silahkan tinggalkan komentar Anda, kritik dan saran sangat saya harapkan.

Sumber: [Tuts+ Premium Course: JavaScript Fundamentals 101](http://tutsplus.com/course/javascript-fundamentals/ "Tuts+ Premium Course: JavaScript Fundamentals 101") oleh Jeremy McPeak
