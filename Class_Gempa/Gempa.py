class Gempa:
    #konstraktor Inisialisasi Atribut
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
    
    #method penentu skala gempa
    def dampak(self):
        #logika statment
        if self.skala <2:
            print("Gempa tidak berasa")
        elif 2 <= self.skala <= 4: 
            print("Dampak gempa bangunan retak-retak")
        elif 4 <= self.skala <= 6:
            print("Dampak gempa banguna roboh")
        elif self.skala >6:
            print("Dampak gempa bangunan roboh dan berpotensi tsunami")

        #Menampilkan Lokasi dan Skala Gempa
        print(f"Lokasi Gempa: {self.lokasi}")
        print(f"Skala Gempa: {self.skala}")

        