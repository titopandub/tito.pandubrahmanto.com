---
layout: post
title: Tutorial Belajar JavaScript - Control Flow
date: 2012-10-12 10:00:00.000000000 +07:00
type: post
published: true
status: publish
permalink: /web-development/tutorial-belajar-javascript-control-flow/
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
  _series_part: '9'
  _spost_short_title: ''
comments: true
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---
[![JavaScript JSconf logo]({{ site.baseurl }}/assets/JSconf_logo-150x150.png "JSconf_logo")]({{ site.baseurl }}/assets/JSconf_logo.png)

Pada tutorial sebelumnya, yaitu [Tutorial Belajar JavaScript - Array](http://tito.pandubrahmanto.com/web-development/tutorial-belajar-javascript-array/ "Tutorial Belajar JavaScript – Array"), kita telah mempelajari banyak hal tentang Array dalam pemrograman JavaScript. Kita akan mempelajari Kondisi dan Control Flow pada kesempatan kali ini.

Dalam JavaScript terdapat beberapa cara untuk mengubah suatu alur program (controlling flow) jika suatu kondisi terjadi. Maka sebelum kita mempelajari mengenai pengambilan keputusan, kita akan pelajari dahulu mengenai kondisi yang ada pada JavaScript.  

* * *

Sebenarnya komputer disusun oleh kumpulan 0 dan 1 atau disebut binary. Komputer hanya mengenal ya atau tidak, komputer tidak mengenal ditengah-tengah atau kondisi "digantung". Maka dalam komputer dikenal istilah `true` atau `false`. Kedua istilah ini juga dikenal dalam JavaScript.

Sebelum kita merubah atau mengambil keputusan untuk suatu bagian program, biasanya syntax program tersebut akan mengambil kondisi `true` atau `false` dari suatu statement. Statement yang mengembalikan nilai `true` atau `false` sering disebut kondisi. Statement ini ada beberapa macam, kita akan bahas satu persatu.

* * *

## A. Operator Perbandingan (Comparison Operator)

Statement ini akan membandingkan nilai yang ada pada sebelah kiri operator pembanding dengan nilai yang ada disebelah kanannya. Ada beberapa operator pembanding, untuk mempermudah kita dalam mempelajarinya, maka saya akan mengulas operator-operator yang dibahas oleh Douglas Crockford dalam buku JavaScript: The Good Parts. Berikut beberapa operator pembanding:

### 1\. Operator Persamaan (`===`)

Operator ini akan membandingkan nilai dan type data. Operator ini akan mengembalikan `true` bila nilai dan type datanya sama. Berikut contohnya.

```javascript
5 + 6 === 11; // true
5 - 2 === 2; // false
5 + 6 === "11"; // false karena type datanya berbeda
```

### 2\. Operator Pertidaksamaan (`!==`)

Operator ini akan memiliki sifat yang sama dengan operator sebelumnya namun akan mengembalikan nilai yang sebaliknya. Operator ini akan mengembalikan nilai `true` bila nilai dan type tidak sama. Berikut contohnya.

```javascript
5 + 6 !== 11; // false
5 - 2 !== 2; // true
5 + 6 !== "11"; // true karena type datanya berbeda
```

### 3\. Operator Kurang Dari (`<`)

Operator ini akan mengembalikan nilai `true` bila nilai disebelah kiri operator lebih kecil daripada nilai disebelah kanan operator. Berikut contoh sederhana.

```javascript
3 < 5; // true
5 < 2; // false
```

### 4\. Operator Kurang Dari Sama Dengan (`<=`)

Operator ini akan mengembalikan nilai `true` bila nilai disebelah kiri operator lebih kecil atau sama dengan daripada nilai disebelah kanan operator. Berikut contoh sederhana.

```javascript
3 <= 5; // true
5 <= 5; // true
```

### 5\. Operator Lebih Dari (`>`)

Operator ini akan mengembalikan nilai `true` bila nilai disebelah kiri operator lebih besar daripada nilai disebelah kanan operator. Berikut contoh sederhana.

```javascript
7 > 5; // true
2 > 5; // false
```

### 6\. Operator Lebih Dari Sama Dengan (`>=`)

Operator ini akan mengembalikan nilai `true` bila nilai disebelah kiri operator lebih besar atau sama dengan daripada nilai disebelah kanan operator. Berikut contoh sederhana.

```javascript
7 >= 5; // true
5 >= 5; // true
```

* * *

## B. Logical Operator

Kita akan membahas dua logical operator dalam JavaScript. Kedua operator tersebut adalah operator and (`&&`) dan operator or (`||`).

### 1\. Operator and (`&&`)

Operator ini akan mengembalikan nilai `true` bila kondisi disebelah kiri dan kanan operator mengembalikan nilai `true`. Jika salah satunya mengembalikan nilai `false`, maka operator ini akan mengembalikan nilai `false`. Berikut contohnya

```javascript
var angka = 7;

angka >= 5 && angka < 10; // true
angka >= 5 && angka < 6; // false
```

### 2\. Operator or (`||`)

Operator ini akan mengembalikan nilai `false` bila kondisi disebelah kiri dan kanan operator mengembalikan nilai `false`. Jika salah satunya mengembalikan nilai `true`, maka operator ini akan mengembalikan nilai `true`. Berikut contohnya.

```javascript
var angka = 7;

angka >= 5 || angka < 6; // true
angka >= 8 || angka < 6; // false
```

* * *

## C. Control Flow

Setelah membahas mengenai operator perbandingan dan logika, kita akan mulai membahas mengenai pengambilan keputusan.

### 1\. Statement `if`

`if` akan mengeksekusi suatu kode jika kondisi dimasukkan ke dalamnya `true`. Berikut contohnya

```javascript
var angka = 7;

if (angka > 5) {
  alert("angka ini lebih besar dari 5");
}
```

Statement `if` juga dapat dibuat bersarang (if di dalam if). Berikut contohnya.

```javascript
var angka = 7;

if (angka > 5) {
  alert("angka ini lebih besar dari 5");
  if (angka <= 10) {
    alert("angka ini lebih besar atau sama dengan 10");
  }
}
```

### 2\. Statement `if .. else`

Jika kita ingin mengeksekusi suatu kode bila secara default bila tidak ada kondisi yang sesuai dengan statement `if` sebelumnya, maka kita dapat menggunakan statement if else. Berikut contohnya.

```javascript
var angka = 4;

if (angka > 5) {
  alert("angka ini lebih besar dari 5");
} else {
  alert("angka ini lebih kecil atau sama dengan 5");
}
```

### 3\. Statement `if .. else if .. else`

Kita bisa membuat program yang dapat mengevaluasi beberapa kondisi, untuk hal tersebut kita dapat memakai `if .. else if .. else`. Berikut contohnya.

```javascript
var bulan = 4;

if (bulan === 0) {
  alert("Ini bulan Januari");
} else if (bulan === 1) {
  alert("Ini bulan Februari");
} else if (bulan === 2) {
  alert("Ini bulan Maret");
} else if (bulan === 3) {
  alert("Ini bulan April");
} else {
  alert("Bulan belum diketahui sistem");
}
```

### 4\. Statement `switch`

Mirip dengan statement `if .. else if .. else`, statement switch juga berguna untuk mengevaluasi beberapa kondisi. Berikut contohnya.

```javascript
switch (expr) {
  case "Jeruk":
    console.log("Jeruk Rp10.000 per kg.");
    break;
  case "Apel":
    console.log("Apel Rp15.000 per kg.");
    break;
  case "Pisang":
    console.log("Pisang Rp8.000 per kg.");
    break;
  case "Mangga":
  case "Pepaya":
    console.log("Mangga dan pepaya Rp20.000 per kg.");
    break;
  default:
    console.log("Maaf, kami kehabisan " + expr + ".");
}
```

* * *

Sekian tutorial yang sangat singkat mengenai `Control Flow` dalam JavaScript. Banyak yang bisa kita gali dari bahasan ini. Selanjutnya kita akan mempelajari mengenai Loop dalam JavaScript secara detail .

Jangan lupa subscribe [RSS](http://feeds.feedburner.com/TitoPanduPersonalBlog "Subscribe to RSS") atau [email](http://eepurl.com/lFtwn "Subscribe by Email"), agar Anda dapat mengikuti tutorial selanjutnya. Silahkan tinggalkan komentar Anda, kritik dan saran sangat saya harapkan.

Sumber: [Tuts+ Premium Course: JavaScript Fundamentals 101](http://tutsplus.com/course/javascript-fundamentals/ "Tuts+ Premium Course: JavaScript Fundamentals 101") oleh Jeremy McPeak
