
n=int(input("masukkan nilai n:"))
if n<4 :
    print("program tidak bisa jalan ")
else:
    jumlah_boom = 0
    nilai_tengah =int((n/2)+1)
    
    for i in range (1,n+1):
        for j in range (1,n+1):
            if n % 2 == 1 and i ==nilai_tengah and j== nilai_tengah:
                print("HORE", end=" "*2)
            elif i == j :
                print(" 1 ", end=" "*3)
            elif i + j == (n + 1):
                print(" 2 ", end=" "*3)
            else:
                print("BOOM", end=" "*2)
                jumlah_boom+=1
        print( )
    print(f"jumlah boom yang muncul adalah : {jumlah_boom}")
    