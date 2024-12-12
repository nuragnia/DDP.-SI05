from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_bulu = jenis_bulu
        self.bunyi = bunyi
    def cetak(self):
        super().cetak()
        print(f'Hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi  {self.bunyi}')
print('------Cetak Burung------')
#Objek pertama
beo = Burung('burung beo', 'biji-bijian', 'udara', 'bertelur', 'blue dan orange', 'kamu jelek')
beo.cetak()
#objek kedua
print()
burung_merak = Burung('Burung Merak', 'biji-bijian', 'darat', 'bertelur',  'sangat indah', 'suara teriakan yang kencang' )
burung_merak.cetak()

