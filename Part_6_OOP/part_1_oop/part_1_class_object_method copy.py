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


mobil = Kendaraan("Suzuki","Sedan",1600)

mobil.getProfile()