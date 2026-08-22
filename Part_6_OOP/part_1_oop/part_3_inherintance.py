# Kendaraan

class Kendaraan: #ini disebut class
    merek = "default"
    _type = "default"
    __cc_mesin = "default"

    def __init__(self,merek,type_kendaraan,cc_mesin):
        self.merek = merek
        self._type = type_kendaraan
        self.__cc_mesin = cc_mesin
    
    def getProfile(self):
        print(f"Merek Kendaraan : {self.merek}")
        print(f"Type Kendaraan : {self._type}")
        print(f"CC Kendaraan : {self.__cc_mesin} HP")

    def setType(self, type_kendaraan):
        self._type = type_kendaraan

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

mobil = Mobil("Suzuki","Sedan",1600)
mobil.getProfile()