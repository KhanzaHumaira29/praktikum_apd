import os
os.system ('cls')
# Data akun & tiket (nested list)
akun = [
    ["khanza", "065", "admin"],
    ["ghina", "ghina01", "pengguna"],
    ["van", "van02", "pengguna"],
    ["rumay", "rumay03", "pengguna"]
]
data_tiket = [
    ["IKN01", "ghina", "10KM", "ghina@gmail.com", "0812345678", "18"],
    ["IKN02", "van", "10KM", "van@gmail.com", "0898766541", "22"],
    ["IKN03", "rumay", "10KM", "rumay@gmail.com", "0835754632", "12"]
]
# Format: [id_tiket, nama_peserta, kategori, email, no_hp, usia]

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*60)
    print("MANAJEMEN DATA E-TIKET EVENT IKN FUN RUN 10KM".center(60))
    print("="*60)
    print("Terdapat dua pilihan untuk mengakses data e-tiket:")
    print("-admin")
    print("-pengguna")
    menu_awal = input("Selamat datang di Data Event IKN Fun Run Kategori 10KM. Ingin Login Sebagai Apa?: ")

    #   MENU LOGIN
    if menu_awal == "admin":
        os.system('cls' if os.name  == 'nt' else 'clear')
        print ("=== LOGIN E-TIKET EVENT IKN FUN RUN 10KM ===")
        username = input("Masukkan Username admin : ")
        password = input ("Masukkan Password admin : ")

        role = ""
        for i in range(len(akun)):
            if akun[i][0] == username and akun[i][1] == password:
                role = akun[i][2]

        if role == "":
            print("Username atau password salah!")
            input("Tekan ENTER untuk kembali...")
            continue

        # MENU ADMIN
        if role == "admin":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("="*60)
                print("SISTEM MANAJEMEN E-TIKET EVENT IKN FUN RUN 10KM".center(60))
                print("="*60)
                print("1. Tambah Tiket Baru (Create)")
                print("2. Lihat Data Tiket (Read)")
                print("3. Ubah Data Tiket (Update)")
                print("4. Hapus Data Tiket (Delete)")
                menu_admin = input("Masukkan Pilihan Menu (1/2/3/4): ")

                # Create 
                if menu_admin == "1":
                    os.system ('cls' if os.name == 'nt' else 'clear')
                    print("===SILAKAN TAMBAH DATA E-TIKET===")

                    id_tiket = input("Masukkan ID E-Tiket:")
                    nama = input("Masukkan nama peserta : ")
                    kategori = input("Kategori 10KM : ")
                    email = input("Masukkan email : ")
                    no_hp = input("Masukkan nomor hp : ")
                    usia = input("Masukkan usia peserta : ")

                    data_tiket.append([id_tiket, nama, kategori, email, no_hp, usia])
                    print("Data E-Tiket terbaru berhasil ditambahkan")
                    input("Tekan ENTER untuk kembali")

                # Read
                elif menu_admin == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("="*75)
                    print("DAFTAR DATA E-TIKET EVENT IKN FUN RUN 10KM".center(75))
                    print("="*75)
                    if len(data_tiket) == 0:
                        print("Belum ada data tiket tersedia")
                    else:
                        print(f"{'ID':<8} {'nama':<15} {'Kategori':<8} {'Email':<20} {'No HP':<12} {'Usia':<5}")
                        print("-" * 70)
                        for i in range(len(data_tiket)):
                            print(f"{data_tiket[i][0]:<8} {data_tiket[i][1]:<15} {data_tiket[i][2]:<8} {data_tiket[i][3]:<20} {data_tiket[i][4]:<12} {data_tiket[i][5]:<5}")
                    
                    input("Tekan ENTER untuk kembali")
                
                # Update
                elif menu_admin == "3" : 
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("===PERBARUI DATA E-TIKET EVENT IKN FUN RUN 10KM===")
                    id_update = input("Masukkan ID E-Tiket yang ingin diperbarui : ")
                    ditemukan = False
                    for i in range(len(data_tiket)):
                        if data_tiket[i][0] == id_update:
                            ditemukan = True
                            print("Data E-Tiket ditemukan, silakan isi data baru {id_update} : ")
                            print(f"Kategori: {data_tiket[i][2]} (tidak dapat diubah)")
                            print("-" * 50)
                            data_tiket[i][1] = input("Nama baru        : ")
                            data_tiket[i][3] = input("Email baru       : ")
                            data_tiket[i][4] = input("Nomor HP baru    : ")
                            data_tiket[i][5] = input("Usia baru        : ")
                            print("Data e-tiket berhasil diperbarui.")
                            break
                    if not ditemukan:
                        print("ID E-Tiket tidak ditemukan.")
                    input("Tekan ENTER untuk kembali")
                # Delete
                elif menu_admin == "4":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== HAPUS DATA E-TIKET EVENT IKN FUN RUN 10KM===")
                    id_hapus = input("Masukkan ID Tiket yang ingin dihapus: ")

                    for i in range(len(data_tiket)):
                        if data_tiket[i][0] == id_hapus:
                            print(f"Data dengan ID {id_hapus} ditemukan.")
                            konfirmasi = input("Yakin ingin menghapus data ini? (ya/tidak): ")
                            if konfirmasi == "ya":
                                del data_tiket[i]
                                print("Data E-Tiket berhasil dihapus.")
                            else:
                                print("E-Tiket batal dihapus")
                            break
                    if not ditemukan:
                        print("ID Tiket tidak ditemukan.")
                    input("Tekan ENTER untuk kembali")
    # Menu Login Pengguna
    elif menu_awal == "pengguna":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN PENGGUNA E-TIKET EVENT IKN FUN RUN ===")
        username = input("Masukkan Username Anda : ")
        password = input("Masukkan Password Anda : ")

        role = ""
        for i in range(len(akun)):
            if akun[i][0] == username and akun[i][1] == password:
                role = akun[i][2]

        if role == "":
            print("Username atau password salah!")
            input("Tekan ENTER untuk kembali")
            continue

        # Menu pengguna           
        if role == "pengguna":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"MENU PENGGUNA EVENT IKN FUN RUN ({username})")
                print("1. Check E-Tiket EVENT IKN FUN RUN SAYA")
                print("2. Logout")
                menu_pengguna = input("Pilih menu: ")

                # Cek e-tiket
                if menu_pengguna == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("="*75)
                    print("DATA E-TIKET IKN FUN RUN ANDA".center(75))
                    print("="*75)
                    print(f"{'ID':<8} {'Nama':<15} {'Kategori':<8} {'Email':<20} {'No HP':<12} {'Usia':<5}")
                    print("-" * 75)
                    for i in range(len(data_tiket)):
                        if data_tiket[i][1] == username:
                            t = data_tiket[i]
                            print(f"{t[0]:<8} {t[1]:<15} {t[2]:<8} {t[3]:<20} {t[4]:<12} {t[5]:<5}")
                    input("Tekan ENTER untuk kembali")
                
                # Logout aja
                elif menu_pengguna == "2":
                    break 
                else:
                    print("Pilihan menu pengguna tidak valid!")
                    input("Tekan ENTER untuk kembali")
    else: 
        print("Pilihan Anda tidak sesuai. Hanya admin dan pengguna saja")
        input("Tekan ENTER untuk mengulang")           