---
layout: post
title: Penyebab dan Pencegahan Flaky Test
description: Bagaimana bisa menemukan dan mencegah Flaky Test
date: 2022-03-23 07:30:33.222222222 +07:00
type: post
published: true
status: publish
permalink: /2022-03-23-penyebab-pencegahan-flaky-test/
categories: 
- Test-Driven Development
tags:
- tdd
- clean code
- software engineering
comments: true
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---

## Background

TDD (Test Driven Development) merupaka development practice yang saya pelajari dan adopsi sekitar tahun 2013. Saat itu saya menggunakan PHP Laravel. Saya merasa practice ini sangat membantu dalam membuat software yang sesuai dengan requirement. Behavior software yang kita buat akan di-"enforce" dengan spesifikasi dari test. Saya merasakan manfaat yang sangat besar sampai hari ini dalam membuat test, sampai rekan saya waktu freelance menyebutkan bahwa kami tidak bisa charge "maintenance fee" karena dalam setahun tidak ada bug dalam software yang kami jual.

TDD juga merupakan "culture" yang diadopsi di Vidio.com, perusahaan tempat saya bekerja saat ini. TDD mengharuskan seorang programmer untuk menulis test sebelum mengimplementasikan code. Scope dari code ini mulai dari sebuah fitur, komponen, bahkan sampai ke level method. Pengalaman saya, hal ini akan membuat coverage dari software yang kita buat selalu berada di atas 90%.

Dengan menulis automated test ini, kita dapat mengurangi test manual yang kita lakukan, memikirkan "edge cases" yang mungkin terjadi pada bagian tersebut dan menjaga agar software tidak mendapatkan "regression" saat diubah di kemudian hari. Kita menjadi percaya diri dalam menulis sebuah fitur, yakin saat melakukan deployment dan dapat juga digunakan sebagai "penjaga" agar sebuah bug tidak muncul lagi. Serta sebagai cara untuk mengurangi waktu feedback cycle, maksudnya supaya kita bisa mengetahui apakah software kita berjalan sesuai ekspektasi, jauh sebelum production environment.

Namun akan ada masalah saat kita sudah memiliki banyak test, apalagi jika kita perlu banyak thread atau bahkan banyak mesin untuk menjalankan test ini. Masalah yang seringkali muncul adalah "Flaky Test". Flaky test adalah test yang tidak deterministik, kadang error, kadang berhasil. Jika kita melihat definisi flaky dalam [Merriam-Webster](https://www.merriam-webster.com/dictionary/flaky), flaky adalah sesuatu yang tidak dapat diandalkan dalam kinerja dan prilaku. Test yang seperti ini membuat kita meragukan apakah software kita ada bug yang kita tidak tahu? Apakah kita perlu menghentikan CI (Continous Integration)? Boleh di deploy atau tidak? Dan jika ini terus menerus dibiarkan, maka kita akan mengabaikan build, menganggap merah itu biasa atau bahkan melakukan deploy terhadap build yang gagal (karena merasa itu hanya karena flaky padahal tidak).

![Photo by Julian on Unsplash]({{ site.baseurl }}/assets/julian-YHaS_ChB0FI-unsplash.jpg "Photo by Julian on Unsplash")
Photo by <a href="https://unsplash.com/@photasticlab?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Julian</a> on <a href="https://unsplash.com/s/photos/snowflake?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

## Penyebab dan Pencegahan Flaky Test

### Asynchronous Behavior

Penyebab yang biasa saya alami adalah asynchronous behavior. Sebagai contoh, kita memiliki sebuah button yang baru bisa di-klik saat suatu AJAX call berhasil, maka kita tidak bisa membuat test yang mengharapkan button tersebut langsung bisa di-klik. Yang sering dilakukan oleh saya, kita menambahkan timeout sebelum mengecek status button tersebut. Hal ini mungkin dapat berjalan, namun tidak deterministik. Bisa jadi saat ini hal tersebut bisa selesai dalam 500ms akan tetapi di test berikutnya akan membutuhkan waktu 2s.

Dalam buku [Growing Object-Oriented Software Guided by Tests](https://learning.oreilly.com/library/view/growing-object-oriented-software/9780321574442/ch27.html), para penulis buku tersebut memberikan beberapa tips dalam menghadapi Asynchronous Behavior, yaitu dengan membuat test yang menunggu hal tersebut terjadi. Tentunya dengan tetap memperhatikan timeout. Alternatif lain yaitu dengan cara sampling / polling. Test akan melakukan polling setiap sekian waktu untuk mengecek apakah hasilnya sudah benar.

Beberapa tips diulas oleh Thoughbot di [blog mereka](https://thoughtbot.com/blog/write-reliable-asynchronous-integration-tests-with-capybara). Tips ini menggunakan Rails.

### Database Ordering

Jika kita tidak memberikan `ORDER BY` dalam sebuah perintah SQL, jangan pernah berasumsi bahwa ordering yang kita dapat saat itu akan selalu sama setiap saat. Hal ini pernah ditanyakan di [stackoverflow](https://stackoverflow.com/questions/20050341/when-no-order-by-is-specified-what-order-does-a-query-choose-for-your-record) dan dijawab dengan referensi dari [Connor Cunningham](https://web.archive.org/web/20160808070425/https://blogs.msdn.microsoft.com/conor_cunningham_msft/2008/08/27/no-seatbelt-expecting-order-without-order-by/) dan [Alexander Kuznetsov](https://web.archive.org/web/20130922121836/http://sqlblog.com/blogs/alexander_kuznetsov/archive/2009/05/20/without-order-by-there-is-no-default-sort-order.aspx).

Pada Postgresql, jika membutuhkan ordering pada saat kita menggunakan query `WHERE somecolumn IN`, kita dapat menggunakan `array_position(sorted_values, column)`, contohnya:

```sql
SELECT *
FROM tracks 
WHERE id IN (5, 3, 1, 9, 7)
ORDER BY array_position(ARRAY[5, 3, 1, 9, 7], id);
```

Kondisi lain yang biasanya dilupakan adalah saat kolom yang di-sort pada `ORDER BY` dibuat dengan value yang sama. Misalnya kita ingin record yang diberikan di-sort berdasarkan `created_at`, akan tetapi kita membuat semua record pada detik yang sama. Hal ini membuat kembalian dari database tidak menggunakan urutan yang sama setiap kali test. Saat kita membutuhkan urutan yang harus selalu sama dalam test, perhatikan kolom yang di-order. Sebagai contoh saat kita membuat test fixture pada Rails.

```yaml
track_one:
  title: Track One
  created_at: <%= 39.minutes.ago.to_fs(:db) %>

track_two:
  title: Track Two
  created_at: <%= 38.minutes.ago.to_fs(:db) %>

track_three:
  title: Track Three
  created_at: <%= 37.minutes.ago.to_fs(:db) %>
```

Atau jika kita tidak membutuhkan ordering tertentu saat assertion, gunakan assertion `assert_includes` atau `include` matchers pada Rspec (`expect([1, 2, 3]).to include(1, 3, 2)`). Hal ini supaya test kita tidak mengharapkan hasilnya selalu dalam ordering yang kita harapkan.

### Penggunaan Waktu

Saat kita ingin melakukan assertion berdasarkan waktu pada sebuah test, usahakan untuk menggunakan waktu yang fixed. Fungsi `Date.today` atau `DateTime.now` pada Rails adalah fungsi yang tidak pure. Maksudnya kedua fungsi ini bisa memberikan hasil yang berbeda tergantung waktu kita menjalankan. Fungsi `Date.today` akan berubah setiap hari. Sedangkan fungsi `DateTime.now` bisa berubah setiap detik. Mungkin kita ingin melakukan assertion hanya dihari Rabu, maka test kita hanya akan berhasil di hari Rabu. Gunakanlah library seperti [Timecop](https://github.com/travisjeffery/timecop) untuk memudahkan kita melakukan assertion berdasarkan fungsi waktu. Atau kita juga dapat melakukan stub (tapi hal ini tidak saya rekomendasikan).

```ruby
describe "some set of tests to mock" do
  before do
    Timecop.freeze(Time.local(2022, 3, 22, 6, 44, 0))
  end

  after do
    Timecop.return
  end

  it "should do blah blah blah" do
  end
end
```

### Test yang tergantung dengan Test lainnya

Biasanya disetiap testing library atau framework ada sebuah fitur untuk melakukan random pada urutan eksekusi test. Hal ini membuat test yang tergantung dengan test lainnya menjadi Flaky. Karena tidak ada jaminan test pertama akan dieksekusi sebelum test kedua. Jika kita menemukan hal ini ada beberapa solusi yang bisa kita lakukan.

Pertama adalah tidak me-random urutan test. Dalam Minitest ataupun Rspec, dikenal dengan nama seed. Pada keduanya, kita bisa memberikan argument `--seed SEED` di mana `SEED` dapat berupa angka. Solusi ini baik dalam jangka pendek akan tetapi masih beresiko Flaky. Jika kita menggunakan TDD, maka setiap fitur yang dibuat akan memiliki test. Penambahan test ini tidak otomatis ditaruh diurutan terakhir. Bisa saja menyelip ke tengah. Hal ini akan membuat test menjadi Flaky kembali.

Solusi kedua adalah dengan mencari dan menghilangkan sumber kebergantungan ini. Umumnya flaky jenis ini adalah karena ada test yang setup ataupun teardown-nya tidak bersih. Sehingga test tersebuh membutuhkan test lain untuk setup (dijalankan sebelumnya) atau merusak test yang berjalan setelahnya. Penggunaan Timecop yang tidak di-return misalnya, atau WebMock yang tidak di-disable atau enable, cache yang tidak dibersihkan, database yang tidak dibersihkan dan lain sebagainya. Setelah ini bisa dihilangkan, maka test kita tidak akan flaky lagi meskipun selalu di random. Justru salah satu tujuan dari penggunaan `--seed SEED` itu sendiri adalah agar test kita tidak saling tergantung satu dengan yang lainnya.

Ada trik yang bisa dilakukan untuk mencari dan menghilangkan sumbernya, yaitu dengan mengulang test yang gagal saja. Ini dapat mengisolasi test tersebut dari test lain untuk memastikan test itu tidak membutuhkan test lain. Meskipun sebelumnya saya tidak menyukai ide ini, namun selalu ada konteks dalam setiap solusi yang kita gunakan. Jika test kita banyak dan tim yang memrogram aplikasi tersebut juga besar, 1 test yang gagal akibat hal ini akan sangat membuat frustasi. Akan tetapi selalu usahakan test yang di-retry dicek dan dicegah agar tidak masuk ke barisan retry.

Oh iya, selalu gunakan seed yang sama dengan yang ada di CI (yang flaky) untuk dapat mereproduksi flaky test di local development kita. Seed yang sama akan menghasilkan urutan test yang sama, sehingga error yang terjadi dapat terjadi juga di mesin kita.

### Penggunaan Faker

[Faker](https://github.com/faker-ruby/faker) adalah tools untuk mempermudah kita menulis test dengan memberikan value random. Biasanya field seperti `name`, `description`, `birthday`, dll dapat menggunakan Faker untuk membuatkan value-nya. Akan tetapi kita perlu memperhatikan kebutuhan field-field tersebut, karena Faker kadang juga memiliki karakter spesial pada beberapa fungsinya. Hati-hati saat kita akan menggunakannya dalam konversi CSV yang sangat sensitif terhadap koma atau fungsi lain yang memiliki sensitivitas terhadap karakter-karakter spesial.

## Kesimpulan

Test yang kita buat adalah sebuah code juga. Meskipun tidak dijalankan di production, akan tetapi setiap code akan menuntut kita untuk melakukan pemeliharaan terhadapnya. Hal ini termasuk refactoring (agar test kita lebih mudah dibaca) dan mencegah flaky test adalah salah duanya. Saya akan mencoba mengupdate post ini bila menemukan penyebab lain dari Flaky Test. Inspirasi dari post ini adalah guide yang saya buat di Vidio.com dalam proses mencari dan mencegah Flaky test.

Sekian dari saya, kalau ada saran atau teman-teman mempunyai pengalaman mengenai Flaky test ini, silahkan tuliskan di kolom komentar. Mudah-mudahan bermanfaat. Terima kasih.