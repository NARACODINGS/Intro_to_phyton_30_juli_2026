from Kendaraan import Kendaraan

class Mobil(Kendaraan): 
    jumlah_roda = 4
    def __init_(self,merek,type_kendaraan,cc_mesin):
        super().__init(merek,type_kendaraan,cc_mesin)

    #def getJumlahRoda(self):
    #    print(f"Jumlah_roda : {self.jumlah_roda}")
    #Teknik Override
    def getJumlahRoda(self):
        super().getProfile()
        print(f"Jumlah_roda : {self.jumlah_roda}")