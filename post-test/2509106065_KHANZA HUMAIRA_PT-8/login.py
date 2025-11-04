from data import akun, current_user
from fungsi import clear, pause, tidak_boleh_kosong
from admin import menu_admin
from user import menu_pengguna
from colorama import Fore, Style, init
init(autoreset=True)

def cek_login(username, password):
    if username in akun and akun[username]["password"] == password:
        return akun[username]["role"]
    else:
        raise KeyError(Fore.RED + "Username atau Password salah!")

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
        print(Fore.GREEN + f"Login berhasil sebagai {role}")
        from data import current_user as cu
        cu = username
        if role == "admin":
            menu_admin(username)
        else:
            menu_pengguna(username)
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
        login()

def register():
    from data import akun
    clear()
    print("REGISTER NEW AKUN IKN FUN RUN 10KM")
    try:
        new_user = input("Masukkan username baru: ")
        tidak_boleh_kosong(new_user)

        if new_user in akun:
            raise KeyError(Fore.RED + "Username sudah terdaftar!")

        new_pass = input("Masukkan password: ")
        tidak_boleh_kosong(new_pass)

        akun[new_user] = {"password": new_pass, "role": "pengguna"}
        print(Fore.GREEN + "Akun berhasil dibuat.")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
    pause()
