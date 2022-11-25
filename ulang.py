import array
# Define the dictionary
data = []

# Insert data into dictionary
# data = {1: ["Samuel", 21, 'Data Structures'],
# 		2: ["Richie", 20, 'Machine Learning'],
# 		3: ["Lauren", 21, 'OOPS with java'],
# 		}

def panggil():
	print("=====================================================================================")
	print("|  No  |     Nama     |     NIM     |   Tugas   |   UTS   |   UAS   |  Nilai Akhir  |");
	print("=====================================================================================");
	i=0
	for x in data:
		i+=1
		print("|  {6:2}  |  {0:10}  |  {1:9}  |  {2:7}  |  {3:5}  | {4:6}  |  {5:11.2f}  |"\
			.format (x[0][:9] , x[1][:9],x[2],x[3],x[4],x[5], i))
	print("=====================================================================================");


while True:
	Nama = input("Nama : ")
	NIM = input("NIM : ")
	Tugas = int(input("Nilai Tugas :"))
	UTS = int(input('Nilai UTS : '))
	UAS = int(input("Nilai UAS : "))
	Nilai_Akhir = float(Tugas)*30/100+(UTS)*35/100+(UAS)*35/100
	xlagi  = input("(L) Lihat , (Ta) Tambah, (U ) Update, (H) Hapus , (C) Cari , (K) Keluar = ")
	data.append([Nama, NIM, Tugas, UTS, UAS, Nilai_Akhir])

	

	if xlagi.lower() == "ta":
		print("tambahlagi :::::::")
	if xlagi.lower() == "l":
		print(data)
		panggil()
		xlagi  = input("(L) Lihat , (Ta) Tambah, (U ) Update, (H) Hapus , (C) Cari , (K) Keluar = ")

	if xlagi.lower() == "h":
		n = int(input("mau nomor berapa yg di hapus : "))
		data.pop(n)
		panggil()
		xlagi  = input("(L) Lihat , (Ta) Tambah, (U ) Update, (H) Hapus , (C) Cari , (K) Keluar = ")
	if xlagi.lower() == "u":
		nomor_u = int(input("nomor mana yang mau update = "))
		kolom_u = int(input("urutan nomor kolom  = "))
		
		if nomor_u == 0:
			nilaiganti = input ("mau di ganti apa ?  = ")
			data[nomor_u][kolom_u] = nilaiganti
			panggil()
			xlagi  = input("(L) Lihat , (Ta) Tambah, (U ) Update, (H) Hapus , (C) Cari , (K) Keluar = ")

		if nomor_u == 1:
			nilaiganti = input ("mau di ganti apa ?  = ")
			data[nomor_u][kolom_u] = nilaiganti
			panggil()
			xlagi  = input("(L) Lihat , (Ta) Tambah, (U ) Update, (H) Hapus , (C) Cari , (K) Keluar = ")

		else:
			nilaiganti = int( input ("mau di ganti apa ?  = "))
			data[nomor_u][kolom_u] = nilaiganti
			panggil()
			xlagi  = input("(L) Lihat , (Ta) Tambah, (U ) Update, (H) Hapus , (C) Cari , (K) Keluar = ")


		

	if xlagi.lower() == "k":
		break
	
	





