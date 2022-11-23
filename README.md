# Praktikum_4
## Membuat Program Sederhana Menambah Data ke Dalam Sebuah List
1. Program meminta memasukkan data sebanyak-banyaknya (gunakan perulangan)
2. Tampilkan pertanyan untuk menambah data (y/t?), apabila menjawab tidak maka menampilkan daftar datanya
3. Nilai akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, dan uas: 35%)
4. Buat flowchart dan penjelasannya pada README.md
5. Commit dan push repository ke github
## Flowchart
![image](https://user-images.githubusercontent.com/115929351/203556776-16b294b1-793c-4209-adc3-82e87471e7db.png)

Penjelasan Flowchart
1. Mulai
2. Dimulai dengan meng-input data, (Nama, NIM, Nilai)
3. Data akan diproses dari ketiga komponen nilai tersebut untuk menghitung rata-rata nilai
4. Keputusan akan menanyakan untuk tambah data (ya/tidak), jika memilih (ya) maka data akan naik ke atas kembali untuk diproses rata-rata nilai akhirnya
5. Jika (tidak), maka data akan stop dan menampilkan daftar datanya
6. Hasil output tampilan daftar datanya dan menampilkan rata-rata nilai akhirnya (List Nama, NIM, Nilai, Rata-rata nilai akhir)
7. Selesai
## Step by Step
![ini yg bener](https://user-images.githubusercontent.com/115929351/203557019-605520fd-0c07-46a3-9f44-2141482c2b4b.png)
1. Membuat codingan input string (Nama, NIM, Tugas, UTS, UAS, Nilai Akhir)
2. Memakai statement float utnuk nilai akhir agar bilangan menjadi koma, dan komponen penilaian yang usdah ditentukan tugas
3. Memakai statement data.append untuk menambahkan data dari variabel diatas
3. Menginput data jika "tambah lagi" memakai statement if,dan lower untuk penulisan huruf kecil
4. Membuat tampilan list yag terdiri dari (No, Nama, NIM, Tugas, UTS, UAS, Nilai Akhir)
5. Menggunakan statement for untuk mengulang data yang disimpan di awal, kemudian data tersebut dikeluarkan dan bertambah 1
6. Membuat index untuk urutan posisi per data
![tikum4](https://user-images.githubusercontent.com/115929351/203560213-42e2800b-9229-4a82-ae87-b67959a72fc3.png)
Ini adalah hasil output membuat program sederhana memasukkan data ke dalam list, terlihat banyaknya data yang dimasukkan ke dalam list bisa melebihi 2 atau sebanyak-banyaknya dengan menggunanakan append
## Latihan Membuat, Mengubah dan Menambah List
![ye](https://user-images.githubusercontent.com/115929351/203562424-c56c03b5-30a3-43e2-9107-b669747674e6.png)
Step by step membuat list sebanyak 5 elemen dengan nilai bebas
1. Menampilkan semua elemen pada variabel a
2. Menampilkan elemen ketiga pada variabel a
3. Menampilkan elemen ke 2 sampai dengan 4 pada variabel a
4. Menampilkan elemen terakhir pada variabel a

Step by step mengubah list dengan nilai bebas
1. Mengubah elemen ke 4 pada variabel a
2. Menampilkan elemen ke 4 yang sudah diubah nilainya
3. Mengubah elemen ke 4 sampai ke elemen terakhir
4. Menampilkan elemen ke 4 sampai elemen terakhir

Step by step tambah elemen list
1. Mengambil 2 bagian dari list pertama (a) dan list kedua (b)
2. Menambah list dengan nilai string dengan append
3. Menambah list (b) dengan 3 nilai dengan extend
4. Menggabungkan nilai list (a) dan list (b) dan menampilkan hasil list (c)
![terbaru list](https://user-images.githubusercontent.com/115929351/203563963-e390751d-5acc-4a82-9b12-fd1bd5d9a0f2.png)
Ini adalah hasil output dari membuat, mengubah serta menambah list dengana elemen sebanyak-banyaknya
