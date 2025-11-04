from prettytable import PrettyTable
from fungsi import clear, pause, tidak_boleh_kosong
from data import data_tiket
from colorama import Fore, Style
from colorama import Fore, Style, init
init(autoreset=True)

def total_tiket():
    return len(data_tiket)

def lihat_tiket_admin():
    clear()
    print(Fore.CYAN + "=" * 65)
    print("DATA E-TIKET IKN FUN RUN 10KM".center(65))
    print("=" * 65 + Style.RESET_ALL)
    if len(data_tiket) == 0:
        print(Fore.RED + "Belum ada data E-Tiket.")
    else:
        tabel = PrettyTable(["ID", "Nama", "Kategori", "Email", "No HP", "Usia"])
        for id_t, t in data_tiket.items():
            tabel.add_row([id_t, t['nama'], t['kategori'], t['email'], t['no_hp'], t['usia']])
        print(tabel)
        print(Fore.GREEN + f"Total E-Tiket: {total_tiket()}")
    pause()

def tambah_tiket():
    clear()
    print("TAMBAH DATA E-TIKET IKN FUN RUN 10KM")
    try:
        id_tiket = input("Masukkan ID E-Tiket : ")
        tidak_boleh_kosong(id_tiket)

        if id_tiket in data_tiket:
            raise KeyError(Fore.RED + "ID sudah tersedia!")

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
        print(Fore.GREEN + "Data E-Tiket sukses ditambahkan.")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
    pause()

def ubah_tiket():
    clear()
    print("=" * 65)
    print("UBAH DATA E-TIKET IKN FUN RUN 10KM".center(65))
    print("=" * 65)

    if len(data_tiket) == 0:
        print(Fore.RED + "Belum ada data E-Tiket.")
        pause()
        return
    else:
        tabel = PrettyTable()
        tabel.field_names = ["ID", "Nama", "Kategori", "Email", "No HP", "Usia"]
        for id_t, t in data_tiket.items():
            tabel.add_row([id_t, t['nama'], t['kategori'], t['email'], t['no_hp'], t['usia']])
        print(tabel)

    try:
        id_up = input("Masukkan ID untuk e-tiket yang ingin diubah : ")
        if id_up not in data_tiket:
            raise KeyError(Fore.RED + "ID E-Tiket tidak ditemukan!")

        print("Masukkan data baru (biarkan kosong jika tidak ingin diubah)")
        nama_baru = input(f"Nama baru ({data_tiket[id_up]['nama']}) : ") or data_tiket[id_up]['nama']
        email_baru = input(f"Email baru ({data_tiket[id_up]['email']}) : ") or data_tiket[id_up]['email']
        nohp_baru = input(f"No HP baru ({data_tiket[id_up]['no_hp']}) : ") or data_tiket[id_up]['no_hp']
        usia_baru = input(f"Usia baru ({data_tiket[id_up]['usia']}) : ") or data_tiket[id_up]['usia']

        data_tiket[id_up].update({
            "nama": nama_baru,
            "email": email_baru,
            "no_hp": nohp_baru,
            "usia": usia_baru
        })

        print(Fore.GREEN + "Data E-Tiket sukses diubah")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
    pause()

def hapus_tiket():
    clear()
    print("=" * 65)
    print("HAPUS DATA E-TIKET IKN FUN RUN 10KM".center(65))
    print("=" * 65)

    if len(data_tiket) == 0:
        print(Fore.RED + "Belum ada data E-Tiket.")
        pause()
        return
    else:
        tabel = PrettyTable()
        tabel.field_names = ["ID", "Nama", "Kategori", "Email", "No HP", "Usia"]
        for id_t, t in data_tiket.items():
            tabel.add_row([id_t, t['nama'], t['kategori'], t['email'], t['no_hp'], t['usia']])
        print(tabel)

    try:
        id_del = input("Masukkan ID untuk e-tiket yang ingin dihapus : ")
        if id_del not in data_tiket:
            raise KeyError(Fore.RED + "ID E-Tiket tidak ditemukan!")

        konfirmasi = input(f"Apakah Anda yakin ingin menghapus e-tiket {id_del}? (y/t): ").lower()
        if konfirmasi == "y":
            del data_tiket[id_del]
            print(Fore.GREEN + "Data E-Tiket sukses dihapus")
        else:
            print(Fore.RED + "Tiket batal dihapus.")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
    pause()

def menu_admin(current_user):
    while True:
        clear()
        print(f"MENU ADMIN ({current_user})")
        print("1. Tambah E-Tiket")
        print("2. Lihat Data E-Tiket")
        print("3. Ubah Data E-Tiket")
        print("4. Hapus Data E-Tiket")
        print("5. Logout")
        pilih = input(Fore.YELLOW + "Pilih menu: ")

        if pilih == "1": tambah_tiket()
        elif pilih == "2": lihat_tiket_admin()
        elif pilih == "3": ubah_tiket()
        elif pilih == "4": hapus_tiket()
        elif pilih == "5": break
        else:
            print(Fore.RED + "Pilihan tidak valid!")
            pause()