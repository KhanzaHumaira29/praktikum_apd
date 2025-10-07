#   Form Login
username_benar = "khanza"
password_benar = "065"
login_berhasil = False
while not login_berhasil: # Selama login masih belum 
    username = input("Silakan masukkan username:")
    password = input("Silakan masukkan password:")

    #   Penanganan untuk input kosong
    if username == "" or password == "":
        print("Input tidak boleh kosong!")
    elif username != "khanza" and password != "065":
        print("Username dan password salah!")
    elif username != "khanza":
        print("Hanya username yang salah!")
    elif password != "065":
        print("Hanya password yang salah!")
    else:
        print("Login berhasil.")
        login_berhasil = True   # keluar dari while

#   Input golongan darah dan rhesus
ulang = "Y"

#   Variabel total darah
total_A_positif = 0
total_A_negatif = 0
total_B_positif = 0
total_B_negatif = 0
total_AB_positif = 0
total_AB_negatif = 0
total_O_positif = 0
total_O_negatif = 0

while ulang == "Y":
    golongan = input("Masukkan golongan darah Anda (A/B/AB/O): ")

    if golongan == "A":
        rhesus = input("Masukkan rhesus Anda (+/-): ")
        if rhesus == "+":
            total_A_positif += int(input("Masukkan jumlah kantong darah: ")) * 500
        elif rhesus == "-":
            total_A_negatif += int(input("Masukkan jumlah kantong darah: ")) * 500
        else:
            print("Rhesus tidak valid!")

    elif golongan == "B":
        rhesus = input("Masukkan rhesus Anda (+/-): ")
        if rhesus == "+":
            total_B_positif += int(input("Masukkan jumlah kantong darah: ")) * 500
        elif rhesus == "-":
            total_B_negatif += int(input("Masukkan jumlah kantong darah: ")) * 500
        else:
            print("Rhesus tidak valid!")

    elif golongan == "AB":
        rhesus = input("Masukkan rhesus Anda (+/-): ")
        if rhesus == "+":
            total_AB_positif += int(input("Masukkan jumlah kantong darah: ")) * 500
        elif rhesus == "-":
            total_AB_negatif += int(input("Masukkan jumlah kantong darah: ")) * 500
        else:
            print("Rhesus tidak valid!")

    elif golongan == "O":
        rhesus = input("Masukkan rhesus (+/-): ")
        if rhesus == "+":
            total_O_positif += int(input("Masukkan jumlah kantong darah: ")) * 500
        elif rhesus == "-":
            total_O_negatif += int(input("Masukkan jumlah kantong darah: ")) * 500
        else:
            print("Rhesus tidak valid!")
    else:
        print("Golongan darah tidak valid!")

    ulang = input("Apakah Anda ingin input lagi? (Y/T): ")

# OUTPUT RINGKASAN (Poin Plus)
print("RINGKASAN DATA DARAH")
print("=======================================")
print(">> Golongan Darah A:")
print("   A+ :", total_A_positif, "ml")
print("   A- :", total_A_negatif, "ml")
print("   Total A :", total_A_positif + total_A_negatif, "ml")

print(">> Golongan Darah B:")
print("   B+ :", total_B_positif, "ml")
print("   B- :", total_B_negatif, "ml")
print("   Total B :", total_B_positif + total_B_negatif, "ml")

print(">> Golongan Darah AB:")
print("   AB+:", total_AB_positif, "ml")
print("   AB-:", total_AB_negatif, "ml")
print("   Total AB:", total_AB_positif + total_AB_negatif, "ml")

print(">> Golongan Darah O:")
print("   O+ :", total_O_positif, "ml")
print("   O- :", total_O_negatif, "ml")
print("   Total O :", total_O_positif + total_O_negatif, "ml")
print("=======================================")

# Hitung total keseluruhan semua darah
total_semua = (
    total_A_positif + total_A_negatif +
    total_B_positif + total_B_negatif +
    total_AB_positif + total_AB_negatif +
    total_O_positif + total_O_negatif
)
print(f"Total keseluruhan darah yang terkumpul: {total_semua} ml")