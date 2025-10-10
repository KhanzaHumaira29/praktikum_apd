# Membuat list didalam list
list_random = [76, 'Nama', 'NIM', ['Indonesia', 'Laos', 'Jepang']]

print(list_random)
print(list_random[-1][2])

# Menambahkan list
list_random.append('bang Ahnaf')
print(list_random)

# Menambah ke dalam index tertentu
list_random.insert(2, ['Samarinda', 'Balikpapan'])
print(list_random)

# Mengubah elemen pada list
studyclub = ["Data Science", "Robotics",['Indonesia', 'Malay', 'Jerman'], "Multimedia", "Network"]
print('Awal mula',studyclub)
studyclub [0] = 'AI dan Publikasi Ilmiah'
print('Awal selanjutnya',studyclub)
print('')

# pop dan del
studyclub.pop(1)
print(studyclub)

del studyclub[3]
print(studyclub)

# remove
matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
print(matakuliah)

matakuliah.remove('APD')
print('Akhir', matakuliah)

praktikum = ["Mahasiswa", 20, True, 45.10, ["APD", 25]]
praktikum[4].pop(0)
print(praktikum)

# start : stop : step

print(praktikum[0:4:3])
# supaya gak kelihatan kurung siku
for item in praktikum[0:4:3]:
    print(item)

print(len(praktikum))



# perkalian
maha=[1,4,7,6,8]
hasil=maha*4
print(hasil)

for i in maha:
    print(i*3)

# Membuat nested list
kelas = [
["Ridho", "Lian", "Nabil"],
["Daffa", "Dante", "Santoso"],
["Pernanda", "Riyadi", "Ahnaf"],
]
print(kelas[0][1])

# Tuple
anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
print(anggota)

anggota=tuple(anggota)
print(anggota)

# beri variabel setiap values
tugas = ('rangkuman', 'arduino','scrapping')
(PTI, orsikom, basisdata) = tugas
print(PTI)
print(orsikom)
print(basisdata)
