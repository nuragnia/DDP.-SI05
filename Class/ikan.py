from Animal import *

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_ikan = warna_ikan
        self.jenis_ikan = jenis_ikan
    def cetak(self):
        super().cetak()
        print(f'warna ikan ini dalah{self.warna_ikan} dan hewan ini jenis ikan{self.jenis_ikan}')
print('-----Cetak Ikan-----')
hiu = ikan('ikan hiu', 'daging', 'air', 'bertelur dan beranak', 'abu-abu', 'ikan air laut')
hiu.cetak()
#objek kedua
cupang = ikan('ikan cupang', 'pelet ikan cupang', 'air', 'bertelur', 'warna-warni', 'ikan air tawar')
cupang.cetak()

