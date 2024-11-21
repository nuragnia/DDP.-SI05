print("-----celcius ke fahrenheit------")
def celcius_ke_fahrenheit(celcius):
    print(celcius * 9/5 + 32)
celcius_ke_fahrenheit(0)
print()

#Soal no 2 
print("----Mencari bilangan genap----")
def is_genap(genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)
print()

#soal no 3
print("----Keterangan lulus atau tidak lulus----")
def skor(nilai):
    if nilai >= 80:
        print("lulus")
    else:
        print("Tidak Lulus")
skor(80)
skor(60)
print()

#Soal no 4
print("---Mencetak bilangan ganjil yang kurang argumen---")
def bil_ganjil(ganjil):
    for i in range(1, ganjil+1, 2):
        print(i, end=" ")
bil_ganjil(20)







