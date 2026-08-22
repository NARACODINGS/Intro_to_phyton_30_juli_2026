karyawan = [
    {
        "nama" : "aura",
        "job" : "programer",
        "tahun_lahir" :  2000,
    },
    {
        "nama" : "naren",
        "job" : "programer",
        "tahun_lahir" :  2001,
    },
    {
        "nama" : "mahes",
        "job" : "programer",
        "tahun_lahir" :  2002,
    },
    {
        "nama" : "wara",
        "job" : "product manager",
        "tahun_lahir" :  2003,
    }
]

# void
def template_print(nama,job,usia = 3):
    print("===========================")
    print(f"Nama : {nama}")
    print(f"job : {job}")
    print(f"usia : {usia} tahun")
# non void
def rumus_usia(tahun_lahir):
    hasil = 2026 - tahun_lahir
    return hasil



template_print(karyawan[0]["nama"],karyawan[0]["job"],rumus_usia(karyawan[0]["tahun_lahir"]))
template_print(karyawan[1]["nama"],karyawan[1]["job"],rumus_usia(karyawan[1]["tahun_lahir"]))
template_print(karyawan[2]["nama"],karyawan[2]["job"],rumus_usia(karyawan[2]["tahun_lahir"]))
template_print(karyawan[3]["nama"],karyawan[3]["job"],rumus_usia(karyawan[3]["tahun_lahir"]))