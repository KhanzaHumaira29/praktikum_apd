from prettytable import PrettyTable
from fungsi import clear, pause
from data import data_tiket
from fungsi import cek_no_hp
from colorama import Fore, Style, init
init(autoreset=True)


def lihat_tiket_saya(current_user):
    clear()
    print(f"DATA E-TIKET ATAS NAMA: {current_user}")
    tabel = PrettyTable(["ID", "Nama", "Kategori", "Email", "No HP", "Usia"])
    ada = False
    for id_t, v in data_tiket.items():
        if v['nama'] == current_user:
            ada = True
            tabel.add_row([id_t, v['nama'], v['kategori'], v['email'], v['no_hp'], v['usia']])
    if ada:
        print(tabel)
    else:
        print(Fore.RED + "Belum ada e-tiket atas nama Anda.")
    pause()

def daftar_tiket_baru(current_user):
    clear()
    print("DAFTAR E-TIKET BARU")
    try:
        new_id = "IKN" + str(len(data_tiket) + 1).zfill(2)
        email = input("Email : ")
        no_hp = input("No HP : ")
        if not cek_no_hp(no_hp):
            raise ValueError(Fore.RED + "Nomor HP harus angka!")
        usia = input("Usia : ")

        data_tiket[new_id] = {
            "nama": current_user,
            "kategori": "10KM",
            "email": email,
            "no_hp": no_hp,
            "usia": usia
        }
        print(Fore.GREEN + f"E-Tiket dengan id {new_id} sukses didaftarkan.")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
    pause()

def menu_pengguna(current_user):
    while True:
        clear()
        print(f"MENU PENGGUNA ({current_user})")
        print("1. Lihat E-Tiket Saya")
        print("2. Daftar E-Tiket Baru")
        print("3. Logout")
        pilih = input("Pilih menu: ")

        if pilih == "1": lihat_tiket_saya(current_user)
        elif pilih == "2": daftar_tiket_baru(current_user)
        elif pilih == "3": break
        else:
            print(Fore.RED + "Pilihan tidak valid!")
            pause()