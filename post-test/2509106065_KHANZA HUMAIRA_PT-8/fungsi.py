import os
from colorama import Fore, Style, init
init(autoreset=True)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input(Fore.YELLOW + "Tekan ENTER untuk kembali...")

def tidak_boleh_kosong(teks):
    if teks.strip() == "":
        raise ValueError("Input tidak boleh kosong!")

def cek_no_hp(no_hp):
    return no_hp.isdigit()
