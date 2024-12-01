
print("___________1_____________")
print()

#Soal No. 1
angka = int(input("Masukkan bilangan bulat : "))
Ganjil = "Bilangan Ganjil"
Genap = "Bilangan Bulat"

if angka % 2 == 0:
 print ("Bilangan Genap")
else:
 print ("Bilangan Ganjil")
print()

print("___________2_____________")
print()
#Soal No. 2
Nilai_Ujian = int(input("Masukkan Nilai Ujian : "))
if Nilai_Ujian >= 75:
 print("Lulus")
else:
 print("Tidak Lulus")
print()

print("___________3______________")
print()
#Soal No. 3
Usia= int(input("Masukkan Usia : "))
if Usia >=18:
 print("Dewasa")
elif Usia <=13 and Usia <=17:
 print("Remaja")
else:
 print("Anak-Anak")
print ()

print("____________4______________")
print()
#Soal No. 4
Status_Anggota = input("Masukkan Status Anggota")
if Status_Anggota == "gold" or Status_Anggota == "silver" :
 print("Selamat Anda Mendapatkan Diskon")
elif Status_Anggota == "Bronze":
 print("Maaf Anda Tidak Mendapatkan Diskon")
else:
 print("Input Tidak Valid")
print()

print("______________5______________")
print()
#Soal No. 5
jumlahpembelian = int(input("Masukkan jumlah pembelian: "))
hargaitem = 100

if jumlahpembelian > 100:
   hargadiskon = hargaitem * jumlahpembelian * (10 / 100)
   hargatotal = hargaitem * jumlahpembelian
   total = hargatotal - hargadiskon
   print(f"Anda mendapat diskon 10%, jadi total yang harus dibayar: {total}")
else:
   total = hargaitem * jumlahpembelian
   print(f"Total yang harus dibayar adalah: {total}")