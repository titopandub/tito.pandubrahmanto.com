---
layout: post
title: Tutorial Belajar JavaScript - Operator
date: 2012-05-18 20:00:45.000000000 +07:00
type: post
published: true
status: publish
permalink: /web-development/tutorial-belajar-javascript-operator/
categories:
- Web Development
tags:
- how to
- javascript
- learning
meta:
  _edit_last: '1'
  _syntaxhighlighter_encoded: '1'
  seo_follow: 'false'
  image: ''
  seo_noindex: 'false'
  _yoast_wpseo_linkdex: '64'
  _series_part: '3'
  _yoast_wpseo_focuskw: tutorial belajar javascript operator
  _yoast_wpseo_title: Tutorial Belajar JavaScript - Operator - Blog of Tito Pandu
  _yoast_wpseo_metadesc: Pada tutorial kali ini, kita akan belajar JavaScript mengenai
    Operator. Kita akan membahas operator pada tipe data integer, float dan string
  dsq_thread_id: '5553485105'
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---
[![JavaScript JSconf logo]({{ site.baseurl }}/assets/JSconf_logo-150x150.png "JSconf_logo")]({{ site.baseurl }}/JSconf_logo.png)

Setelah mempelajari beberapa variable dasar dari JavaScript, saat ini kita akan belajar operator-operator apa saja yang bisa dipakai untuk variable dasar tersebut. Operator yang akan dibahas adalah operator untuk Integer, Float dan String. Jika Anda belum membaca tutorial sebelumnya, silahkan lihat di [Tutorial Belajar JavaScript - Variable dan Tipe Data](http://tito.pandubrahmanto.com/web-development/tutorial-belajar-javascript-variable-tipe-dat/ "Tutorial Belajar Javascript – Variable dan Tipe Data").

* * *

## Integer

Kita mulai dengan operator untuk Integer. Integer seperti yang sudah kita kenal, adalah objek bilangan bulat. Operator dasar untuk Integer adalah tanda tambah (+), kurang (-), kali (\*), bagi (/) dan modulus/sisa pembagian (%). Berikut adalah contoh penggunaannya dengan hasil operasi pada komentar.

```javascript
var jumlah = 5 + 2; // 7
var selisih = 5 - 2; // 3
var perkalian = 5 * 2; // 10
var pembagian = 6 / 2; // 3
var sisa = 5 % 2; // 1
```

Anda juga dapat melakukan beberapa operasi secara sekaligus, berikut contohnya.

```javascript
var foo = 5 + 2 - 6 + 3; // 4
```

Selain penjumlahan dan selisih, kita juga dapat melakukannya dengan operator yang lain, berikut contohnya.

```javascript
var bar = 5 * 2 + 6 / 3; // 12
```

JavaScript akan melakukan operasi dari kiri ke kanan, jika ada perkalian dan pembagian maka akan dilakukan terlebih dahulu sebelum operasi penjumlahan dan pengurangan. Jika Anda menginginkan suatu operasi dilakukan terlebih dahulu, maka dapat ditambahkan tanda kurung ( ), berikut contohnya.

```javascript
var bar = 5 * ( 2 + 6 ) / 2; // 20
```

* * *

## Float

Pada dasarnya operator pada Integer dan Float adalah sama, karena keduanya merupakan jenis objek bilangan (Number). Namun yang perlu diperhatikan, jika Anda menggunakan Float bersamaan dengan Integer pada satu operasi, maka bilangan Integer tersebut akan secara otomatis dikonversi menjadi Float. Berikut contohnya.

```javascript
var pecahan = 7.5 + 5; // 12.5
```

Namun uniknya, jika hasil dari operasi tersebut adalah bilangan bulat, maka operasi tersebut secara otomatis mengkonversinya menjadi bilangan bulat. Berikut contohnya.

```javascript
var sama = 7.5 + 2.5; // 10
```

* * *

## String

Selanjutnya operasi untuk objek String. String memiliki beberapa operator, yaitu concatenation (penggabungan) dan operator konversi. Kita mulai dengan String concatenation.

### Concatenation (Penggabungan)

Salah satu operator yang pasti sering Anda pakai adalah String concatenation, yang berguna untuk menggabungkan dua String objek. Berikut beberapa contoh pemakaian String concatenation.

```javascript
var hello = "hello";
var world = "world";
var helloWorld = hello + world; // memakai tanda tambah (+)
var helloWorld2 = hello.concat(world); // memakai fungsi concat
```

Kedua bentuk operator concatenation adalah sama, namun operator tanda tambah sangat praktis digunakan.

Hati-hati dalam menggunakan operator concatenation pada String dan penjumlahan pada Integer. Berikut adalah contohnya.

```javascript
var foo = 5 + 4 + "7";

alert(foo);
```

Jika Anda mencoba kode diatas maka hasilnya adalah “97”. JavaScript akan mengambil hasil dari Integer (dalam hal ini 5 + 4 = 9) dan karena melihat objek selanjutnya adalah String, maka hasil tersebut akan dirubah menjadi String dan dilakukan operasi concatenation (menjadi “97”). Seringkali kita melupakan hal ini dan membuat hasil dari operasi tidak sesuai dengan yang kita inginkan.

### Konversi

Selanjutnya adalah operator konversi. Operator konversi untuk String objek salah satunya adalah parseInt. Operator ini akan mengubah String objek ke nilai Integer. Berikut contohnya.

```javascript
var foo = parseInt("77", 10); // 77
```

Fungsi parseInt membutuhkan dua argumen, yaitu objek String yang akan dikonversi dan basis bilangan (radix) dalam hal ini desimal adalah basis 10\. Anda juga dapat mengkonversikan ke biner, oktal atau heksadesimal dengan hanya menentukan basis bilangan 2, 8 atau 16\. Jika fungsi parseInt menemukan String objek bukan bilangan di dalamnya, maka fungsi ini akan berhenti. Berikut ini contohnya.

```javascript
var foo = parseInt("77s88", 10); // 77
```

Jika tidak ada bilangan sama sekali di dalam objek tersebut, atau karakter pertama adalah bukan bilangan, maka fungsi ini akan mengembalikan nilai NaN (Not a Number).

Selanjutnya kita akan membahas operator atau fungsi pada objek String yang kedua, yaitu parseFloat. Fungsi ini hampir sama dengan parseInt, namun akan mengembalikan nilai pecahan desimal (Float). Berikut contohnya.

```javascript
var pi = parseFloat("3.14", 10); // 3.14
```

* * *

Kita sudahi dahulu tutorial singkat mengenai operator untuk variable dasar pada JavaScript. Kita sudah mempelajari operator-operator yang terdapat pada operasi bilangan dan pada String. Di tutorial selanjutnya kita akan mempelajari mengenai “Function” pada JavaScript.

Function memiliki kekuatan yang sangat besar pada JavaScript. Namun kita akan mempelajari dasar-dasar penggunannya dahulu, supaya lebih mudah dalam mempelajarinya dan hanya membutuhkan waktu yang singkat.

Jangan lupa subscribe [RSS](http://feeds.feedburner.com/TitoPanduPersonalBlog "Subscribe to RSS") atau [email](http://eepurl.com/lFtwn "Subscribe by Email"), agar Anda dapat mengikuti tutorial selanjutnya. Silahkan tinggalkan komentar Anda, kritik dan saran sangat saya harapkan.

Sumber: [Tuts+ Premium Course: JavaScript Fundamentals 101](http://tutsplus.com/course/javascript-fundamentals/ "Tuts+ Premium Course: JavaScript Fundamentals 101") oleh Jeremy McPeak
