from Animal import *

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bisa, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_bisa = jenis_bisa
        self.warna = warna
    def cetak(self):
        super().cetak()
        print(f'hewan ini memiliki bisa{self.jenis_bisa} dan memiliki warna{self.warna}')
print('-----Cetka Ular-----')
piton = ular('ular piton','mamalia kecil', 'darat', 'bertelur', 'tidak berbisa', 'cokelat, hijau, dan kuning')
piton.cetak()
print()
anakonda  = ular('ular anakonda', 'daging', 'darat', 'bertelur', 'tidak berbisa', 'hijau,hitam,kuning keemasan')
anakonda.cetak()