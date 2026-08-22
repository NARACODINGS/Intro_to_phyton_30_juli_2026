# for
print("====== for ======")
for index in range(1,101):
    print(f"index of {index} : maaf")

print("====== for List ======")
list_makanan = ["Nasi Goreng", "Mie Goreng", "Ayam Bakar"]
for makanan in list_makanan:
    print(f"Value : {makanan}")

# While
print("====== While ======")
nomer = 101
while nomer <= 100 :
    print(f"{nomer}")
    nomer += 1

# break and continue
print("====== Break and Continue ======")
nomer = 1
while nomer <= 100:
    if nomer % 2 == 0 :
        nomer += 1
        continue # Skip 1 putaran
    print(f"index of {nomer}")
    nomer += 1
    if nomer >= 30:
        break