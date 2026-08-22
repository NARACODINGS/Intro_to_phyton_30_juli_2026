file = open("../Create/pesan_rahasia.txt","r")
# Read all
lines = file.read()
print("======List Test======")
print(lines)
print("=======Read 1 Line========")
file.seek(0)
for line in file.readlines():
    print(line.strip())
    break