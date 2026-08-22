from Kendaraan import Kendaraan

class Motor(Kendaraan): 
    jumlah_roda = 2
    def __init_(self,merek,type_kendaraan,cc_mesin):
        super().__init(merek,type_kendaraan,cc_mesin)

    def getJumlahRoda(self):
        super().getProfile()
        print(f"Jumlah_roda : {self.jumlah_roda}")