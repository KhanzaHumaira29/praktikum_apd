import os
os.system('cls' if os.name == 'nt' else 'clear')

#   Data Akun (default)
akun = { 
    "khanza" : {"password": "065", "role": "admin"},
    "ghina" : {"password": "ghina01", "role": "pengguna"},
    "van" : {"password": "van02", "role": "pengguna"},
    "rumay" : {"password": "rumay03", "role": "pengguna"}
}

#   Data E-Tiket (default)
data_tiket = {
    "IKN01": {"nama": "ghina", "kategori": "10KM", "email": "ghina@gmail.com", "no_hp": "0812345678", "usia": "18"},
    "IKN02": {"nama": "van", "kategori": "10KM", "email": "van@gmail.com", "no_hp": "0898766541", "usia": "22"},
    "IKN03": {"nama": "rumay", "kategori": "10KM", "email": "rumay@gmail.com", "no_hp": "0835754632", "usia": "12"}
}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*60)
    print("SISTEM MANAJEMEN DATA E-TIKET EVENT IKN FUN RUN 10KM".center(60))
    print("="*60)
    print("Terdapat 3 pilihan untuk mengakses data e-tiket:")
    print("1. Login")
    print("2. Register Akun Baru Saja")
    print("3. Logout")
    menu_awal = input("Silakan pilih menu(1/2/3): ")
    
    #   Menu Awal Login
    if menu_awal == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN MANAJEMEN DATA E-TIKET IKN FUN RUN 10KM ===")
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        if username in akun and akun[username]["password"] == password:
            role = akun[username]["role"]
        else:
            print("Username atau password salah!")
            input("Tekan ENTER untuk kembali ke menu awal...")
            continue

        #   Menu Admin
        if role == "admin":
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

                #   Create
                if menu_admin == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== TAMBAH DATA E-TIKET ===")
                    id_tiket = input("Masukkan ID E-Tiket: ")
                    if id_tiket in data_tiket:
                        print("ID E-Tiket sudah ada, gunakan ID lain!")
                    else:
                        nama = input("Masukkan Nama Peserta: ")
                        kategori = "10KM"
                        email = input("Masukkan Email: ")
                        no_hp = input("Masukkan Nomor HP: ")
                        usia = input("Masukkan Usia Peserta: ")
                        data_tiket[id_tiket] = {
                            "nama": nama,
                            "kategori": kategori,
                            "email": email,
                            "no_hp": no_hp,
                            "usia": usia
                        }
                        print("Data E-Tiket berhasil ditambahkan!")
                    input("Tekan ENTER untuk kembali...")

                #   Read
                elif menu_admin == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=" * 75)
                    print("DAFTAR DATA E-TIKET EVENT IKN FUN RUN 10KM".center(75))
                    print("=" * 75)
                    if len(data_tiket) == 0:
                        print("Belum ada data E-Tiket tersedia.")
                    else:
                        print(f"{'ID':<8} {'Nama':<15} {'Kategori':<8} {'Email':<20} {'No HP':<12} {'Usia':<5}")
                        print("-" * 75)
                        for id_tiket, t in data_tiket.items():
                            print(f"{id_tiket:<8} {t['nama']:<15} {t['kategori']:<8} {t['email']:<20} {t['no_hp']:<12} {t['usia']:<5}")
                    input("Tekan ENTER untuk kembali...")

                #   Update
                elif menu_admin == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== UBAH DATA E-TIKET ===")
                    id_update = input("Masukkan ID E-Tiket yang ingin diperbarui: ")
                    if id_update in data_tiket:
                        print(f"Kategori (tidak dapat diubah): {data_tiket[id_update]['kategori']}")
                        print("-" * 50)
                        data_tiket[id_update]['nama'] = input("Nama baru        : ")
                        data_tiket[id_update]['email'] = input("Email baru       : ")
                        data_tiket[id_update]['no_hp'] = input("Nomor HP baru    : ")
                        data_tiket[id_update]['usia'] = input("Usia baru        : ")
                        print("Data E-Tiket berhasil diperbarui!")
                    else:
                        print("ID E-Tiket tidak ditemukan.")
                    input("Tekan ENTER untuk kembali...")

                #   Delete
                elif menu_admin == "4":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== HAPUS DATA E-TIKET ===")
                    id_hapus = input("Masukkan ID E-Tiket yang ingin dihapus: ")
                    if id_hapus in data_tiket:
                        konfirmasi = input(f"Anda yakin ingin menghapus {id_hapus}? (ya/tidak): ")
                        if konfirmasi == "ya":
                            del data_tiket[id_hapus]
                            print("Data berhasil dihapus!")
                        else:
                            print("Data batal dihapus.")
                    else:
                        print("ID E-Tiket tidak ditemukan.")
                    input("Tekan ENTER untuk kembali...")

                #   Logout
                elif menu_admin == "5":
                    break
                else:
                    print("Menu tidak valid!")
                    input("Tekan ENTER untuk kembali...")

        #   Menu Pengguna
        elif role == "pengguna":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"=== MENU PENGGUNA ({username}) ===")
                print("1. Lihat E-Tiket Saya")
                print("2. Daftar E-Tiket Baru")
                print("3. Logout")
                menu_pengguna = input("Pilih menu (1/2/3): ")

                # Lihat E-Tiket Pribadi
                if menu_pengguna == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== DATA E-TIKET SAYA ===")
                    print(f"{'ID':<8} {'Nama':<15} {'Kategori':<8} {'Email':<20} {'No HP':<12} {'Usia':<5}")
                    print("-" * 75)
                    ada = False
                    for key, value in data_tiket.items():
                        if value["nama"].lower() == username.lower():
                            ada = True
                            print(f"{key:<8} {value['nama']:<15} {value['kategori']:<8} {value['email']:<20} {value['no_hp']:<12} {value['usia']:<5}")
                    if not ada:
                        print("Belum ada e-tiket atas nama Anda.")
                    input("Tekan ENTER untuk kembali...")

                # Pengguna Daftar E-Tiket Pribadi
                elif menu_pengguna == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== DAFTAR E-TIKET IKN FUN RUN (NEW) ===")
                    #   Auto ID (IKN-XX)
                    new_id = "IKN" + str(len(data_tiket) + 1).zfill(2)
                    print(f"ID E-tiket otomatis: {new_id}")
                    kategori = "10KM"
                    email = input("Masukkan Email: ")
                    no_hp = input("Masukkan No HP: ")
                    usia = input("Masukkan Usia: ")
                    data_tiket[new_id] = {
                        "nama": username,
                        "kategori": kategori,
                        "email": email,
                        "no_hp": no_hp,
                        "usia": usia
                    }
                    print(f"Yeay, E-Tiket {new_id} berhasil didaftarkan untuk {username}.")
                    input("Tekan ENTER untuk kembali...")

                elif menu_pengguna == "3":
                    break
                else:
                    print("Pilihan tidak valid.")
                    input("Tekan ENTER untuk kembali...")

    # Menu Register Akun Baru
    elif menu_awal == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER AKUN BARU ===")
        new_user = input("Masukkan username baru: ")
        if new_user in akun:
            print("Username sudah terdaftar, coba username lain.")
        else:
            new_pass = input("Masukkan password: ")
            akun[new_user] = {"password": new_pass, "role": "pengguna"}
            print(f"Akun {new_user} berhasil dibuat. Silakan login untuk mendaftar tiket.")
        input("Tekan ENTER untuk kembali ke menu utama...")

    # Logout
    elif menu_awal == "3":
        print("Yeay, terimakasih sudah berkunjung:)")
        break

    else:
        print("Pilihan tidak valid.")
        input("Tekan ENTER untuk kembali...")