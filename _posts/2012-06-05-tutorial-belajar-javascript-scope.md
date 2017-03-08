---
layout: post
title: Tutorial Belajar JavaScript - Scope
date: 2012-06-05 10:00:38.000000000 +07:00
type: post
published: true
status: publish
permalink: /web-development/tutorial-belajar-javascript-scope/
categories:
- Web Development
tags:
- how to
- Internet
- javascript
meta:
  _edit_last: '1'
  seo_follow: 'false'
  image: ''
  seo_noindex: 'false'
  _syntaxhighlighter_encoded: '1'
  _yoast_wpseo_linkdex: '61'
  _series_part: '5'
  _yoast_wpseo_focuskw: tutorial belajar javascript scope
  _yoast_wpseo_title: Tutorial Belajar JavaScript - Scope - Blog of Tito Pandu
  _yoast_wpseo_metadesc: Pada tutorial kali ini, kita akan belajar JavaScript mengenai
    scope. Kita akan mempelajari perbedaan dan penggunaan Global dan Local Scope.
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---
[![JavaScript JSconf logo]({{ site.baseurl }}/assets/JSconf_logo-150x150.png "JSconf_logo")]({{ site.baseurl }}/assets/JSconf_logo.png)

Pada tutorial sebelumnya mengenai function pada JavaScript, kita telah mempelajari banyak hal tentang bagaimana menggunakan function di dalam pemrograman JavaScript. Saat ini kita akan mempelajari mengenai Scope. Pembahasan mengenai scope seringkali sangat rumit dan membingungkan. Saya akan mencoba untuk membahasnya semudah mungkin untuk dapat dimengerti oleh kita semua.

Scope dalam bahasa Indonesia dapat diartikan sebagai cakupan atau jangkauan. Dalam JavaScript, scope adalah topik yang sangat penting, karena hal ini menentukan bagaimana sebuah variable atau function dapat diakses. Pada post saat ini, saya akan coba membahas dua jenis scope, yaitu Global Scope dan Functional (Local) Scope.

* * *

## Global Scope

Sesuai dengan namanya, yaitu global yang berarti variable atau function yang dideklarasikan di dalam global scope akan dapat diakses oleh seluruh kode yang Anda buat, baik di luar maupun di dalam function. Berikut adalah contoh sederhana dari global scope.

```javascript
var iniVarGlobal = "saya";

alert(iniVarGlobal);
```

Variable iniVarGlobal dapat diakses oleh setiap kode yang ada, baik di luar, maupun di dalam function, bahkan dapat diakses pula oleh library JavaScript yang kita gunakan di dalam suatu halaman web. Pemakaian global scope sangat beresiko, karena jika salah satu dari variable yang kita buat ternyata juga dipakai oleh bagian kode yang lain, maka salah satu atau kedua variable tersebut tidak dapat diakses sesuai dengan yang seharusnya.

* * *

## Functional Scope (Local Scope)

Berkebalikan dengan global scope, functional/local scope adalah variable atau function yang dideklarasikan di dalam function dan hanya dapat diakses oleh kode di dalam function tersebut, termasuk function yang dideklarasikan di dalamnya. Mari kita simak contoh ini.

```javascript
var localScope = function () {
  var localVar = "Hello, World!";
  alert(localVar);
};

localScope();
alert(localVar);
```

Hasil dari fungsi alert akan muncul satu kali, karena alert di luar function tidak dapat membaca localVariable yang posisinya di dalam function localScope. Namun sebaliknya, jika kita ingin mengakses variable di luar function, itu dapat dengan mudah kita lakukan. Berikut contoh sederhana, pengembangan dari contoh sebelumnya.

```javascript
var globalVar = "Saya adalah variable global"

var localFunction = function () {
  alert(globalVar);
  globalVar = "Ganti variable global melalui fungsi lokal";
  alert(globalVar);
};

localFunction();
alert(globalVar);
```

Jika anda mencoba menjalankan contoh di atas, maka akan muncul tiga alert box. Yang pertama adalah kalimat yang kita deklarasikan pada variable global. Yang kedua dan ketiga adalah kalimat yang kita set pada variable global. Ini membuktikan bahwa kita dapat mengakses variable di luar function, tidak hanya membaca, tapi juga memberikan value terhadap variable tersebut. Ini menjadi sebuah masalah, jika kita membuat seluruh variable pada Global Scope. Kita harus membuat setiap variable unik agar tidak terjadi bentrokan nama antar variable.

Sekian tutorial yang sangat singkat mengenai Scope dalam JavaScript. Banyak yang bisa kita gali dari bahasan ini. Saya akan mencoba memperkenalkan sedikit demi sedikit mengenai konsep Scope pada tutorial-tutorial selanjutnya, dan akan saya sesuaikan dengan konteks tutorialnya. Selanjutnya kita akan mempelajari mengenai tipe data "_String_" secara mendetail.

Jangan lupa subscribe [RSS](http://feeds.feedburner.com/TitoPanduPersonalBlog "Subscribe to RSS") atau [email](http://eepurl.com/lFtwn "Subscribe by Email"), agar Anda dapat mengikuti tutorial selanjutnya. Silahkan tinggalkan komentar Anda, kritik dan saran sangat saya harapkan.

Sumber: [Tuts+ Premium Course: JavaScript Fundamentals 101](http://tutsplus.com/course/javascript-fundamentals/ "Tuts+ Premium Course: JavaScript Fundamentals 101") oleh Jeremy McPeak
