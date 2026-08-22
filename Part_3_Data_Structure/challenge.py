n = 5

# ==========================
# PERSEGI
# ==========================
print("PERSEGI")

for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

print()

# ==========================
# SEGITIGA KIRI BAWAH
# ==========================
print("SEGITIGA KIRI BAWAH")

for i in range(n):
    for j in range(n):
        if j <= i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print()

# ==========================
# SEGITIGA KIRI ATAS
# ==========================
print("SEGITIGA KIRI ATAS")

for i in range(n):
    for j in range(n):
        if j < n - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print()

# ==========================
# SEGITIGA KANAN BAWAH
# ==========================
print("SEGITIGA KANAN BAWAH")

for i in range(n):
    for j in range(n):
        if j < n - i - 1:
            print(" ", end="")
        else:
            print("*", end="")
    print()

print()

# ==========================
# SEGITIGA KANAN ATAS
# ==========================
print("SEGITIGA KANAN ATAS")

for i in range(n):
    for j in range(n):
        if j < i:
            print(" ", end="")
        else:
            print("*", end="")
    print()