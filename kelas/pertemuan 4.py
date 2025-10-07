ulangi = 10
for i in range (ulangi):
    print(f'Perulangan ke {i}')

#Contoh penggunaan For pada List
simpan = [1, 'Dapupu', 4.00, True]
for i in simpan:
    print (i) 

#Contoh penggunaan Nested for
for i in range (1, 4):  #Mengontrol baris dalam tabel perkalian
    for j in range (1, 5):  #Mengontrol kolom dalam tabel perkalian
        print(f'{i} x {j} = {i*j}')
    print('')   #Memberi jarak antar baris  

#Contoh penggunaan While
jawab = 'ya'
hitung = 0
while (jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi?")
print(f"total perulangan : {hitung}")

username = input("Masukkan username : ")
while username == "":
    username = input("Masukkan username : ")

#Contoh penggunaan Break
angka = [2, 5, 8, 12, 15, 7, 20]

print("Mencari angka lebih besar dari 10...")

for n in angka:
    print(f"Sekarang memeriksa angka: {n}")
    if n > 10:
        print(f"Angka {n} lebih besar dari 10, perulangan berhenti.")
        break

print("program selesai.")