---
layout: post
title: Belajar dari Bahasa Pemrograman Functional
description: Perjalanan saya mempelajari beberapa bahasa pemrograman Functional
date: 2022-03-06 20:30:33.222222222 +07:00
type: post
published: true
status: publish
permalink: /2022-03-06-belajar-dari-bahasa-pemrograman-functional/
categories: 
- Computer
tags:
- programming
- software engineering
- clean code
- functional programming
comments: true
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---

Dahulu di KMK (sekarang Vidio.com), bahasa pemrograman yang tergolong functional, tidak termasuk dalam bahasa pemrograman yang banyak kita gunakan di production environment. Karena kita adalah tim yang pragmatis, maka kita tidak akan menggunakan suatu teknologi hanya karena sedang "hype". Akan tetapi mempertimbangkan banyak hal seperti support, stabilitas API, supporting library dan sebagainya.

## Mengapa belajar bahasa pemrograman Functional?

Sebagai software engineer pada umumnya, rasa penasaran itu kadang tidak terbendung. Iseng-iseng saya mulai belajar bahasa pemrograman functional di waktu senggang. Dimulai dari Elixir, Elm, Haskell, bahkan Arrow (Functional Type library dari Kotlin).

Dalam bahasa yang memang di desain untuk memprogram dengan paradigma functional, terdapat beberapa mindset yang kurang ditekankan dalam bahasa yang memiliki paradigma OOP. Beberapa diantaranya akan saya bahas dalam tulisan ini.

## Apa saja yang saya pelajari dari bahasa-bahasa tersebut?

Dari hasil "jalan-jalan" saya di alam functional programming, saya menemukan beberapa "pengetahuan" yang bisa kita aplikasikan dalam bahasa lain dan menurut saya dapat membantu kita untuk menulis code yang lebih jelas dan bersih (clean code).

![Data Information Knowledge Insight Wisdom]({{ site.baseurl }}/assets/data_information_knowledge_insight_wisdom-1.jpg "Data Information Knowledge Insight Wisdom")

Cartoon by [David Somerville](http://random-blather.com/2014/04/28/information-isnt-power/), based on a two pane version by Hugh McLeod.

## Knowledge

### Programming merupakan Data Transformation

Dalam buku [Programming Elixir](https://learning.oreilly.com/library/view/programming-elixir/9781680506129/f_0007.xhtml#d25e218), Dave Thomas mengatakan bahwa dia menemukan kembali kesenangan dalam memprogram, yaitu dengan cara mentransform data.

> Elixir lets us solve the problem in the same way the Unix shell does. Rather than have command-line utilities, we have functions. And we can string them together as we please. The smaller—more focused—those functions, the more flexibility we have when combining them.

Menurut dia, setiap code yang kita tulis adalah sebuah cara bagi kita untuk melakukan transformasi data. Sebagai contoh, dalam sebuah web server, kita mentransform request berupa `GET /users/1` menjadi sebuah response JSON. Atau `POST /users` menjadi cara untuk kita melakukan save user ke database dan mengembalikan response `200 OK` atau `422 Unprocessable Entity` jika data user tidak valid.

### Pisahkan IO (Input Output) dengan Logic

Saat saya belajar Elm, dalam Elm Architecture, bahasa ini mengajarkan kita untuk memisahkan antara IO dengan Logic. Dalam Elm, hal ini biasa disebut dengan Commands and Subscriptions. Pada bagian inilah kita menaruh Commands seperti XHR, generate random number, dsb. Jika kita bicara server side, maka Commands adalah query dan save data ke database, redis ataupun server lainnya.

Untuk subscriptions, kita dapat menaruh subscription terhadap waktu, seperti yang saya lakukan pada aplikasi waktu sholat saya https://github.com/titopandub/time-keeper dan melakukan perhitungan terhadap input tersebut.

### Optimalkan Penggunaan Data Type

Ini berlaku dalam bahasa pemrograman Functional Typed, seperti Elm, Haskell, OCaml, dsb. Sebagai contoh yang sederhana, dalam Elm, return type untuk XHR adalah Result error value yang mempunyai dua kemungkinan, yaitu Ok value dan Err error. Hal ini membuat programmer akan menjaga client dari XHR tersebut untuk selalu memiliki handle jika berhasil dan jika gagal.

Kita mungkin berargumen, jika harusnya setiap programmer melakukan itu dalam test-nya, namun seringkali hal ini dilupakan dan pada akhirnya ada error yang terekspos ke user. Menurut saya, data type hanya untuk memastikan kita meng-cover branch yang ada, sedangkan test adalah untuk memastikan code yang meng-cover branch tersebut benar dan sesuai spesifikasi.

## Wisdom

Saya sudah membaca Clean Code dan Clean Coder sekitar tahun 2014. Saya juga sudah menonton berkali-kali presentasi dari Uncle Bob tentang Clean Architecture. Saya juga pernah mencoba mengaplikasikannya, namun belum berhasil dan belum mengerti, sebenarnya bagaimana membangun software dengan arsitektur yang baik.

Sampai suatu saat, saya 1 on 1 dengan Mohan (CTO KMKLabs waktu itu) dan bertanya, "Bagaimana caranya saya bisa mengaplikasikan Clean Architecture, bagaimana saya bisa tahu kalau suatu code itu sudah clean, saya sudah baca buku ini itu, nonton conference ini itu, sudah juga coba melakukannya, namun belum juga berhasil". Beliau menjawab, "Kamu akan dapat itu dari pengalaman, berapa lama kamu ada di dunia pemrograman? Mungkin pengalaman kamu belum cukup banyak untuk melihat berbagai software".

Dan hal tersebut akhirnya saya temukan juga, saat saya membuat aplikasi dalam Elm di sela-sela weekend. Akhirnya saya menemukan bahwa maksud dari Clean Architecture adalah memisahkan IO dan Logic, serta fokus terhadap data transformasi pada layer Entities dan Use Cases. Akhirnya kami bisa membangun product BBM Timeline dengan Clean Architecture.

![Diagram Clean Architecture]({{ site.baseurl }}/assets/CleanArchitecture.jpg "Diagram Clean Architecture")
Diagram Clean Architecture dari [The Clean Code Blog](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

Meskipun kami menggunakan Kotlin, yang bukan purely functional. Kami tetap bisa menggunakan kaidah-kaidah yang saya sebutkan sebelumnya. Kaidah-kaidah itu sebenarnya tidak eksklusif ada pada bahasa pemrograman Functional, namun seringkali tertutup dengan framework atau library yang kita gunakan. Kita jadi lupa untuk membangun code yang bersih, malah hanya sekedar menempelkan library atau menggunakan framework, dan sedihnya terkunci dengan mindset yang dibawa oleh library ataupun framework tersebut.

Sebagai contoh sederhana, di Rails, kita disarankan untuk menulis logic di model. Meskipun ini tidak sepenuhnya ideal, tapi usahakanlah untuk menulis seluruh query di model dan hanya ekspos method untuk memanggil query-query tersebut, daripada melakukannya di luar model. Ini akan mempermudah kita dalam me-refactor dan merubah query saat diperlukan.

Daripada melakukan seperti ini.

```ruby
class Api::AuthorsController < ApplicationController
  def index
    @authors = Author.where("tracks_count > 0").order(updated_at: :desc).page(params[:page])
  end
end
```

Sebaiknya seperti ini.

```ruby
class Api::AuthorsController < ApplicationController
  def index
    @authors = Author.sorted_by_newest(page: params[:page])
  end
end

class Author < ApplicationRecord
  def self.sorted_by_newest(page: 1)
    where("tracks_count > 0").order(updated_at: :desc).page(page)
  end
end
```

Setelah kita dapat mendorong semua logic IO ke masing-masing kelas yang memang bertugas memanggil eksternal, maka kita bisa mengoptimalkan bagian data transformation. Contohnya seperti apa yang saya tunjukan di blog post [sebelumnya](2022-03-03-refactor-if-dan-argumen-boolean.md).

```python
class Prediction():
    def __init__(self, user_id):
        self.user_id = user_id

    def results(self):
        seed = Seed.data(self.user_id)
        recommendations = Model.predict(seed)

        recommendations = self.filter(recommendations)

        if len(recommendations) <= 10:
            recommendations += self.fallback()

        return recommendations

    def filter(self, recommendations):
        return recommendations

    def fallback(self):
        return Fallback.result()

class PredictionSpecial(Prediction):
    def filter(self, recommendations):
        return Special.filter(recommendations)

    def fallback(self):
        return FallbackSpecial.result()

user_id = 1
print(Prediction(user_id).results())
print(PredictionSpecial(user_id).results())
```

Transformasi dari `Seed.data`, lalu `Model.predict`, lalu `filter`, lalu ditambahkan `fallback` merupaka data transformasi. Ini membuat kita lebih mudah dalam mengerjakan program, karena pada satu waktu kita hanya perlu fokus ke satu level abstraksi, dalam hal ini abstraksi transformasi recommendations. Hal ini sesuai dengan yang dikatakan Robert C. Martin di bukunya Clean Code, [Chapter 3 mengenai Functions](https://learning.oreilly.com/library/view/clean-code-a/9780136083238/chapter03.xhtml#ch3lev1sec3).

> Mixing levels of abstraction within a function is always confusing. Readers may not be able to tell whether a particular expression is an essential concept or a detail. Worse, like broken windows, once details are mixed with essential concepts, more and more details tend to accrete within the function.

Mengenai data type, saya berusaha menggunakan satu data type untuk transformasi. Dalam bahasa pemrograman Functional yang menggunakan Type, seperti Elm, kita dapat menggunakan `Maybe`. Namun dalam bahasa pemrograman yang tidak memiliki Type seperti itu, kita perlu "mengakali"-nya. Misalnya dengan menggunakan exception atau memberikan nilai kosong (jika hal tersebut masuk akal).

Menurut saya hal-hal inilah yang penting untuk kita aplikasikan di bahasa pemrograman lain yang saya pelajari dari bahasa pemrograman Functional. Saya menjadi mengerti bagaimana arsitektur dasar yang baik dan bersih. Memang jika kita ingin benar-benar bersih, kita harus terlepas dari framework, namun tidak semua software harus mencapai level tersebut. Bersikap pragmatis sangat penting, jika tidak, kita akan menghabiskan banyak waktu untuk membangun semuanya dari nol. Menggunakan framework tidak masalah, tapi kita sendirilah yang menentukan struktur dari software yang kita bangun supaya bersih dan mudah dirubah dikemudian hari.

## Sekarang

Meskipun kami (Vidio.com) memiliki budaya yang pragmatis, perkembangan bahasa pemrograman Functional tidak dapat dipungkiri lagi. Saat ini kita telah mengadopsi beberapa bahasa pemrograman Functional seperti Scala, Swift dan Kotlin. Sehingga paradigma-paradigma yang saya sebutkan sebelumnya sudah kami implementasikan di production environment. Pada bahasa pemrograman yang bukan tergolong Functional sekali pun, prinsip-prinsip tersebut di atas juga mulai diadopsi.

## Rekomendasi Buku

Beberapa rekomendasi buku yang teman-teman bisa baca mengenai hal-hal ini.

1. [Clean Code: A Handbook of Agile Software Craftsmanship](https://learning.oreilly.com/library/view/clean-code-a/9780136083238/)
2. [Grokking Simplicity](https://grokkingsimplicity.com/)

Sekian dari saya, mudah-mudahan bermanfaat. Terima kasih.