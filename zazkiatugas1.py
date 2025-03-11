paket_makanan = {
    1: "ayam = Rp20000",
    2: "sapi = Rp35000",
    3: "cumi-cumi = Rp45000"
}
print(f"pilih paket makanan = {paket_makanan} ")

pilihan = int(input("masukkan nomor paket yang ingin di pesan : "))
jarak_rumah = float(input("masukkaan jarak rumah ke restoran : "))
if jarak_rumah <= 1 :
    ongkir = 0
elif 1 <= jarak_rumah <= 3 :
    ongkir = 7000
else :
    ongkir = 15000
harga_paket = [20000 , 35000 , 45000] [pilihan -1]
total_biaya = harga_paket + ongkir

print(f"total biaya yang perlu di bayar = {total_biaya}")
