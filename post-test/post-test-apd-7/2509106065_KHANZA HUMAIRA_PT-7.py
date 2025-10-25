import os
os.system('cls' if os.name == 'nt' else 'clear')

#   Variabel Global
akun = { 
    "khanza" : {"password": "065", "role": "admin"},
    "ghina" : {"password": "ghina01", "role": "pengguna"},
    "van" : {"password": "van02", "role": "pengguna"},
    "rumay" : {"password": "rumay03", "role": "pengguna"}
}
data_tiket = {
    "IKN01": {"nama": "ghina", "kategori": "10KM", "email": "ghina@gmail.com", "no_hp": "0812345678", "usia": "18"},
    "IKN02": {"nama": "van", "kategori": "10KM", "email": "van@gmail.com", "no_hp": "0898766541", "usia": "22"},
    "IKN03": {"nama": "rumay", "kategori": "10KM", "email": "rumay@gmail.com", "no_hp": "0835754632", "usia": "12"}
}

current_user = ""

#   Fungsi Parameter
def cek_login(username,password):
    if username in akun and[username]["password"] == password:
        return akun[username]["role"]
    raise ValueError("Username atau Password salah.")

#   Fungsi tanpa Parameter
def generate_id():
    return "IKN" + str (len(data_tiket) + 1).zfill(2)

#   Prosedur ke-1
def menu_admin():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print("MENU ADMIN E-TIKET EVENT IKN FUN RUN 10KM".center(60))
        print("=" * 60)
        print("1. Tambah E-Tiket Baru (Create)")
        print("2. Lihat Data E-Tiket (Read)")
        print("3. Ubah Data E-Tiket (Update)")
        print("4. Hapus Data E-Tiket (Delete)")
        print("5. Logout")
        menu_admin = input("Masukkan pilihan (1/2/3/4/5): ")

        if menu_admin == "1":
            id_tiket = input("Masukkan ID E-Tiket: ")
            if id_tiket in data_tiket:
                print("ID E-Tiket sudah tersedia!")
            else:
                nama = input("Nama Peserta: ")
                kategori = "10KM"
                email = input("Email: ")
                no_hp = input("Nomor HP: ")
                usia = input("Usia: ")
                data_tiket[id_tiket] = {"nama": nama, "kategori": kategori, "email": email, "no_hp": no_hp, "usia": usia}
                print("Data E-Tiket berhasil ditambahkan.")
            input("Tekan ENTER untuk kembali.")
        
        elif menu_admin == "2":
            print(f"{'ID':<8} {'Nama':<15} {'Kategori':<8} {'Email':<20} {'No HP':<12} {'Usia':<5}")
            for id_tiket, t in data_tiket.items():
                print(f"{id_tiket:<8} {t['nama']:<15} {t['kategori']:<8} {t['email']:<20} {t['no_hp']:<12} {t['usia']:<5}")
            input("Tekan ENTER untuk kembali.")