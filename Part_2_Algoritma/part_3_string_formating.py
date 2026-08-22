import datetime
tanggal = datetime.datetime.now()
manager = "Aura Narendra Maheswara"
pt = "PT. Semua Mahir teknologi"

print("==========")
print("Tanggal {0}\nYTH.{1}\n{2}".format(tanggal,pt,manager)) #Bisa Terbalik
print("==========")
# Keyword Argument
print("Tanggal : {tanggal}\nYTH.{manager}\n{pt}".format(tanggal=tanggal,pt=pt,manager=manager)) #Terlalu Banyak
print("==========")
# Cara simpel
print(f"Tanggal : {tanggal}\nYTH.{manager}\n{pt}")
print("==========")