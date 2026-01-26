# Laporan Praktikum Kriptografi
Minggu ke-: 14  
Topik: Analisis Serangan Kriptografi  
Nama: Nur Fatahillah  
NIM: 230202772  
Kelas: 5IKRB  

---

## 1. Tujuan
- Mengidentifikasi jenis serangan pada sistem informasi nyata.
- Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
- Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.

---

## 2. Dasar Teori
Analisis serangan kriptografi merupakan kajian yang membahas berbagai teknik dan metode yang digunakan untuk melemahkan atau memecahkan sistem kriptografi. Tujuan utama dari analisis ini adalah untuk mengevaluasi tingkat keamanan suatu algoritma kriptografi dengan mengidentifikasi celah yang dapat dimanfaatkan oleh penyerang. Serangan kriptografi dapat menargetkan aspek matematis algoritma, implementasi sistem, maupun pola penggunaan kunci, sehingga analisis ini menjadi bagian penting dalam perancangan dan pengujian sistem keamanan informasi.

Secara umum, serangan kriptografi dapat diklasifikasikan ke dalam beberapa jenis, seperti brute force attack, known-plaintext attack, chosen-plaintext attack, dan man-in-the-middle attack. Selain itu, terdapat pula serangan berbasis implementasi seperti side-channel attack yang memanfaatkan kebocoran informasi dari perangkat keras, misalnya waktu eksekusi atau konsumsi daya. Dengan melakukan analisis serangan kriptografi secara menyeluruh, pengembang dapat meningkatkan ketahanan sistem kriptografi melalui pemilihan algoritma yang kuat, manajemen kunci yang baik, serta penerapan standar keamanan yang tepat.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan hashlib

---

## 4. Langkah Percobaan
1. Menentukan studi kasus serangan kriptografi, yaitu serangan brute force dan collision pada algoritma hash MD5.
2. Mengidentifikasi vektor serangan yang memanfaatkan kelemahan algoritma MD5.
3. Menganalisis penyebab kelemahan MD5 berdasarkan literatur dan dokumentasi keamanan.
4. Melakukan simulasi hashing password menggunakan algoritma MD5 dan SHA-256.
5. Membandingkan hasil hash dari kedua algoritma untuk melihat perbedaan tingkat keamanan.
6. Menyusun rekomendasi algoritma kriptografi yang lebih aman sebagai solusi.

---

## 5. Source Code
```python
import hashlib

password = "password123"

md5_hash = hashlib.md5(password.encode()).hexdigest()
sha256_hash = hashlib.sha256(password.encode()).hexdigest()

print("Password :", password)
print("MD5 Hash :", md5_hash)
print("SHA-256 Hash :", sha256_hash)

```

---

## 6. Hasil dan Pembahasan
Hasil eksekusi program menunjukkan bahwa algoritma MD5 menghasilkan nilai hash yang lebih pendek dibandingkan SHA-256. SHA-256 menghasilkan hash sepanjang 256-bit yang lebih kompleks dan sulit untuk ditebak. Dari hasil simulasi, kedua algoritma menghasilkan hash yang berbeda untuk input yang sama.

Hasil eksekusi program :

![Hasil Eksekusi](screenshots/image.png)

---

## 7. Jawaban Pertanyaan

- Pertanyaan 1: Banyak sistem lama masih rentan terhadap brute force atau dictionary attack karena menggunakan algoritma kriptografi yang sudah usang dan tidak dirancang untuk menghadapi kemampuan komputasi modern. Selain itu, sistem lama sering kali menyimpan password tanpa mekanisme pengamanan tambahan seperti salt dan key stretching. Keterbatasan pembaruan sistem serta ketergantungan pada konfigurasi lama juga menyebabkan sistem tersebut tetap menggunakan metode autentikasi yang lemah, sehingga mudah dieksploitasi oleh penyerang.  
- Pertanyaan 2: Kelemahan algoritma merupakan kelemahan yang berasal dari desain atau konsep matematis algoritma kriptografi itu sendiri, seperti ketidakmampuan algoritma dalam menahan serangan collision atau brute force. Contohnya adalah algoritma MD5 yang tidak lagi memiliki sifat collision resistance yang kuat.
Sementara itu, kelemahan implementasi terjadi akibat kesalahan dalam penerapan algoritma yang sebenarnya aman, seperti penggunaan kunci yang terlalu pendek, penyimpanan password dalam bentuk plaintext, atau kesalahan konfigurasi sistem. Dengan kata lain, algoritma yang kuat tetap dapat menjadi tidak aman jika diimplementasikan dengan cara yang keliru.  
- Pertanyaan 3: Organisasi dapat memastikan sistem kriptografi tetap aman di masa depan dengan menerapkan algoritma kriptografi yang mengikuti standar keamanan terkini dan melakukan pembaruan sistem secara berkala. Selain itu, organisasi perlu menerapkan manajemen kunci yang baik, menggunakan algoritma yang tahan terhadap serangan brute force, serta melakukan audit dan pengujian keamanan secara rutin. Edukasi terhadap pengembang dan administrator sistem juga penting agar implementasi kriptografi dilakukan sesuai dengan praktik terbaik yang direkomendasikan.  

---

## 8. Kesimpulan
Berdasarkan analisis yang telah dilakukan, dapat disimpulkan bahwa banyak sistem lama masih rentan terhadap serangan brute force dan dictionary attack akibat penggunaan algoritma kriptografi yang sudah tidak aman serta lemahnya mekanisme perlindungan tambahan. Perbedaan antara kelemahan algoritma dan kelemahan implementasi menunjukkan bahwa keamanan sistem tidak hanya bergantung pada kekuatan algoritma, tetapi juga pada cara penerapannya. Oleh karena itu, organisasi perlu melakukan pembaruan algoritma, menerapkan praktik keamanan yang baik, serta melakukan evaluasi dan audit keamanan secara berkala agar sistem kriptografi tetap aman di masa depan.

---

## 9. Daftar Pustaka
---

## 10. Commit Log
```
week14-analisis-serangan
Author: Nur Fatahillah <dneth001@gmail.com>
Date:   2026-01-26

    week14-analisis-serangan: Analisis Serangan Kriptografi
```
