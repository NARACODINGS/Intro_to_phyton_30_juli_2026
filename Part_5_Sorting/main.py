import random

def generate_random_number(jumlah_data:int):
    data = []
    for value in range (jumlah_data):
        value = random.randint(1,100)
        data.append(value)
    return data

def bubble_sorting(data:list):
    jumlah_data = len(data)
    for index in range(jumlah_data):
        for value in range(0,jumlah_data - index - 1):
            if data[value] > data[value + 1]: # Kecil ke besar (ASC) (>) # Besar ke kecil (DEC) (<)
                temp = data[value]
                data[value] = data[value + 1]
                data[value + 1] = temp

def selection_sorting(data:list):
    jumlah_data = len(data)
    for index in range(jumlah_data):
        min_index = index
        for value in range(index + 1 , jumlah_data):
            if data[value] < data[value + 1]:
                min_index = value
    data[index],data[min_index] = data[min_index],data[index]

def insert_sorting(data:list):
    for index in range(1,len(data)):
        min_value = data[index]
        value = index - 1
        while value >= 0 and min_value < data[value]:
            data[value + 1]= data[value]
            value -= 1
        
        data[value + 1] = min_value

def merge_sorting(data:list):
    if len(data) > 1:
        nilai_tengah = len(data) // 2
        data_kiri = data[:nilai_tengah]
        data_kanan = data [nilai_tengah:]

        merge_sorting(data_kiri)
        merge_sorting(data_kanan)

        index = value = real_index = 0

        while index < len(data_kiri) and value < len(data_kanan):
            if data_kiri[index] < data_kanan[value]:
                data[real_index] = data_kiri[index]
                index += 1
            else:
                data[real_index] =  data_kanan[value]
                value += 1

            real_index +=1

        while index < len (data_kiri):
            data[real_index] = data_kiri[index]
            index += 1
            real_index += 1
        while value < len(data_kanan):
            data[real_index] = data_kanan[value]
            value += 1
            real_index += 1

if __name__ == "__main__":
    try: # di gunakan untum mengatasi atau memperkirakan kalau code ini akan error
        jumlah_data= int(input("Masukan jumlah data yang akan di generate : "))
    except ValueError:
        print("Invalid Input Type")
        exit(1)

    data = generate_random_number(jumlah_data)
    print("========== Random Number List ==========")
    print(data)
    input("==== Press Enter to next area ====")
    # Algoritma
    #bubble_sorting(data)
    #selection_sorting(data)
    #insert_sorting(data)
    #merge_sorting(data)
    print(data)