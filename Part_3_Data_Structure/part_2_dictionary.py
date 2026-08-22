profile = { 
    "nama_lengka" : "Aura Narendra Maheswara",
    "usia" : 22,
    "alamat" : "Bekasi",
    "job" : ["Fullsack", "Cybersecurity", " Academic", "Maestro"],
}
print(f"readl all data : {profile}")
print(f"Read data key usia : {profile["usia"]}")
print(f"Read data key cybersecurity : {profile["job"][1]}")

profile["Gaji"] = 6000000
print(f"read all data : {profile}")

profile["job"] = "Cybersecurity"
print(f"read all data : {profile}")

del profile["Gaji"]
print(f"read all data : {profile}")