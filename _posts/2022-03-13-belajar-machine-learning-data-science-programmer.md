---
layout: post
title: Belajar Machine Learning dan Data Science untuk Programmer
description: Perjalanan saya mempelajari Machine Learning dan Data Science.
date: 2022-03-13 21:30:33.222222222 +07:00
type: post
published: true
status: publish
permalink: /2022-03-13-belajar-machine-learning-data-science-programmer/
categories: 
- Machine Learning
tags:
- data science
- programmer
- data analytics
comments: true
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---

## Background

Di awal tahun 2021 yang lalu, saya dipercaya untuk masuk ke tim Recommendation di Vidio.com. Setelah masuk dan mempelajari berbagai model yang digunakan, saya merasa pengetahuan saya sangatlah minim di dunia Data ataupun Machine Learning. Saya memutuskan untuk meng-upgrade diri mempelajari beberapa hal yang menurut saya sangat penting dalam dunia Recommendation ini.

Berikut ini adalah perjalanan saya mempelajari Machine Learning dan Data Science, mudah-mudahan bisa membantu teman-teman yang ingin mempelajarinya.

![Photo by Pietro Jeng on Unsplash]({{ site.baseurl }}/assets/pietro-jeng-n6B49lTx7NM-unsplash.jpg "Photo by Pietro Jeng on Unsplash")
Photo by <a href="https://unsplash.com/@pietrozj?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Pietro Jeng</a> on <a href="https://unsplash.com/s/photos/data-science?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

## Google Machine Learning Crash Course

Berbekal dari rekomendasi teman saya Ade Sueb (Nurhadi), saya memulainya dengan belajar mengenai Machine Learning Crash Course. Dimulai dari Youtube video [Machine Learning Zero to Hero (Google I/O'19)](https://youtu.be/VwVg9jCtqaU) yang dibawakan Laurence Moroney and Karmel Allison. Lalu dilanjutkan dengan [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/). Sebagai software engineer, saya merasa kedua resource ini sangat membantu "nyebur" ke dunia Machine Learning. Karena keduanya tidak terlalu dalam membahas mengenai rumus matematika dan lebih memfokuskan mengenai coding part dari Machine Learning.

Setelah selesai mempelajari keduanya, saya mencoba untuk mengaplikasikan Tensorflow untuk membuat model prediksi Linear Regression untuk [Abalone](https://archive.ics.uci.edu/ml/datasets/Abalone) dari UCI Machine Learning Repository.

## Tensorflow Recommenders

Saya juga mempelajari Guide dan Tutorial dari [Tensorflow Recommenders](https://www.tensorflow.org/recommenders/examples/quickstart). Library dari Tensorflow ini membantu kita untuk membuat recommendation yang berbasis [Collaborative Filtering](https://en.wikipedia.org/wiki/Collaborative_filtering). Di salah satu guide-nya, kita juga diajarkan untuk membuat Hybrid Recommendation yang menggabungkan Content-based dan Collaborative Filtering.

## Machine Learning dari Andrew Ng di Coursera

Sembari membuat model di kantor, saya mengambil course [Machine Learning](https://www.coursera.org/learn/machine-learning) dari Andrew Ng di Coursera. Course ini lebih mengajarkan intuisi dari sebuah model seperti Linear Regression, Logistic Regression, Neural Network dan lainnya. Sayangnya saya berhenti sampai di pembahasan Neural Network. Saya kurang cocok dengan pembahasan yang Bottom Up, yaitu yang menjelaskan dasar dari suatu topik naik sampai ke implementasi. Saya lebih cocok dengan pembahasan Machine Learning Crash Course yang Top Down, di mana membahas implementasi, lalu menjelaskan mengapa itu bisa terjadi.

Setelah berhenti dari Machine Learning Coursera ini, saya lebih memfokuskan diri ke kuliah saya di semester 3 ini dulu. Kebetulan sedang ada mata kuliah Statistika, Struktur Data dan Sistem Operasi, sehingga membuat saya cukup sibuk untuk menggali ketiga mata kuliah tersebut di semester 3.

## AI Powered Search

Di sela-sela waktu kuliah, saya sempatkan membaca buku [AI Powered Search](https://www.manning.com/books/ai-powered-search). Saya melihat banyak improvement yang bisa dilakukan untuk sistem rekomendasi berbasis konten di Vidio. Saya memutuskan untuk menulis beberapa "Epic" agar mudah menjelaskan kepada tim produk maupun teman-teman engineer. Alhamdulillah saat ini ada dua improvement yang sudah kita implementasikan, satu di Search dan satu lagi di Recommendation. Saya sangat senang, meskipun "Epic" yang saya tulis sangat sederhana, teman-teman engineer dan Data Science membuat sistem yang jauh lebih baik daripada apa yang saya baca dari buku. Terima kasih teman-teman.

## Google Data Analytics Professional Certificate

Setelah selesai UAS semester 3, saya mulai mencari lagi course atau buku untuk saya dalami saat "liburan" semester. Di pekerjaan, saya merasa cukup ok dalam membuat model, namun di sisi lain saya masih merasa sangat kurang dalam menganalisa data. Baik itu data yang berkaitan dengan model ataupun data metric sehari-hari. Saya sempat menimbang beberapa course Data Analytics di Coursera, Udemy dan platform lain. Namun akhirnya pilihan saya jatuh pada [Google Data Analytics Professional](https://www.coursera.org/professional-certificates/google-data-analytics).

Course yang diberikan Google cukup mendasar, dari mulai memformulasikan masalah, bertanya kepada stakeholder, memilih data, mengolah data, membersihkan data, menganalisa data, membuat visualisasi untuk data dan mempresentasikan temuan dan kesimpulan kepada stakeholder. Dari sisi teknologi, course ini juga mengajarkan penggunaan spreadsheets, SQL, Tableau dan R. Materi-materi yang diberikan sebenarnya cukup "menginjak tanah", sehingga dapat dipelajari bahkan untuk orang dari luar IT. Karena itu saya merekomendasikan course ini untuk programmer yang baru masuk ke dunia data dan teman-teman yang bukan berkecimpung di dunia IT.

Dari sisi data analysis, course ini membantu saya untuk lebih percaya diri dalam menghadapi masalah yang membutuhkan analisa data. Saya menjadi lebih berani dan lebih mengerti query SQL yang kompleks, terutama yang menggunakan `WITH name AS ()`. Dan meskipun di Vidio kami menggunakan Python, namun pengetahuan mengenai analisa data di R cukup membantu saya dalam menggunakan Pandas di Python. Karena sebenarnya dari konsep antara dataframe di Pandas dengan dataframe di R. Nilai plus dari saya, di R bisa pake pipe `%>%` (meskipun di Python juga ada [library-nya](https://github.com/JulienPalard/Pipe)).

Kalau ada yang ingin tahu Capstone project yang saya kerjakan untuk Google Data Analytics Professional, berikut ini [linknya]({{ site.baseurl }}/assets/Google_Data_Analytics_Capstone_Tito_Bike_Sharing.pdf)

Alhamdulillah saya sudah menyelesaikan [course ini](https://coursera.org/share/b36f7935fb4c437a9387472d225cf31b)

## Grokking Deep Learning

Dari sisi buku, saya sedang membaca [Grokking Deep Learning](https://www.manning.com/books/grokking-deep-learning). Saya merasa cukup kesulitan dalam membaca literatur mengenai Deep Learning, khususnya pada gambar-gambar arsitektur sebuah model Deep Learning. Saya putuskan saya akan mempelajarinya lebih dalam. Setelah membaca ulasan dari beberapa buku, saya sadar kalau saya pernah membeli ebook ini di Manning. Jadi ya tinggal lanjut baca. Manning juga memberikan diskon, yaitu hanya menambah USD 12, saya bisa mendapatkan buku cetaknya. Jadi sekalian saya beli.

Saya belum selesai membaca buku ini. Dari beberapa chapter yang sudah saya baca, saya lihat penjelasannya sangat enak. Disertai banyak gambar, ini membantu saya mengerti mengenai konsep dan arsitektur Deep Learning. Lengkapnya akan saya post di lain waktu.

## Selanjutnya?

Dari sisi course, saya sedang audit course [Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning) dari Andrew Ng di Coursera. Menurut saya course ini lebih fokus ke Deep Learning yang memang kami gunakan di tim Recommendation. Bentuk materinya mirip dengan Machine Learning yang saya ulas sebelumnya, namun yang saya suka dari course ini adalah saya bisa langsung menggunakan ilmunya dalam pekerjaan sehari-hari. Saya belum memutuskan untuk membayar course-nya, karena saya khawatir tidak sempat selesai saat perkuliahan saya dimulai.

## Penutup

Hampir satu tahun saya ada di tim Recommendation. Saya sangat senang bisa belajar sekaligus berkontribusi kepada perusahaan. Hal yang saya sukai adalah belajar dan saya selalu berusaha untuk menggunakan apa yang saya pelajari. Menurut saya perjalanan saya di dunia Machine Learning dan Data Science masih jauh, selain belajar berbagai course dan buku, saya juga berusaha belajar dari rekan-rekan di tim Recommendation. Mulai dari bagaimana mereka melakukan query-query yang rumit, analisa data, membuat visualisasi yang memudahkan kita untuk mengerti sampai membuat model. Setelah pemrograman, sepertinya saya jatuh cinta dikedua bidang ini.

Menurut Andrej Karpathy di salah satu talknya berjudul [Building the Software 2.0 Stack](https://youtu.be/y57wwucbXR8), Software 1.0 adalah kode yang ditulis oleh manusia, sedangkan Software 2.0 adalah kode yang ditulis oleh optimization dalam bentuk Neural Network Training. Meskipun tidak semua software bisa ditulis dengan cara Software 2.0 dan Software 1.0 masih dibutuhkan untuk mendukungnya (dalam bentuk infrastuktur, data pipeline, machine learning pipeline, MLOps, dll), saya merasa kita sebagai programmer perlu mengetahui dan "mencicipi" Software 2.0 ini. Agar kita memiliki alat atau senjata tambahan untuk menyelesaikan sebuah masalah.

Kalau ada masukan mengenai apa yang harus saya pelajari atau dalami, boleh ditulis di kolom komentar. Terima kasih.