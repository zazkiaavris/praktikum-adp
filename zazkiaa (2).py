print((" ")+"*kalkulator sederhana*")
perhitungan = True
while perhitungan>=0 :
    angka_pertama= int(input("masukkan angka pertama :"))
    angka_kedua = int(input("masukkan angka kedua :"))
    print("pilihan operasi")
    print("1. penjumlahan")
    print("2. pengurangan")
    print("3. perkalian")
    print("4. pembagian")
    print("5. keluar ")
    nomor_pilihan= int(input("masukkan nomor pilihan operasi (1/2/3/4/5):"))
    if nomor_pilihan == 1 :
        hasil= angka_pertama + angka_kedua
        print(f"hasilnya untuk penjumlahan adalah :{hasil}")
    elif nomor_pilihan == 2 :
        hasil = angka_pertama - angka_kedua
        print(f"hasilnya untuk pengurangan adalah :{hasil}")
    elif nomor_pilihan == 3:
        hasil = angka_pertama*angka_kedua
        print(f"hasilnya untuk perkalian adalah:{hasil}")
    elif nomor_pilihan == 4:
        if angka_kedua == 0 :
                print("tidak valid")
        else :
            hasil = angka_pertama / angka_kedua 
            print(f"hasilnya untuk pembagian adalah: {hasil}")
    else :
         print("pilihan operasi tidak valid = keluar")
    lakukan_perulangan = input("lakukan perulangan (yes/no):")
    if lakukan_perulangan == "yes" :
         print("kalkulator sederhana :") 
    else :
        print("tidak dilakukan perulangan")
        break
perhitungan = False
