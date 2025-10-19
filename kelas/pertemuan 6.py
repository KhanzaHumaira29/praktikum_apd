list_Mahasiswa = ["Andi", "Budi", "Citra", "Dewi"]
print("Nama Anda", list_Mahasiswa[0])

set_Makanan = {"nasi", "nasi", "ayam", "sayur", "buah"}
set_Makanan2= {"nasi", "ayam", "ikan", "telur"}
print("Makanan favorit saya adalah", set_Makanan)

set_Minuman = {"air", "Jus", "susu", "teh"}
for minum in set_Minuman:
    print("Minuman saya adalah", minum)

set_All = set_Makanan.union(set_Minuman)
print(set_All)

#   Mencari yang ada di tengah
set_Sama = set_Makanan.intersection(set_Makanan2)
print("ini yang sama",set_Sama)

set_Update = set_Makanan.update(set_Makanan)
print("ini setelah di update",set_Makanan)

Nilai = {
"Matematika": 80,
"B. Indonesia": 90,
"B. Inggris": 81,
"Kimia": 78,
"Fisika": 80
}

# Menggunakan items()
for i, j in Nilai.items():
    print(f"Nilai {i} anda adalah {j}")

Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}
print(Film)
Film["Zombieland"] = "Comedy"
Film.update({"Hours" : "Thriller"})
#Setelah Ditambah
print(Film)

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81
}
print(Nilai)
print("")
#menggunakan setdefault
print("Nilai : ", Nilai.setdefault("Kimia", 70))
print("")
#setelah menggunakan setdefault
print(Nilai)

Musik = {
"The Chainsmoker" : ["All we Know", "The Paris"],
"Alan Walker" : ["Alone", "Lily"],
"Neffex" : ["Best of Me", "Memories"]
}
for i, j in Musik.items():
    print(f"Musik milik {i} adalah : ")
    for song in j:
        print(song)
    print("")