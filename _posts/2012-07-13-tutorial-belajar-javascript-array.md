---
layout: post
title: Tutorial Belajar JavaScript - Array
date: 2012-07-13 08:39:05.000000000 +07:00
type: post
published: true
status: publish
permalink: /web-development/tutorial-belajar-javascript-array/
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
  _series_part: '8'
comments: true
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---
[![JavaScript JSconf logo]({{ site.baseurl }}/assets/JSconf_logo-150x150.png "JSconf_logo")]({{ site.baseurl }}/JSconf_logo.png)

Pada tutorial yang lalu dalam [Tutorial Belajar JavaScript - Object](http://tito.pandubrahmanto.com/web-development/tutorial-belajar-javascript-object/ "Tutorial Belajar JavaScript – Object"), kita telah mempelajari banyak hal tentang Object dan OOP dalam pemrograman JavaScript. Saat ini kita akan membahas mengenai Array.

Array merupakan kumpulan beberapa data dalam satu kesatuan data. Data-data di dalam Array disebut elemen. Kita dapat mengakses elemen di dalam Array melalui indeks dari setiap elemen dalam Array.

Dalam setiap bahasa pemrograman, tipe data Array akan selalu ada. Karena elemen inilah (disamping Object) yang dapat memudahkan kita dalam menyederhanakan dalam penyelesaian problem yang kompleks.  

* * *

## Mendeklarasikan Array dengan cara lama

Kita akan mempelajari bagaimana mendeklarasikan Array dalam dua cara. Yaitu cara lama dan cara baru yang jauh lebih mudah. Pendeklarasian Array dengan cara lama tidak jauh berbeda dengan cara mendeklarasikan Object. Berikut contohnya.

```javascript
var foo = new Array();
```

Kita dapat menambahkan elemen saat mendeklarasikan Array, kita hanya perlu memasukkan elemen ke dalam parameter `Array()` dipisahkan dengan tanda koma (,). Elemen tersebut tidak harus sama tipe datanya. Kita dapat memasukkan beberapa tipe data ke dalam Array. Berikut contohnya.

```javascript
var foo = new Array("Buku", 1, true);
```

Array memiliki properti `length`, mirip dengan String. `length` pada Array memberikan informasi banyaknya elemen yang terdapat di dalamnya. Berikut contoh penggunaan `length`.

```javascript
var foo = new Array("Buku", 1, true);

var jumlah = foo.length;
alert(jumlah);
```

Kita dapat merubah atau menambahkan elemen ke dalam Array. Caranya sangat sederhana, yaitu dengan menambahkan kurung kotak ( [ ] ) dan mengisinya dengan indeks Array yang akan dirubah atau indeks Array terakhir ditambah satu (untuk menambah Array). Kita juga dapat mengakses elemen dengan cara yang sama. Berikut contoh untuk merubah atau menambah elemen ke dalam Array.

```javascript
var foo = new Array("Buku", 1, true);
var jumlah = foo.length;

// Akses elemen di dalam Array dan memasukkan ke dalam variable
var barang = foo[0];
alert(barang);

// Merubah elemen yang sudah ada di dalam Array
foo[0] = "Pulpen";
alert(foo[0]);

// Menambahkan elemen ke dalam Array
foo[3] = "Mouse";
alert(foo);
```

* * *

## Mendeklarasikan Array dengan cara baru

JavaScript menyediakan dua cara dalam mendeklarasikan Array. Berikut adalah cara untuk melakukannya dengan cara yang lebih mudah.

```javascript
var foo = ["Buku", 1, true];
```

* * *

## Metode pada Array

Array juga memiliki beberapa metode yang sangat berguna. Diantaranya adalah push, concat, join, reverse dan sort. Kita akan membahas keempat metode atau function tersebut.

### push

Metode ini berguna untuk menambahkan elemen baru ke dalam Array. Memang kita dapat dengan mudah menggunakan properti `length`, namun lebih mudah untuk menggunakan metode yang satu ini. Saya akan memberikan contoh menggunakan properti length dan akan kita bandingkan dengan metode push.

```javascript
var foo = ["Buku", 1, true];

foo[foo.length] = "Pulpen";

foo.push(18);
alert(foo);
```

Dapat terlihat jelas, menggunakan metode push membuat kode lebih singkat dan lebih mudah dibaca.

### concat

`concat` pada Array kurang lebih memiliki fungsi yang sama dengan concat pada String. Gunanya adalah untuk menggabungkan 2 Array atau lebih. Berikut contohnya.

```javascript
var foo = ["Buku", "Pensil", "Pulpen"];  
var foo2 = ["Penggaris", "Penghapus", "Kertas"];  
var foo3 = ["Stabilo", "Komik"];

var barang = foo.concat(foo2, foo3);

alert(barang);
```

Akan muncul gabungan dari tiga Array, yaitu foo, foo2, dan foo3.

### join

`join` akan menggabungkan elemen dalam Array menggunakan separator tertentu dan mengubahnya menjadi String. Kita perlu memberikan parameter separator kepada fungsi ini. Berikut contohnya menggunakan tiga Array sebelumnya.

```javascript
var foo = ["Buku", "Pensil", "Pulpen"];
var foo2 = ["Penggaris", "Penghapus", "Kertas"];
var foo3 = ["Stabilo", "Komik"];

var barang = foo.concat(foo2, foo3);

var gabung = barang.join(", ");

alert(gabung);
```

Pada contoh di atas akan muncul kedelapan elemen Array dan menjadi String dengan menggunakan separator koma dan spasi (, ).

### reverse

`reverse` akan membalik urutan Array, yang pertama menjadi yang terakhir dan yang terakhir menjadi yang pertama. Berikut contohnya.

```javascript
var foo = ["Buku", "Pensil", "Pulpen"];
var foo2 = ["Penggaris", "Penghapus", "Kertas"];
var foo3 = ["Stabilo", "Komik"];

var barang = foo.concat(foo2, foo3);

var terbalik = barang.reverse();

alert(terbalik);
```

### sort

Seperti namanya, `sort` akan mengurutkan elemen Array sesuai dengan abjad. Mari kita lihat contoh berikut ini.

```javascript
var foo = ["Buku", "Pensil", "Pulpen"];
var foo2 = ["Penggaris", "Penghapus", "Kertas"];
var foo3 = ["Stabilo", "Komik"];

var barang = foo.concat(foo2, foo3);

var urutAbjad = barang.sort();

alert(urutAbjad);
```

* * *

Sekian tutorial yang sangat singkat mengenai `Array` dalam JavaScript. Banyak yang bisa kita gali dari bahasan ini. Selanjutnya kita akan mempelajari mengenai _Control Flow_ dalam JavaScript secara detail. Control Flow yang dimaksud adalah statement If..Then..Else. Sampai bertemu ditutorial selanjutnya.

Jangan lupa subscribe [RSS](http://feeds.feedburner.com/TitoPanduPersonalBlog "Subscribe to RSS") atau [email](http://eepurl.com/lFtwn "Subscribe by Email"), agar Anda dapat mengikuti tutorial selanjutnya. Silahkan tinggalkan komentar Anda, kritik dan saran sangat saya harapkan.

Sumber: [Tuts+ Premium Course: JavaScript Fundamentals 101](http://tutsplus.com/course/javascript-fundamentals/ "Tuts+ Premium Course: JavaScript Fundamentals 101") oleh Jeremy McPeak
