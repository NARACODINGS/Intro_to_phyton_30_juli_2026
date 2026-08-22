from Kendaraan import Kendaraan
from Mobil import Mobil
from Motor import Motor

def getProfile(jenis_kendaraan):
    jenis_kendaraan.getProfile()

if __name__ == "__main__":
    mobil = Mobil("Suzuki","Sedan",1600)
    motor = Motor("Kawasaki","H2",1000)

    getProfile(mobil)
    print("===================")
    getProfile(motor)