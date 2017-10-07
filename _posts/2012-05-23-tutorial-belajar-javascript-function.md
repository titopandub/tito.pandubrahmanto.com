---
layout: post
title: Tutorial Belajar JavaScript - Function
date: 2012-05-23 10:00:32.000000000 +07:00
type: post
published: true
status: publish
permalink: /web-development/tutorial-belajar-javascript-function/
categories:
- Web Development
tags:
- how to
- Internet
- javascript
meta:
  _edit_last: '1'
  _syntaxhighlighter_encoded: '1'
  image: ''
  seo_follow: 'false'
  seo_noindex: 'false'
  _yoast_wpseo_linkdex: '64'
  _series_part: '4'
  _yoast_wpseo_focuskw: tutorial belajar javascript function
  _yoast_wpseo_title: Tutorial Belajar JavaScript - Function - Blog of Tito Pandu
  _yoast_wpseo_metadesc: Pada tutorial kali ini, kita akan belajar JavaScript mengenai
    Function. Kita akan mempelajari beragam cara menggunakan JavaScript function.
  dsq_thread_id: '5553490207'
comments: true
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---
[![JavaScript JSconf logo]({{ site.baseurl }}/assets/JSconf_logo-150x150.png "JSconf_logo")]({{ site.baseurl }}/assets/JSconf_logo.png)

Kita telah mempelajari beberapa [operator untuk variable-variable dasar pada JavaScript]({{ site.baseurl }}/web-development/tutorial-belajar-javascript-operator/ "Tutorial Belajar JavaScript – Operator"). Saat ini kita akan mempelajari fitur terhebat pada JavaScript, yaitu function.

Pada tutorial sebelumnya, sebenarnya kita telah memakai beberapa function, seperti alert, parseInt dan parseFloat. Function pada JavaScript merupakan kumpulan beberapa instruksi dan atau function yang dapat dipanggil. Hal ini dapat mempermudah kita dalam memanage program dalam JavaScript. Untuk saat ini kita akan mempelajari bagaimana mendeklarasikan dan menggunakan function untuk mempersingkat beberapa instruksi yang berulang.

* * *

## Menggunakan Function

Sebagai contoh yang sederhana, mari kita simak baris program berikut ini.

```javascript
var foo = 3 + 3; // 6
foo = foo * 7; // 42
foo = foo - 5; // 37

var bar = 5 + 3; // 8
bar = bar * 7; // 56
bar = bar - 5; // 51

alert(foo);
alert(bar);
```

Dari contoh baris program sebelumnya kita melihat ada perulangan instruksi. Jika kita membuat sebuah program yang cukup besar, dimana beberapa baris instruksi akan diulang berkali-kali (bahkan bisa sampai ribuan kali), akan sangat tidak efisien jika kita harus melakukannya. Tidak hanya membuat lelah untuk mengetik instruksi yang sama ratusan bahkan ribuan kali (puluhan saja sudah capek), program yang kita buat akan lebih rentan terhadap error. Maka itulah dibuat function. Sehingga kita dapat membuat program lebih singkat dan lebih mudah untuk diperiksa. Dalam bahasa pemrograman aktifitas untuk membuat program lebih singkat dan lebih maintainable disebut "_Refactor_".

Kita akan mencoba untuk membuat baris program di atas menjadi sebuah function dan memanggilnya.

```javascript
function lakukanSesuatu(paramSatu) {
  paramSatu = paramSatu + 3;
  paramSatu = paramSatu * 7;
  paramSatu = paramSatu - 5;
  return paramSatu;
}

var foo = lakukanSesuatu(3);
var bar = lakukanSesuatu(5);

alert(foo);
alert(bar);
```

Hasil dari operasi tersebut akan sama dengan sebelumnya, namun kita dapat mengeksekusi function beberapa kali tanpa harus menuliskan satu-persatu operasi yang ada di dalamnya.

Kita juga dapat menggunakan lebih dari satu parameter pada function. Kita hanya perlu memisahkan antar parameter menggunakan koma (,). Berikut contohnya.

```javascript
function lakukanSesuatu(paramSatu, paramDua) {
  paramSatu = paramSatu + 3;
  paramSatu = paramSatu * 7;
  paramSatu = paramSatu - 5;
  return paramSatu + paramDua;
}

var foo = lakukanSesuatu(3, 5); // 42
var bar = lakukanSesuatu(5, 7); // 58
alert(foo);
alert(bar);
```

* * *

## Beberapa cara penggunaan function

Sebenarnya ada beberapa cara untuk mendeklarasikan dan menggunakan function selain yang sudah diberikan sebelumnya. Jika Anda sering mendengar istilah "_anonymous function_", maka berikut ini adalah contohnya.

```javascript
function(paramSatu, paramDua) {
  paramSatu = paramSatu + 3;
  paramSatu = paramSatu * 7;
  paramSatu = paramSatu - 5;
  return paramSatu + paramDua;
}
```

Biasanya anonymous function digunakan sebagai parameter untuk function lainnya. Saya akan coba mengulas anonymous function pada seri-seri berikutnya. Karena penggunaannya yang cukup kompleks, memerlukan satu ulasan tersendiri.

Function juga dapat diassign ke dalam variable. JavaScript memiliki kemampuan untuk menaruh function di dalam variable. Kemampuan itulah yang membuat JavaScript menjadi salah satu programming language yang powerful. Berikut contoh function yang sama seperti sebelumnya, namun ditaruh di dalam sebuah variable.

```javascript
var lakukanSesuatu = function(paramSatu, paramDua) {
  paramSatu = paramSatu + 3;
  paramSatu = paramSatu * 7;
  paramSatu = paramSatu - 5;
  return paramSatu + paramDua;
};

var foo = lakukanSesuatu(3, 2);

alert(foo); // 39
```

Ini adalah bentuk penggunaan function yang sangat disarankan. Kita dapat memanggil function dengan memanggil variable. Hal ini akan mempermudah kita dalam membaca kode yang dibuat serta beberapa keuntungan lainnya. Namun perlu diingat, tidak seperti bentuk sebelumnya, bentuk ini mengharuskan Anda untuk menulis function sebelum function tersebut dipanggil/digunakan.

* * *

## Menggunakan function sebagai parameter di dalam function

Fitur ini adalah fitur yang sangat menarik juga sangat berguna di dalam JavaScript. Kita dapat menggunakan function sebagai parameter di dalam function yang kita buat. Daripada saya hanya menulis penjelasan beberapa paragraf, lebih baik kita langsung melihat contohnya.

```javascript
var lakukanSesuatu = function(paramSatu, paramDua, fn) {
  paramSatu = paramSatu + 3;
  paramSatu = paramSatu * 7;
  paramSatu = paramSatu - 5;
  return fn(paramSatu, paramDua);
};

var jumlah = function(paramSatu, paramDua) {
  return paramSatu + paramDua;
};

var perkalian = function(paramSatu, paramDua) {
  return paramSatu * paramDua;
};

var foo = lakukanSesuatu(3, 2, jumlah);
var bar = lakukanSesuatu(4, 2, perkalian);

alert(foo); // 39
alert(bar); // 88
```

Sebenarnya kita dapat menggunakan anonymous function. Berikut contohnya, bila menggunakan anonymous function.

```javascript
var lakukanSesuatu = function(paramSatu, paramDua, fn) {
  paramSatu = paramSatu + 3;
  paramSatu = paramSatu * 7;
  paramSatu = paramSatu - 5;
  return fn(paramSatu, paramDua);
};

var jumlah = function(paramSatu, paramDua) {
  return paramSatu + paramDua;
};

var foo = lakukanSesuatu(3, 2, jumlah);
var bar = lakukanSesuatu(4, 2, function(paramSatu, paramDua) {
  return paramSatu * paramDua;
});

alert(foo); // 39
alert(bar); // 88
```

Banyak hal yang dapat dilakukan dengan memasukkan function ke dalam variable. Salah satunya dalam membuat "event" yang nanti akan dibahas pada tutorial mendatang.

* * *

Sekian tutorial mengenai function pada JavaScript. Sebenarnya JavaScript memiliki fitur-fitur yang sangat banyak di dalam function. Namun kita akan mempelajarinya pada lain waktu, sehingga dapat lebih mudah dimengerti dan lebih singkat waktu yang diperlukan untuk mempelajarinya. Serta tidak membuat bosan dalam mempelajarinya.

Pada tutorial saat ini kita baru mempelajari bagaimana cara penggunaan function, anonymous function dan melakukan assignment function terhadap variable. Selanjutnya, kita akan mempelajari mengenai "_Scope_" dalam JavaScript.

Jangan lupa subscribe [RSS](http://feeds.feedburner.com/TitoPanduPersonalBlog "Subscribe to RSS") atau [email](http://eepurl.com/lFtwn "Subscribe by Email"), agar Anda dapat mengikuti tutorial selanjutnya. Silahkan tinggalkan komentar Anda, kritik dan saran sangat saya harapkan.

Sumber: [Tuts+ Premium Course: JavaScript Fundamentals 101](http://tutsplus.com/course/javascript-fundamentals/ "Tuts+ Premium Course: JavaScript Fundamentals 101") oleh Jeremy McPeak
