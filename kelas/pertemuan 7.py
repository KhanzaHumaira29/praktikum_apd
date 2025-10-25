# #   Membuat Prosedur
# def pesan_halo():
#     print('Halo Akademik!')
#     print('Indonesia')

# pesan_halo()

# def segitiga(alas, tinggi):
#     luas = 1/2* alas * tinggi
#     print(luas)

# segitiga()


# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# def volume_balok(luas):
#     volume = luas_persegi(sisi)*sisi
#     print(volume)

# volume_balok(4)

# def pertambahan():
#     hasil=x+3
#     print(hasil)

# pertambahan(3)

# Variabel global untuk menyimpan data Film
film = []
# Fungsi untuk menampilkan semua data
def show_data():
    if len(film) <= 0:
        print("Belum Ada data")
    else:
        print("ID | Judul Film")
        for indeks in range(len(film)):
            print(indeks, "|", film[indeks])