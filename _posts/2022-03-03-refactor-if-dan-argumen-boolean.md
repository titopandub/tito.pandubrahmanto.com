---
layout: post
title: Refactor `if` dan Argumen Boolean
description: Refactor `if` dan Argumen Boolean dalam bahasa pemrograman Python
date: 2022-03-03 15:00:33.222222222 +07:00
type: post
published: true
status: publish
permalink: /2022-03-03-refactor-if-dan-argumen-boolean/
categories: 
- Refactoring
tags:
- python
- refactoring
- flag argument
- boolean argument
comments: true
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---

Di dalam pemrograman, hal yang sangat penting adalah bagaimana membuat komputer *bereaksi* terhadap kondisi. Salah satu cara yang sering dilakukan adalah dengan membuat conditional `if`. Penggunaan keyword `if` berbeda-beda tergantung bahasa pemrograman yang digunakan. Biasanya syntaxnya adalah `if kondisi then kondisi_benar else kondisi salah`.

Meskipun sangat diperlukan dan bermanfaat, penggunaan `if` yang ada di banyak tempat membuat kode yang kita buat agak sulit dipahami. Apalagi jika kondisi yang akan diperiksa merupakan argumen untuk sebuah fungsi. Ini membuat bingung orang lain yang membacanya (mungkin orang lain ini kita sendiri di masa depan).

edit: Saya baru menemukan artikel dari Martin Fowler mengenai [FlagArgument](https://martinfowler.com/bliki/FlagArgument.html). Teman-teman bisa mendapatkan alasan lebih detil dan kapan kita tidak perlu me-refactor hal ini.

![Photo by Chris Ried on Unsplash]({{ site.baseurl }}/assets/chris-ried-ieic5Tq8YMk-unsplash-optimize.jpg "Photo by Chris Ried on Unsplash")
Photo by <a href="https://unsplash.com/@cdr6934?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Chris Ried</a> on <a href="https://unsplash.com/s/photos/python?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

## Pada Awalnya

Berikut ini sebuah contoh sederhana dalam bahasa pemrograman Python.

```python
class Prediction():
    def __init__(self, user_id):
        self.user_id = user_id

    def results(self):
        seed = Seed.data(self.user_id)
        recommendations = Model.predict(seed)

        if len(recommendations) <= 10:
            recommendations += Fallback.result()

        return recommendations

class Seed:
    def data(user_id):
        return [1, 2, 3, 4, 5]

class Model:
    def predict(seed):
        return [6, 7, 8, 9, 10]

class Fallback:
    def result():
        return [11, 12, 13, 14, 15]

user_id = 1
print(Prediction(user_id).results())
```

## Permintaan Baru

Waktu berjalan, tiba-tiba datang permintaan dari tim Product untuk menambahkan Prediction untuk konten spesial. Program yang kita buat belum memiliki kemampuan untuk mem-filter konten-konten yang spesial ini. Story dibuat dan kita ambil. Hal yang paling mudah adalah dengan menambahkan `if` di dalam `Prediction(user_id).result(special=True)`.

```python
class Prediction():
    def __init__(self, user_id):
        self.user_id = user_id

    def results(self, special=False):
        seed = Seed.data(self.user_id)
        recommendations = Model.predict(seed)

        if special:
            recommendations = Special.filter(recommendations)

        if len(recommendations) <= 10:
            recommendations += Fallback.result()

        return recommendations

class Special:
    def filter(recommendations):
        return [x for x in recommendations if x % 2 == 0]

user_id = 1
print(Prediction(user_id).results())
print(Prediction(user_id).results(special=True))
```

## Permintaan Lagi

Lalu ada lagi permintaan untuk menggunakan fallback yang spesial juga. Dapat diambil dari `FallbackSpecial.result()`. Kita kembali ke kode dan menambahkan if lagi.

```python
class Prediction():
    def __init__(self, user_id):
        self.user_id = user_id

    def results(self, special=False):
        seed = Seed.data(self.user_id)
        recommendations = Model.predict(seed)

        if special:
            recommendations = Special.filter(recommendations)

        if len(recommendations) <= 10:
            recommendations += self.fallback(special)

        return recommendations

    def fallback(self, special=False):
        if special:
            return FallbackSpecial.result()
        else:
            return Fallback.result()

class FallbackSpecial:
    def result():
        [17, 19, 21]

user_id = 1
print(Prediction(user_id).results())
print(Prediction(user_id).results(special=True))
```

Wah, jadi semakin kompleks ya. Dalam perkembangannya kemungkinan besar kita juga diminta melakukan perubahan pada non-spesial dan spesial. Bahkan antara dua kondisi tersebut bisa jadi memiliki logic yang sangat berbeda. Saya ingin menawarkan sudut pandang yang lain. Bagaimana jika kita tidak perlu menambahkan argumen? Bagaimana jika kita membuat method atau bahkan kelas yang berbeda untuk kedua kondisi ini? Ada yang bilang hal tersebut tidak `DRY (Don't Repeat Yourself)`. Saya akan mencoba menawarkan sudut pandang ini.

## Solusi (Menurut Saya)

Pertama, buatlah kelas yang persis sama, namun tanpa `if` conditional.

```python
class Prediction():
    def __init__(self, user_id):
        self.user_id = user_id

    def results(self, special=False):
        seed = Seed.data(self.user_id)
        recommendations = Model.predict(seed)

        if len(recommendations) <= 10:
            recommendations += self.fallback()

        return recommendations

    def fallback(self, special=False):
        return Fallback.result()

class PredictionSpecial():
    def __init__(self, user_id):
        self.user_id = user_id

    def results(self):
        seed = Seed.data(self.user_id)
        recommendations = Model.predict(seed)

        recommendations = Special.filter(recommendations)

        if len(recommendations) <= 10:
            recommendations += self.fallback()

        return recommendations

    def fallback(self, special=False):
        return FallbackSpecial.result()

user_id = 1
print(Prediction(user_id).results())
print(PredictionSpecial(user_id).results())
```

Wah, jadi lebih banyak ya dan banyak code yang terduplikasi karena refactoring ini. Untuk membuang duplikasi, kita bisa menggunakan inheritance. Dalam hal ini kelas `PredictionSpecial` merupakan spesialisasi dari kelas `Prediction`. Sebenarnya ada banyak cara, untuk kali ini saya memilih cara ini.

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

Dengan begini, kita bisa men-spesialisasi `PredictionSpecial`. Cara ini mungkin bukan yang terbaik, tapi paling tidak bisa memberikan solusi untuk future proof di kemudian hari bila banyak kebutuhan yang ingin ditambahkan untuk kedua kondisi yang berbeda. Bahkan jika kita memiliki kondisi baru, misalnya `PredictionSuperSpecial`, kita juga bisa membuatnya dengan lebih mudah tanpa memberikan argumen baru.

Nah, tapi kenapa tetap ada `if len(recommendations) <= 10`? Karena kondisi ini tidak di-passing melalui argumen, kondisi ini tidak masalah dan memang sesuai dengan kebutuhannya, yaitu memeriksa apakah jumlah prediction sesuai dengan kebutuhan. Dalam keadaan nyata, jumlah prediction diambil dari sebuah sumber (database atau prediksi machine learning) yang bisa saja sangat bervariasi per keadaan.

Sebuah quote yang cukup terkenal dan kontroversial (pada saat itu) dari [Sandi Metz](https://sandimetz.com/blog/2015/1/20/the-wrong-abstraction)

> "duplication is far cheaper than the wrong abstraction"

Selamat mencoba. Semoga bermanfaat buat teman-teman semua. Bila ada kritik dan saran, boleh disampaikan di kolom komentar. Terima kasih.