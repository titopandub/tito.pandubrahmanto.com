---
layout: post
title: Upgrade Ruby (2.1.2) dan Rails
description: Bagaimana mengupgrade aplikasi Ruby on Rails yang tidak pernah di-update sejak tahun 2016.
date: 2022-02-06 21:30:00.000000000 +07:00
type: post
published: true
status: publish
permalink: /2022-02-07-upgrade-ruby-dan-rails/
categories:
- Computer
tags:
- programming
- web-development
- ruby
- rails
- docker
- container
comments: true
author:
  login: tito
  email: tito@pandubrahmanto.com
  display_name: Tito
  first_name: Tito
  last_name: Pandu Brahmanto
---
# Aplikasi "Jadul"

Sebuah aplikasi yang saya buat bersama teman saya di tahun 2014, beberapa bulan yang lalu mendapatkan notifikasi email dari Heroku kalau aplikasi ini sudah tidak didukung lagi. Hal ini karena versi Ruby yang digunakan adalah `2.1.2`. Versi ini tidak lagi mendapatkan dukungan dari Ruby team[^1]. Heroku (Platform As A Service) yang saya gunakan juga tidak lagi memberikan dukungan untuk cedar-14 stack yang digunakan oleh aplikasi saya[^2]. Jika saya tidak mau meng-upgrade, maka saya tidak bisa melakukan deploy terhadap aplikasi ini. Jika tidak bisa melakukan deploy, artinya saya tidak bisa melakukan fix atau menambah fitur baru ke aplikasi ini. Karena hal inilah saya memutuskan untuk melakukan upgrade Ruby dan Rails ke versi yang didukung oleh Heroku.

# Menjalankan Aplikasi

Sebelum melakukan upgrade, karena aplikasi ini sudah cukup lama tidak saya "sentuh", maka saya mencoba untuk menjalankannya. Saya coba install Ruby `2.1.2` menggunakan [rbenv](https://github.com/rbenv/rbenv). Hasilnya... Zonk!. Saya sudah tidak bisa memasang Ruby `2.1.2` melalui rbenv, karena saya menggunakan Ubuntu 20.04 yang sudah tidak mendukung library yang dibutuhkan Ruby `2.1.2`. Ini disebabkan Ubuntu 20.04 menggunakan openssl versi 1.1, sedangkan Ruby dibawah versi `2.4` membutuhkan versi 1.0[^3].

```
$ rbenv install 2.1.2
Downloading ruby-2.1.2.tar.bz2...
-> https://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.bz2
Installing ruby-2.1.2...

WARNING: ruby-2.1.2 is past its end of life and is now unsupported.
It no longer receives bug fixes or critical security updates.


BUILD FAILED (Ubuntu 20.04 using ruby-build 20211227-3-gcdc215e)

Inspect or clean up the working tree at /tmp/ruby-build.20220206202538.62579.iunGXq
Results logged to /tmp/ruby-build.20220206202538.62579.log
```

Daripada bersusah payah menginstall openssl 1.0, saya memutuskan untuk menjadi momen ini sebagai kesempatan belajar Docker dan Docker Compose.

## Menggunakan Docker

Di tempat kerja saya, kami terbilang bukan early adopter dari Docker. Kami baru menggunakannya sebagai development tools. Awalnya saya skeptis, karena merasa VM (dengan vagrant dan virtualbox) sudah cukup. Namun saya akhirnya harus menyerah pada VM dan menggunakan Docker saat saya "terpaksa" menggunakan laptop Windows saya untuk bekerja. WSL2 memiliki support yang lebih baik untuk Docker ketimbang VM (karena menggunakan Hypervisor).

Dalam kasus ini, saya mencoba menggunakan Docker Compose untuk menjalankan aplikasi saya ini. Sebenarnya banyak trial dan error dalam membuat Docker Compose ini, tapi saya akan memberikan versi yang sudah jadi. Saya menggunakan tutorial dari Jason Swett di [Dockerize Rails Application](https://www.codewithjason.com/dockerize-rails-application/)

### Dockerfile

```dockerfile
FROM ruby:2.1.2

WORKDIR /code

COPY . /code

RUN apt-get update && apt-get -y install curl gnupg apt-utils
RUN curl -sL https://deb.nodesource.com/setup_12.x  | bash - && apt-get -y --force-yes install nodejs && npm install
RUN bundle config github.https true && bundle install --full-index

CMD ["rails", "server", "-b", "0.0.0.0"]
```

### docker-compose.yml

```yaml
version: "3.8"

# Each thing that Docker Compose runs is referred to as
# a "service". In our case, our Rails application is one
# service ("web") and our PostgreSQL database instance
# is another service ("database").
services:

  database:
    image: postgres:9.6.24
    environment:
      POSTGRES_PASSWORD: password1

    volumes:
      - db_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

  web:
    build: .
    volumes:
      - .:/code:cached
    command: bash -c "rm -f tmp/pids/server.pid && bundle exec rails s -p 3000 -b '0.0.0.0'"
    ports:
      - "3000:3000"
    depends_on:
      - database
    environment:
      RAILS_ENV: development
      DATABASE_NAME: office_service_development
      DATABASE_USER: dbuser
      DATABASE_PASSWORD: dbpassword
      DATABASE_HOST: database

# Declare the volumes that our application uses.
volumes:
  db_data:
```

# Berhasil Install, Semua Test Hijau, Upgrade!

Setelah berhasil menjalankan aplikasi dan semua test hijau. Saya memulai untuk mengupgrade perlahan-lahan dari mulai 2.1.2 sampai 2.6.9. Kira-kira prosesnya adalah seperti ini

1. Upgrade dari `2.1.2` ke `2.1.10` (versi paling akhir dari 2.1)
2. Pastikan test berjalan lancar, jika tidak upgrade gem yang diperlukan dan coba lakukan test kembali.
3. Upgrade dari `2.1.10` ke `2.2.10` (versi paling akhir dari 2.2)
4. Pastikan test berjalan lancar, jika tidak upgrade gem yang diperlukan dan coba lakukan test kembali.
5. Upgrade dari `2.2.10` ke `2.3.8` (versi paling akhir dari 2.3)
6. Pastikan test berjalan lancar, jika tidak upgrade gem yang diperlukan dan coba lakukan test kembali.
7. Upgrade dari `2.3.8` ke `2.4.10` (versi paling akhir dari 2.4)
8. Pastikan test berjalan lancar, jika tidak upgrade gem yang diperlukan dan coba lakukan test kembali.
9. Upgrade dari `2.4.10` ke `2.5.9` (versi paling akhir dari 2.5)
10. Pastikan test berjalan lancar, jika tidak upgrade gem yang diperlukan dan coba lakukan test kembali.
11. Upgrade dari `2.5.9` ke `2.6.9` (versi paling akhir dari 2.6)
12. Pastikan test berjalan lancar, jika tidak upgrade gem yang diperlukan dan coba lakukan test kembali.

Akhirnya berhasil upgrade ke `2.6.9`, yaitu versi yang didukung oleh Heroku, yaitu heroku-20 stack[^4].

### Dockerfile

```dockerfile
FROM ruby:2.6.9

WORKDIR /code

COPY . /code

RUN apt-get update && apt-get -y install curl gnupg apt-utils
RUN curl -sL https://deb.nodesource.com/setup_12.x  | bash - && apt-get -y --force-yes install nodejs && npm install
RUN bundle config github.https true && bundle install --full-index

CMD ["rails", "server", "-b", "0.0.0.0"]
```

Berikut ini beberapa Gem yang saya perlu upgrade secara "manual" dengan menambahkan versi atau menunjuk ke repository git dari gem tersebut.

```gemfile
source 'https://rubygems.org'
ruby '2.6.9'
gem 'rails', '4.2.11.3'
gem 'bootstrap-sass', '3.2.0.4'
gem 'devise', git: 'https://github.com/plataformatec/devise', branch: '3-stable'
gem 'pundit', '2.1.1'
gem 'rails4-autocomplete'
gem 'acts_as_caxlsx', git: 'https://github.com/caxlsx/acts_as_caxlsx'
gem 'caxlsx'
gem 'caxlsx_rails'
gem 'validates_timeliness', '~> 4.1.1'
gem 'pg', '0.18.4'

group :development, :test do
  gem 'sqlite3'
  gem 'bullet'
  gem 'did_you_mean', '1.3.0'
end
```

# Lessons Learned

Upgrade aplikasi kamu sesering mungkin. Semakin sering kamu lakukan, maka akan semakin mudah untuk melakukannya. Hal ini dikemukakan oleh Martin Fowler di-post-nya berjudul [Frequency Reduce Difficulty](https://www.martinfowler.com/bliki/FrequencyReducesDifficulty.html). Dengan begitu kamu akan memiliki aplikasi yang up to date, mendapatkan support yang baik dari komunitas atau perusahaan.

Sebenarnya saya sendiri sudah membeli beberapa buku Docker, tapi sepertinya sangat sulit untuk mempelajarinya hanya dari buku dan menggunakan contoh yang ada di buku. Dengan menggunakan pendekatan proyek dan langsung terjun menggunakannya, saya merasa ini adalah hal yang sangat efektif. Saya menjadi paham apa saja command-command yang ada di dalam Docker dan Docker Compose, bagaimana menggunakannya, bagaimana konfigurasinya dan pada akhirnya lebih percaya diri dalam menggunakan Docker (dan container pada umumnya).

Semoga bermanfaat.

# Note

Kalau kalian sadar Ruby `2.6.9` sebenarnya akan habis masa dukungannya dan sepertinya saya harus upgrade lagi ke versi Ruby dan mungkin Rails yang lebih tinggi. Dengan adanya pengalaman upgrade ini, saya merasa lebih percaya diri melakukannya, apalagi dengan bantuan tooling seperti Docker.

# Footnote

[^1]: [Support of Ruby 2.1 has ended](https://www.ruby-lang.org/en/news/2017/04/01/support-of-ruby-2-1-has-ended/)
[^2]: [Cedar-14 Stack](https://devcenter.heroku.com/articles/cedar-14-stack)
[^3]: [ruby-build issue](https://github.com/rbenv/ruby-build/issues/1353)
[^4]: [Heroku-20 Stack](https://devcenter.heroku.com/articles/heroku-20-stack)