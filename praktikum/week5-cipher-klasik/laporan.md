# Laporan Praktikum Kriptografi
Minggu ke-: 5  
Topik: Chiper Klasik  
Nama: Nur Fatahillah  
NIM: 230202772  
Kelas: 5IKRB  

---

## 1. Tujuan
1. Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
2. Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
3. Mengimplementasikan algoritma transposisi sederhana.
4. Menjelaskan kelemahan algoritma kriptografi klasik.

---

## 2. Dasar Teori
Cipher klasik adalah sistem penyandian tradisional yang digunakan sebelum munculnya komputer modern. Sistem ini bekerja dengan cara mengubah teks asli atau plaintext menjadi teks sandi (ciphertext) menggunakan aturan tertentu agar isi pesan tidak dapat dibaca oleh pihak yang tidak berwenang. Proses kebalikannya disebut dekripsi, yaitu mengembalikan ciphertext menjadi plaintext dengan menggunakan kunci yang sesuai. Keamanan cipher klasik bergantung pada kerahasiaan kunci dan aturan penyandian yang digunakan, bukan pada kompleksitas algoritmanya.

Secara umum, cipher klasik terbagi menjadi dua jenis utama, yaitu cipher substitusi dan cipher transposisi. Pada cipher substitusi, setiap huruf pada plaintext diganti dengan huruf lain berdasarkan pola tertentu. Contohnya adalah Caesar Cipher, yang mengganti setiap huruf dengan huruf lain yang berjarak tetap dalam alfabet, serta Vigenère Cipher, yang menggunakan beberapa abjad pengganti berdasarkan kunci berulang untuk meningkatkan kerumitan. Sementara itu, pada cipher transposisi, huruf-huruf dalam plaintext tidak diganti, tetapi diubah urutannya sesuai pola tertentu, seperti pada Rail Fence Cipher atau Columnar Transposition Cipher.

Keamanan cipher klasik cukup terbatas karena sifatnya yang masih mempertahankan pola statistik bahasa asli. Hal ini membuat cipher klasik rentan terhadap analisis frekuensi, di mana penyerang dapat menebak isi pesan dengan mempelajari pola kemunculan huruf. Meskipun demikian, cipher klasik memiliki peran penting dalam sejarah kriptografi karena menjadi dasar pengembangan algoritma enkripsi modern yang jauh lebih aman dan kompleks. Prinsip-prinsip dasar seperti substitusi, transposisi, penggunaan kunci, dan analisis statistik masih digunakan dalam kriptografi digital saat ini.


---

## 3. Alat dan Bahan
- Python 3.12  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
```python caesar
def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

# Contoh uji
msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```

```python transpose
def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# Contoh uji
msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```

```python vignere
def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

# Contoh uji
msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```

---

## 6. Hasil dan Pembahasan
![Hasil caesar](screenshots/caesar.png)
![Hasil transpose](screenshots/transpose.png)
![Hasil vignere](screenshots/vigenere.png)

---

## 7. Jawaban Pertanyaan 
- Pertanyaan 1: Kelemahan utama Caesar Cipher adalah pola pergeserannya yang sangat sederhana dan tetap, sehingga mudah ditebak dengan mencoba semua kemungkinan pergeseran (hanya 25 kemungkinan dalam alfabet Latin). Selain itu, karena pola huruf dalam ciphertext tetap mengikuti frekuensi huruf dalam bahasa aslinya, cipher ini sangat rentan terhadap analisis frekuensi, di mana penyerang dapat membandingkan pola huruf ciphertext dengan statistik huruf dalam bahasa tertentu untuk menemukan kunci. Sementara itu, Vigenère Cipher memang lebih kuat karena menggunakan beberapa abjad pengganti, tetapi kelemahannya muncul jika panjang kunci pendek atau berulang, sebab pola pengulangan dapat dianalisis menggunakan metode seperti Kasiski examination atau Index of Coincidence untuk menemukan panjang kunci dan kemudian memecah cipher menjadi beberapa Caesar Cipher terpisah.  
- Pertanyaan 2: Cipher klasik secara umum mudah diserang dengan analisis frekuensi karena sifat bahasa manusia yang memiliki pola tertentu, beberapa huruf atau kombinasi huruf muncul lebih sering daripada yang lain. Ketika cipher tidak sepenuhnya menghilangkan pola statistik ini, seperti pada Caesar atau monoalphabetic cipher, penyerang dapat menggunakan distribusi huruf umum (misalnya huruf “E” yang sering muncul dalam bahasa Inggris) untuk menebak substitusi yang digunakan. Hal ini membuat cipher klasik rentan meskipun tanpa mengetahui kunci secara langsung.  
- Pertanyaan 3: Jika dibandingkan, cipher substitusi dan cipher transposisi memiliki kelebihan dan kelemahan masing-masing. Cipher substitusi mengganti setiap huruf dengan simbol lain, sehingga lebih sulit dikenali secara langsung, tetapi pola frekuensi huruf tetap muncul, menjadikannya rentan terhadap analisis statistik. Sementara itu, cipher transposisi tidak mengganti huruf, melainkan hanya mengubah urutannya, sehingga frekuensi huruf tetap sama, tetapi pola struktur kata menjadi rusak. Kelebihan cipher transposisi adalah hasil ciphertext-nya tampak acak dan sulit dibaca, namun jika penyerang mengetahui pola atau panjang kunci yang digunakan, ciphertext dapat diuraikan dengan mudah. Karena itu, cipher modern sering menggabungkan kedua teknik ini untuk meningkatkan keamanan.
---

## 8. Kesimpulan
cipher klasik merupakan dasar penting dalam perkembangan ilmu kriptografi, meskipun tingkat keamanannya masih rendah dibandingkan sistem modern. Algoritma seperti Caesar Cipher dan Vigenère Cipher menunjukkan bagaimana penyandian bekerja melalui substitusi dan transposisi huruf, namun keduanya memiliki kelemahan utama, terutama karena masih mempertahankan pola statistik bahasa yang mudah dianalisis. Serangan seperti analisis frekuensi dapat memanfaatkan pola kemunculan huruf untuk menebak kunci atau isi pesan tanpa harus mengetahui algoritma secara pasti. Meskipun begitu, konsep-konsep dasar yang digunakan pada cipher klasik seperti substitusi, transposisi, dan penggunaan kunci tetap menjadi fondasi penting dalam perancangan algoritma enkripsi modern yang lebih kompleks dan aman.

---

## 9. Daftar Pustaka
---

## 10. Commit Log
```
commit week5-cipher-klasik
Author: Nama Mahasiswa <email>
Date:   2025-10-30

    week5-cipher-klasik (Caesar, Vigenère, Transposisi)
```
