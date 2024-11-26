nama: teguh Praditya_F55123046

analisis best case untuk kuis 2
1. naive bayes:
   Best case untuk program ini terjadi ketika ukuran daftar bilangan yang diproses kecil dan elemen-elemen dalam daftar sudah terdistribusi sedemikian rupa sehingga mempermudah
   pembagian kategori. Pada kasus terbaik, iterasi untuk menentukan kategori dapat dioptimalkan, misalnya jika semua bilangan yang lebih kecil atau sama dengan ambang batas
   berada di awal daftar, sehingga program dapat berhenti lebih cepat setelah menemukan elemen pertama dari kategori kedua. Proses penghitungan probabilitas tetap memerlukan
   iterasi penuh terhadap daftar, tetapi dengan jumlah elemen yang sedikit, komputasi ini tetap efisien. Selain itu, pengacakan bilangan dengan `random.shuffle` memiliki
   kompleksitas \(O(n)\), yang tidak berubah dalam best case. Dengan demikian, total kompleksitas waktu untuk best case adalah \(O(n)\), yang mencakup pengacakan, pembagian
   kategori, dan penghitungan probabilitas. Program ini bekerja optimal pada daftar kecil dengan struktur data yang memungkinkan iterasi cepat pada kategori.
2. divide and concuer:
   Best case untuk program ini terjadi dalam skenario ketika daftar bilangan memiliki panjang \( n = 1 \), sehingga langsung memenuhi kondisi dasar rekursi tanpa perlu
   melakukan pembagian lebih lanjut. Pada kondisi ini, fungsi hanya memeriksa elemen tunggal dalam daftar dan langsung mengembalikannya sebagai nilai maksimum, dengan
   kompleksitas waktu \( O(1) \). Secara umum, metode yang digunakan adalah *Divide and Conquer*, yang membagi daftar menjadi dua bagian hingga ukuran setiap subdaftar
   mencapai 1. Setiap pemanggilan rekursif melibatkan pembagian daftar dan penggabungan hasil maksimum dari kedua subdaftar. Namun, pada best case (daftar ukuran 1), tidak ada
   operasi pembagian atau penggabungan yang diperlukan, sehingga waktu eksekusi adalah yang paling cepat. Dengan demikian, program ini memiliki efisiensi optimal dalam
   skenario daftar bilangan berukuran kecil atau saat elemen maksimum terletak di awal subdaftar pertama yang diperiksa.
