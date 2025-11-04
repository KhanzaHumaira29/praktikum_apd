from fungsi import clear, pause
from data import running
from login import login, register
from colorama import Fore, Style, init
init(autoreset=True)

def menu_awal():
    global running
    while running:
        clear()
        print("MENU AWAL SISTEM MANAJEMEN DATA E-TIKET EVENT IKN FUN RUN 10KM")
        print("1. Login (Admin/Pengguna)")
        print("2. Register Akun Baru")
        print("3. Keluar")
        pilih = input("Pilih menu (1/2/3): ")

        if pilih == "1":
            login()
        elif pilih == "2":
            register()
        elif pilih == "3":
            print(Fore.CYAN + "Yeay, terimakasih sudah berkunjung :)")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid.")
            pause()

if __name__ == "__main__":
    menu_awal()