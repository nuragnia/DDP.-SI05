class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    def cetak (self):
        print(f'Hewan {self.nama} Ini makanan {self.makanan}, Hewan ini juga hidup di {self.hidup} dan Berkembang biak dengan cara {self.berkembang_biak}')
#C1 = Animal('Buaya', 'Daging', 'Amphibi', 'Bertelur')
#C1.cetak() 
