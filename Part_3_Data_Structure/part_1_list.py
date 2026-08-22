# CRUD
# C Create
# Inisialisasi Data
makanan = ["Nasi Goreng", "Mie Goreng", "Ayam Bakar"]
# R Read
print(f"Read all data : {makanan}")
print(f"Read data in index 1 : {makanan[1]}")
print(f"Read data in index -1 : {makanan[-1]}")
# U Update
# append manambahkan data di akhir list
makanan.append("Sate Ayam")
print(f" Real all data : {makanan}")
# Update data
makanan[1] = "Mie Rebus"
print(f" Real all data : {makanan}")
# D Delete
del makanan[0]
print(f"Read all data : {makanan}")

# Inilah yang dinamakan tipe data dinamis