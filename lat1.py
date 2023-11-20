import os

#fungsi ascending
def urutasc(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                simpan=a[j]
                a[j]=a[j+1]
                a[j+1]=simpan
    print(a)
    
#fungsi Descending
def urutdesc(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]<a[j+1]:
                simpan=a[j]
                a[j]=a[j+1]
                a[j+1]=simpan
    print(a)



while(True):
    os.system('cls')

    print("Program Mengurutkan Angka")
    print("Menggunakan Bubble Short")

    a = int(input("Masukan Angka 1 : "))
    b = int(input("Masukan Angka 2 : "))
    c = int(input("Masukan Angka 3 : "))
    d = int(input("Masukan Angka 4 : "))
    e = int(input("Masukan Angka 5 : "))
    f = int(input("Masukan Angka 6 : "))
    g = int(input("Masukan Angka 7 : "))
    h = int(input("Masukan Angka 8 : "))
    i = int(input("Masukan Angka 9 : "))
    j = int(input("Masukan Angka 10 : "))

    print('----------------------------------')
    print('Pilih Metode Pengurutan :')
    print('1.Ascending')
    print('2.Descending')

    bil = [a,b,c,d,e,f,g,h,i,j]
    maks = max(bil)
    mines = min(bil)
    rata = sum(bil)/len(bil)

    pilih = input("Metode yang dipilih : ")
    print('----------------------------------')

    print('Data sebelum diurutkan : ')
    print(bil)
    print('Nilai Maksimal : ',maks)
    print('Nilai Minimal : ',mines)
    print('Nilai Rata-rata : ',rata)

    print('Data setelah diurutkan  : ')

    if pilih=="1":
        urutasc(bil)
    elif pilih=="2":
        urutdesc(bil)
    else:
        print("Pilihan Tidak Ada")
        

    menu = input("Ingin Melanjutkan(Y/N)? ")


    if menu=="Y" or "y":
        continue
    
    elif menu=="n" or "N":
        print("Terimakasih")
        break
    
    else:
        print("Pilihan Tidak Ada")
        break
