# Nilai siswa
nilai = 80

# id statement
# if (Kondisi):
    #perintah yang akan kamu lakukan  sesuai dengan kondisi
print( "=====IF STATEMENT=====")
if nilai > 80:
    print("Selamat Anda Lulus")
print("=====IF else STATEMENT=====")
if nilai > 80:
    print("Selamat Anda Lulus")
else:
    print("Maaf Anda Tidak Lulus")
print("=====If elif else STATEMENT=====")
if nilai > 91 and nilai <= 100:
    print("Selamat Anda Mendapat Nilai A")
elif nilai > 81 and nilai <= 90:
    print("Selamat Anda Mendapat Nilai B")
elif nilai > 71 and nilai <= 80:
    print("Selamat Anda Mendapat Nilai c")
else:
    print("Maaf Anda Tidak Lulus")
print("=====IF Nested STATEMENT=====") # Tidak Disarankan | Setelah IF bisa IF lagi
if nilai >= 80 :
    # Program
    # Program
    if nilai < 90 : 
        print("Selamat Anda Mendapatkan Nilai B")
    else:
        print("Selamat Anda Mendapatkan Nilai A")
print("=====If Tenary STATEMENT=====") # Tidak di sarankan | Lebih FIX/Singkat
# (Kondisi) ? (Jika Jondisi True) : (Jika Kondisi False)
hasil = "Selamat anda lulus" if nilai >80 else "Maaf anda tidak lulus"
print(hasil)

print("======= Match Statement =======")
print("======Menu======")
print("1. Menu Makanan")
print("2. Menu Minuman")
select = int(input("Pilih Menu : "))
match select:
    case 1:
        print("Anda memilih menu makanan")
    case 2:
        print("Anda memilih menu minuman")
    case _:
        Print("Pilihan Invalid")


#print("=====Penggunaan OR=====")
#if nilai < 70 or nilai < 100: # Salah satu harus terpenuhi
    #print("Selamat Anda Lulus")
#print("=====Penggunaan AND=====")
# Buat nilai >70
#if nilai > 70 or nilai < 100: # Dua-duanya harus terpenuhi
    #print("Selamat Anda Lulus")