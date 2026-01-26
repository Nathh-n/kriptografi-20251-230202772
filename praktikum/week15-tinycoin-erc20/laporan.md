# Laporan Praktikum Kriptografi
Minggu ke-: 15  
Topik: Proyek Kelompok – TinyCoin ERC20  
Nama: Nur Fatahillah  
NIM: 230202772  
Kelas: 5IKRB  

---

## 1. Tujuan
1. Mengembangkan proyek sederhana berbasis algoritma kriptografi.
2. Mendokumentasikan proses implementasi proyek ke dalam repository Git.
3. Menyusun laporan teknis hasil proyek akhir.

---

## 2. Dasar Teori
ERC20 adalah standar token pada blockchain Ethereum yang mendefinisikan seperangkat fungsi dan event agar token dapat saling kompatibel dengan wallet, exchange, dan aplikasi terdesentralisasi (dApp). Fungsi utama ERC20 meliputi totalSupply, balanceOf, transfer, approve, dan transferFrom.

Smart contract adalah program yang berjalan di blockchain dan dieksekusi secara otomatis ketika kondisi tertentu terpenuhi. Dengan menggunakan bahasa Solidity, pengembang dapat membuat token digital yang memiliki nilai dan dapat ditransfer antar akun tanpa perantara. TinyCoin merupakan contoh implementasi token ERC20 sederhana untuk pembelajaran kriptografi dan blockchain.

---

## 3. Alat dan Bahan
- Solidity (bahasa pemrograman smart contract)
- Remix IDE (https://remix.ethereum.org)
- Browser web
- Git dan GitHub

---

## 4. Langkah Percobaan
1. Membuka Remix IDE di browser.
2. Membuat file smart contract baru bernama TinyCoin.sol.
3. Menuliskan kode smart contract ERC20.
4. Melakukan compile smart contract pada Remix IDE.
5. Deploy smart contract ke jaringan lokal (JavaScript VM).
6. Menguji fungsi token seperti totalSupply, balanceOf, dan transfer.

---

## 5. Source Code

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TinyCoin is ERC20 {
    constructor(uint256 initialSupply) ERC20("TinyCoin", "TNC") {
        _mint(msg.sender, initialSupply);
    }
}
```

---

## 6. Hasil dan Pembahasan
Hasil pengujian menunjukkan bahwa smart contract TinyCoin berhasil diimplementasikan sesuai standar ERC20. Fungsi name, symbol, decimals, dan totalSupply mengembalikan nilai yang sesuai dengan spesifikasi token. Token awal berhasil dimint ke akun pembuat kontrak.
Hasil eksekusi program :

![Hasil Eksekusi](screenshots/image.png)

---

## 7. Jawaban Pertanyaan
- Pertanyaan 1: ERC20 berfungsi sebagai standar teknis untuk pembuatan dan pengelolaan token pada blockchain Ethereum. Standar ini mendefinisikan sekumpulan fungsi dan event yang wajib dimiliki oleh sebuah token, seperti transfer, balanceOf, dan totalSupply.

Dengan adanya ERC20, token yang dibuat menjadi kompatibel dan interoperabel dengan berbagai wallet, exchange, dan aplikasi terdesentralisasi (dApps). Hal ini memudahkan pengembang dan pengguna dalam berinteraksi dengan token tanpa perlu penyesuaian khusus.  
- Pertanyaan 2: Mekanisme transfer token pada kontrak ERC20 dilakukan melalui fungsi transfer(address to, uint256 value). Fungsi ini akan memeriksa apakah pengirim memiliki saldo token yang cukup. Jika saldo mencukupi, maka jumlah token akan dikurangi dari akun pengirim dan ditambahkan ke akun penerima.

Selain itu, ERC20 juga menyediakan mekanisme approve dan transferFrom yang memungkinkan pihak ketiga untuk melakukan transfer token atas nama pemilik token dalam batas jumlah yang telah disetujui sebelumnya.  
- Pertanyaan 3: Risiko utama dalam implementasi smart contract meliputi bug pada kode, kesalahan logika, dan celah keamanan seperti reentrancy atau integer overflow. Kesalahan tersebut dapat menyebabkan kerugian aset karena smart contract bersifat tidak dapat diubah setelah dideploy.

Mitigasi risiko dapat dilakukan dengan menggunakan library standar yang telah teruji seperti OpenZeppelin, melakukan pengujian menyeluruh, serta menerapkan audit kode sebelum smart contract dideploy ke jaringan publik.  

---

## 8. Kesimpulan
Berdasarkan praktikum yang telah dilakukan, smart contract TinyCoin berbasis standar ERC20 berhasil diimplementasikan dan diuji menggunakan Remix IDE. Seluruh fungsi utama ERC20, seperti pembuatan token, pengecekan saldo, dan transfer token, dapat berjalan dengan baik sesuai dengan teori yang dipelajari. Praktikum ini menunjukkan pentingnya penggunaan standar dan library yang telah teruji untuk meminimalkan risiko keamanan dalam pengembangan smart contract.

---

## 9. Daftar Pustaka

---

## 10. Commit Log
```
week15-tinycoin-erc20
Author: Nur Fatahillah <dneth001@gmail.com>
Date:   2026-01-26

    week15-tinycoin-erc20: Proyek Kelompok – TinyCoin ERC20
```
