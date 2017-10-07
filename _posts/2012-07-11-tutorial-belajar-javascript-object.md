---
layout: post
title: Tutorial Belajar JavaScript - Object
date: 2012-07-11 17:55:19.000000000 +07:00
type: post
published: true
status: publish
permalink: /web-development/tutorial-belajar-javascript-object/
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
  _series_part: '7'
comments: true
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---
[![JavaScript JSconf logo]({{ site.baseurl }}/assets/JSconf_logo-150x150.png "JSconf_logo")]({{ site.baseurl }}/assets/JSconf_logo.png)

Pada tutorial yang lalu dalam [Tutorial Belajar JavaScript - String]({{ site.baseurl }}/web-development/tutorial-belajar-javascript-string/ "Tutorial Belajar JavaScript – String"), kita telah mempelajari banyak hal tentang String dalam pemrograman JavaScript. Saat ini kita akan membahas mengenai Object.

JavaScript merupakan pemrograman yang menggunakan konsep OOP atau [Object-oriented Programming](http://en.wikipedia.org/wiki/Object-oriented_programming "Object-oriented_programming"), namun JavaScript tidak memaksa Anda untuk menggunakan OOP setiap saat. Anda bisa saja membuat program dalam JavaScript tanpa berorientasi Object, tapi saat program kita semakin kompleks maka pemrograman berorientasi Object akan sangat dibutuhkan. Mari kita pelajari konsep Object pada kesempatan kali ini.

* * *

Sebenarnya setiap tipe data dalam JavaScript merupakan `Object`. Kita sudah mempelajari dalam tutorial sebelumnya mengenai object `String`. Selain `String`, tipe data seperti `Number`, `Array`, dan juga `Boolean` merupakan `Object`. Semuanya merupakan turunan dari tipe data `Object`, hal ini disebut **"Inheritance"** dalam konsep OOP. Kita tidak akan membahas hal ini secara mendalam pada tutorial kali ini. Kita akan fokus pada pendeklarasian dan penggunaan `Object`.

Cara mendeklarasikan `Object` dalam JavaScript sangat mudah dan mirip dengan bahasa pemrograman lainnya. Berikut contoh sederhananya.

```javascript
var karyawan = new Object;  
```

Sangat simpel? Jika kita ingin memberikan properti atau metode, kita hanya perlu memanggil variable karyawan dan menambahkan . (titik) dan nama properti atau metode. Berikut contoh secara lengkap lanjutan dari kode sebelumnya.

```javascript
var karyawan = new Object;

karyawan.namaDepan = "Tito";
karyawan.namaBelakang = "Brahmanto";

karyawan.tampilkanNamaLengkap = function () {
  return this.namaDepan + " " + this.namaBelakang;
};

alert(karyawan.tampilkanNamaLengkap());
```

Sangat mudah bukan untuk mendeklarasikan Object dalam JavaScript. Tapi tunggu dulu, contoh-contoh sebelumnya adalah cara lama dalam mendeklarasikan Object. Cara barunya jauh lebih sederhana. Cara ini disebut "**Object Literal Notation**".

Object Literal Notation sangat sederhana dan tidak membutuhkan banyak sintaks. Hanya diperlukan tanda buka dan tutup kurung kurawal ( { } ). Berikut contoh Object Literal Notation.

```javascript
var karyawan = {
  namaDepan: "Tito",
  namaBelakang: "Brahmanto",
  tampilkanNamaLengkap: function () {
    return this.namaDepan + " " + this.namaBelakang;
  }
};

alert(karyawan.tampilkanNamaLengkap());
```

Dengan kode yang jauh lebih sederhana, kita sudah bisa membuat `Object`. Perbedaan yang sangat mendasar dan jangan sampai dilupakan adalah antara properti dan metode selalu dipisahkan oleh tanda , (koma) dan bukan ; (titik koma). Jika hal ini dilupakan maka akan menimbulkan error. Ingat error dalam JavaScript tidak ada pesan errornya dan sangat menyesatkan.

* * *

Sekian tutorial yang sangat singkat mengenai `Object` dalam JavaScript. Banyak yang bisa kita gali dari bahasan ini. Kita dapat memulai untuk memakai Object dalam pemrograman JavaScript. Selanjutnya kita akan mempelajari mengenai tipe data "_Array_" secara mendetail.

Jangan lupa subscribe [RSS](http://feeds.feedburner.com/TitoPanduPersonalBlog "Subscribe to RSS") atau [email](http://eepurl.com/lFtwn "Subscribe by Email"), agar Anda dapat mengikuti tutorial selanjutnya. Silahkan tinggalkan komentar Anda, kritik dan saran sangat saya harapkan.

Sumber: [Tuts+ Premium Course: JavaScript Fundamentals 101](http://tutsplus.com/course/javascript-fundamentals/ "Tuts+ Premium Course: JavaScript Fundamentals 101") oleh Jeremy McPeak
