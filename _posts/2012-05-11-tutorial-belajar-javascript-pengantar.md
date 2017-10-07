---
layout: post
title: Tutorial Belajar JavaScript - Pengantar
date: 2012-05-11 16:00:26.000000000 +07:00
type: post
published: true
status: publish
permalink: /web-development/tutorial-belajar-javascript-pengantar/
categories:
- Web Development
tags:
- how to
- javascript
- learning
meta:
  _edit_last: '1'
  image: ''
  seo_follow: 'false'
  seo_noindex: 'false'
  _syntaxhighlighter_encoded: '1'
  dsq_thread_id: '685415468'
  _yoast_wpseo_linkdex: '70'
  _series_part: '1'
  _yoast_wpseo_focuskw: Belajar JavaScript
  _yoast_wpseo_title: Tutorial Belajar JavaScript - Pengantar - Blog of Tito Pandu
  _yoast_wpseo_metadesc: Pengantar untuk sebuah post berseri mengenai belajar JavaScript
    bagi para pemula. Disajikan dalam bahasa Indonesia.
comments: true
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---
[![JavaScript JSconf logo]({{ site.baseurl }}/assets/JSconf_logo-150x150.png "JSconf_logo")]({{ site.baseurl }}/JSconf_logo.png)

Anda mungkin sudah membaca post mengenai bagaimana untuk [mempelajari Bahasa Pemrograman Javascript]({{ site.baseurl }}/web-development/belajar-bahasa-pemrograman-javascript/ "Belajar Bahasa Pemrograman: Javascript"). Anda bisa mempelajarinya secara interaktif melalui [Codeacademy](http://www.codecademy.com/ "Learn to Code, Codeacademy") atau Eloquent JavaScript, seperti yang Anda baca pada post sebelumnya. Karena kedua sumber tersebut memakai Bahasa Inggris, saya rasa mungkin ada baiknya jika saya bisa memberikan tutorial mengenai belajar JavaScript dalam Bahasa Indonesia.  

Javascript termasuk bahasa pemrograman yang sangat populer dan sangat mudah digunakan. Anda hanya memerlukan **web browser terkini (Google Chrome, Safari, IE 9, Opera)** dan **text editor (Notepad++, TextMate)**. Namun jika Anda menginginkan editor untuk pemrograman JavaScript yang lebih advance dan tentunya mudah digunakan, saya menyarankan untuk menggunakan **Microsoft Web Matrix (untuk Windows) atau Aptana IDE (untuk Windows, Linux dan Mac OS X)**.

* * *

## Meletakkan JavaScript dalam file HTML

Anda akan membutuhkan HTML dalam penulisan kode Javascript pada halaman web. Berikut ini adalah HTML minimal yang Anda butuhkan untuk mengeksekusi kode JavaScript kita. File HTML akan selalu berekstensi .html, Anda dapat membuat file index.html seperti contoh di bawah ini.

```html
<!DOCTYPE html>

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title></title>
    <script>
    alert("Hello World!");
    </script>
  </head>
  <body>

  </body>
</html>
```

Ada cara lain yang lebih baik dalam meletakkan kode JavaScript, yaitu sebelum menutup body tag. Seperti ini.

```html
<!DOCTYPE html>

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title></title>
  </head>
  <body>

    <script>
    alert("Hello World!");
    </script>
  </body>
</html>
```

* * *

## Penulisan JavaScript

Kode JavaScript selalu menempel pada HTML dalam penggunaannya sebagai skrip pada web page. Untuk menggunakannya biasanya ditaruh dalam script tag. Ada dua cara penulisan JavaScript, pertama adalah menulisnya di dalam tag seperti contoh sebelumnya. Namun menulis seperti itu akan tercampur menjadi satu dengan tag HTML atau stylesheet lainnya, serta jika kode tersebut dibutuhkan di beberapa halaman web, maka akan menjadi pekerjaan yang berulang-ulang.

Cara kedua, yaitu dengan memasukkan JavaScript pada suatu file dengan ekstensi .js, contohnya pada skrip.js yang diisi dengan hanya kode JavaScript tanpa script tag dan menambahkan parameter src pada script tag. Jangan lupa untuk selalu menutup tagnya. Berikut ini contoh index.html.

```html
<!DOCTYPE html>

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title></title>
  </head>
  <body>

    <script src="skrip.js"></script>
  </body>
</html>
```

Dan ini contoh skrip.js.

```javascript
alert("Hello World!");
```

Dengan memakai cara kedua akan memudahkan kita dalam menulis dan melakukan perubahan pada kode JavaScript kita. Hal ini juga memudahkan jika Anda memiliki banyak script, seperti framework dan plugin-pluginnya. Jika kode JavaScript Anda banyak dan besar ukurannya juga dengan mudah dapat di-minify supaya lebih cepat proses loading halaman webnya.

* * *

Sekian perkenalan dari saya. Saya harap dengan membaca ini, Anda sudah bisa memulai untuk belajar JavaScript. Nantikan post saya selanjutnya mengenai variable pada JavaScript. Anda dapat subscribe ke [RSS](http://feeds.feedburner.com/TitoPanduPersonalBlog "RSS dari Tito Pandu Personal Blog") atau ke [email list](http://eepurl.com/lFtwn) untuk mendapatkan update tutorial selanjutnya. Jangan lupa tinggalkan komentar bila ada pertanyaan ataupun saran.

Sumber: [Tuts+ Premium Course: JavaScript Fundamentals 101](http://tutsplus.com/course/javascript-fundamentals/ "Tuts+ Premium Course: JavaScript Fundamentals 101") oleh Jeremy McPeak
