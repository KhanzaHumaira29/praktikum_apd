import os
#  Variabel Global
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
running = True

#   Prosedur 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Tekan ENTER untuk kembali.")

# Error Handling
def tidak_boleh_kosong(teks):
    if teks.strip() == "":
        raise ValueError("Input tidak boleh kosong!")
    
#   Fungsi dgn Parameter
def cek_login(username, password):
    if username in akun and akun[username]["password"] == password:
        return akun[username]["role"]
    else:
        raise KeyError("Username atau Password salah!")
    
#   Fungsi dgn parameter
def cek_no_hp(no_hp):
    return no_hp.isdigit()
    
#   Fungsi tanpa parameter
def total_tiket():
    return len(data_tiket)

#   Fungsi Rekursif (menu)
def login():
    global current_user
    clear()
    print("Silakan Login sebagai (Admin/Pengguna)")
    try:
        username = input("Masukkan Username : ")
        password = input("Masukkan Password : ")

        tidak_boleh_kosong(username)
        tidak_boleh_kosong(password)

        role = cek_login(username, password)
        current_user = username
        if role == "admin":
            menu_admin()
        else:
            menu_pengguna()
    except Exception as e:
        print(f"Error: {e}")
        login()

#   Menu Register
def register():
    clear()
    print("REGISTER NEW AKUN IKN FUN RUN 10KM")
    try:
        new_user = input("Masukkan username baru: ")
        tidak_boleh_kosong(new_user)

        if new_user in akun:
            raise KeyError("Username sudah terdaftar!")

        new_pass = input("Masukkan password: ")
        tidak_boleh_kosong(new_pass)

        akun[new_user] = {"password": new_pass, "role": "pengguna"}
        print("Akun berhasil dibuat. Silakan login terlebih dahulu untuk melihat.")
    except Exception as e:
        print(f"Error: {e}")
    pause()

#   Fungsi Tanpa Parameter
def menu_awal():
    global running
    clear()
    print("MENU AWAL SISTEM MANAJEMEN DATA E-TIKET EVENT IKN FUN RUN 10KM")
    print("1. Login (Admin/Pengguna)")
    print("2. Register Akun Baru")
    print("3. Logout")
    pilih = input("Pilih menu (1/2/3): ")

    try:
        if pilih == "1":
            login()
        elif pilih == "2":
            register()
        elif pilih == "3":
            running = False
        else:
            raise ValueError("Pilihan tidak valid.")
    except Exception as e:
        print(f"Error: {e}")
        pause()
        menu_awal()

#   Menu Admin
def tambah_tiket():
    clear()
    print("TAMBAH DATA E-TIKET IKN FUN RUN 10KM")
    try:
        id_tiket = input("Masukkan ID E-Tiket : ")
        tidak_boleh_kosong(id_tiket)

        if id_tiket in data_tiket:
            raise KeyError("ID sudah tersedia!")

        nama = input("Masukkan Nama Peserta : ")
        email = input("Masukkan Email : ")
        no_hp = input("Masukkan Nomor HP : ")
        usia = input("Masukkan Usia : ")

        data_tiket[id_tiket] = {
            "nama": nama,
            "kategori": "10KM",
            "email": email,
            "no_hp": no_hp,
            "usia": usia        
        }
        print("Data E-Tiket sukses ditambahkan.")
    except Exception as e:
        print(f"Error: {e}")
    pause()

def lihat_tiket_admin():
    clear()
    print("=" * 75)
    print("LIHAT DATA E-TIKET IKN FUN RUN 10KM".center(75))
    print("=" * 75)
    if len(data_tiket) == 0:
        print("Belum ada data E-Tiket.")
    else:
        for id_t, t in data_tiket.items():
            print(f"{id_t:<8} {t['nama']:<15} {t['kategori']:<8} {t['email']:<20} {t['no_hp']:<12} {t['usia']:<5}")
    print(f"Total E-Tiket Terdaftar: {total_tiket()}")
    pause()

def ubah_tiket():
    clear()
    print("=" * 75)
    print("UBAH DATA E-TIKET IKN FUN RUN 10KM".center(75))
    print("=" * 75)
    lihat_tiket_admin()

    try:
        id_up = input("Masukkan ID untuk e-tiket yang ingin diubah : ")
        if id_up not in data_tiket:
            raise KeyError("ID E-Tiket tidak ditemukan!")

        data_tiket[id_up]['nama'] = input("Nama baru : ")
        data_tiket[id_up]['email'] = input("Email baru : ")
        data_tiket[id_up]['no_hp'] = input("Nomor HP baru : ")
        data_tiket[id_up]['usia'] = input("Usia baru : ")
        print("Data E-Tiket sukses diubah.")
    except Exception as e:
        print(f"Error: {e}")
    pause()

def hapus_tiket():
    clear()
    print("=" * 75)
    print("HAPUS DATA E-TIKET".center(75))
    print("=" * 75)
    lihat_tiket_admin()

    try:
        id_del = input("Masukkan ID untuk e-tiket yang ingin dihapus : ")
        if id_del not in data_tiket:
            raise KeyError("ID E-Tiket tidak ditemukan.")
        
        del data_tiket[id_del]
        print("Data E-Tiket sukses dihapus.")
    except Exception as e:
        print(f"Error: {e}")
    pause()

def menu_admin():
    clear()
    print(f"MENU ADMIN MANAJEMEN DATA E-TIKET IKN FUN RUN 10KM ({current_user})")
    print("1. Tambah E-Tiket Baru (Create)")
    print("2. Lihat Data E-Tiket (Read)")
    print("3. Ubah Data E-Tiket (Update)")
    print("4. Hapus Data E-Tiket (Delete)")
    print("5. Logout Menu Admin")

    pilih = input("Pilih menu (1/2/3/4/5): ")
    
    try:
        if pilih == "1":
            tambah_tiket()
        elif pilih == "2":
            lihat_tiket_admin()
        elif pilih == "3":
            ubah_tiket()
        elif pilih == "4":
            hapus_tiket()
        elif pilih == "5":
            return
        else:
            raise ValueError("Pilihan menu tidak valid.")
    except Exception as e:
        print(f"Error: {e}")
    clear()
    menu_admin()

#   Menu Pengguna
def lihat_tiket_saya():
    clear()
    print("=" * 75)
    print(f"DATA E-TIKET IKN FUN RUN 10KM ATAS NAMA : {current_user}".center(75))
    print("=" * 75)
    ada = False
    print(f"{'ID':<8} {'Nama':<16} {'Kategori':<8} {'Email':<16} {'Usia':<8} {'No HP':<16}")
    for id_t, v in data_tiket.items():
        if v['nama'] == current_user:
            ada = True
            print(f"{id_t:<8} {v['nama']:<16} {v['kategori']:<8} {v['email']:<16} {v['usia']:<8} {v['no_hp']:<16}")
    if not ada:
        print("Belum ada e-tiket atas nama Anda.")
    pause()

def daftar_tiket_baru():
    clear()
    print("DAFTAR E-TIKET BARU")
    try:
        new_id = "IKN" + str(len(data_tiket) + 1).zfill(2)
        email = input("Email : ")
        no_hp = input("No HP : ")
        if not cek_no_hp(no_hp):
            raise ValueError("Nomor HP harus angka!")
        usia = input("Usia : ")

        data_tiket[new_id] = {
            "nama": current_user,
            "kategori": "10KM",
            "email": email,
            "no_hp": no_hp,
            "usia": usia
        }
        print(f"E-Tiket dengan id {new_id} sukses didaftarkan.")
    except Exception as e:
        print(f"Error: {e}")
    pause()

def menu_pengguna():
    clear()
    print(f"MENU PENGGUNA E-TIKET IKN FUN RUN 10KM({current_user})")
    print("1. Lihat E-Tiket Saya")
    print("2. Daftar E-Tiket Baru")
    print("3. Logout Menu Pengguna")
    pilih = input("Pilih menu (1/2/3) : ")

    try:
        if pilih == "1":
            lihat_tiket_saya()
        elif pilih == "2":
            daftar_tiket_baru()
        elif pilih == "3":
            return
        else:
            raise ValueError("Pilihan menu tidak valid.")
    except Exception as e:
        print(f"Error: {e}")
    clear()
    menu_pengguna() 

while running:
    menu_awal()

clear()
print("Yeay, terimakasih sudah berkunjung:)")