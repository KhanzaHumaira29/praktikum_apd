print ("Selamat datang, silakan login untuk mengakses kalkulator konversi.")
username = input("Masukkan username:")  
password = input("Masukkan password:")
if username == "khanza" and password == "065":
    print ("Yeay, login berhasil! Anda dapat mengakses kalkulator konversi.")        

    # --- MENU UTAMA ---
    print("=== SELAMAT DATANG DI KALKULATOR KONVERSI, SILAKAN PILIH MENU KONVERSI ===")
    print("1. Konversi Panjang")
    print("2. Konversi Massa")
    print("3. Konversi Suhu")
    print("4. Konversi Waktu")
    pilihan = input("Pilih menu (1-4): ")

    # --- KONVERSI PANJANG ---
    if pilihan == "1":
        print("Pilihlah sub menu yang ingin Anda konversi:")
        print("a. Kaki (feet) ke Meter")
        print("b. Kilometer ke Meter")
        print("c. Centimeter ke Meter")
        sub = input("Pilih konversi dengan sub menu dari (a-c): ")
        if sub == "a":
            feet = float(input("Masukkan nilai panjang kaki (feet): "))
            meter = feet * 0.3048
            print(f"{feet} kaki (feet) = {meter} meter")
        elif sub == "b":
            kilometer = float(input("Masukkan nilai dalam kilometer: "))
            meter = kilometer * 1000
            print(f"{kilometer} kilometer = {meter} meter")
        elif sub == "c":
            centimeter = float(input("Masukkan nilai dalam centimeter: "))
            meter = centimeter / 100
            print(f"{centimeter} centimeter = {meter} meter")
        else:
            print("Maaf, Anda salah memilih sub menu.")

# --- KONVERSI MASSA --- DENGAN POIN PLUS DITAMBAH 2 SATUAN KE KILOGRAM
    elif pilihan == "2":
        print("Pilihlah sub menu yang ingin Anda konversi:")
        print("a. Pon (Pound) ke Gram")
        print("b. Ton ke Kilogram")
        print("c. Gram ke Kilogram")
        print("d. Ons ke Kilogram")
        print("e. Miligram ke Kilogram")    
        sub = input("Pilih konversi dengan sub menu dari (a-e): ")
        if sub == "a":
            pound = float(input("Masukkan nilai massa dalam pon (pound): "))
            kg = pound * 0.453592
            print(f"Hasil konversi: {kg} kilogram")
        elif sub == "b":
            ton = float(input("Masukkan nilai massa dalam (ton metrik): "))
            kg = ton * 1000.0
            print(f"Hasil konversi: {kg} kilogram")
        elif sub == "c":
            gram = float(input("Masukkan nilai massa dalam gram: "))
            kg = gram / 1000.0
            print(f"Hasil konversi: {kg} kilogram")
        elif sub == "d":
            ons = float(input("Masukkan nilai massa dalam ons: "))
            kg = ons * 0.1
            print(f"Hasil konversi: {kg} kilogram")
        elif sub == "e":
            mg = float(input("Masukkan nilai massa dalam miligram: "))
            kg = mg / 1000000.0
            print(f"Hasil konversi: {kg} kilogram")
        else:
            print("Maaf, Anda salah memilih sub menu.")

# --- KONVERSI SUHU ---
    elif pilihan == "3":
        print("Pilihlah sub menu yang ingin Anda konversi:")
        print("a. Celcius ke Kelvin")
        print("b. Fahrenheit ke Kelvin")
        print("c. Reamur ke Kelvin")
        sub = input("Pilih konversi dengan sub menu dari (a-c): ")
        if sub == "a":
            c = float(input("Masukkan nilai suhu dalam Celcius: "))
            k = c + 273.15
            print(f"Hasil konversi adalah: {k} K")
        elif sub == "b":
            f = float(input("Masukkan nilai suhu dalam Fahrenheit: "))
            k = (f-32) * 5.0/9.0 + 273.15
            print(f"Hasil konversi adalah: {k} K")
        elif sub == "c":
            r = float(input("Masukkan nilai suhu dalam Reamur: "))
            k = (r * 5.0/4.0) + 273.15
            print(f"Hasil konversi adalah: {k} K")
        else:
            print("Maaf, Anda salah memilih sub menu.")

# --- KONVERSI WAKTU ---
    elif pilihan == "4":
        print("Pilihlah sub menu yang ingin Anda konversi:")
        print("a. Menit ke Detik")
        print("b. Jam ke Detik")
        sub = input("Pilih konversi dengan sub menu dari (a-b): ")
        if sub == "a":
            menit = float(input("Masukkan nilai waktu dalam menit: "))
            detik = menit * 60.0
            print(f"Hasil konversi adalah: {detik} detik")
        elif sub == "b":
            jam = float(input("Masukkan nilai waktu dalam jam: "))
            detik = jam * 3600.0
            print(f"Hasil konversi adalah: {detik} detik")
        else:
            print("Maaf, Anda salah memilih sub menu.")
    else:
        print("Maaf, Harap memilih menu yang tersedia (1-4).")

# --- LOGIN GAGAL --- POIN PLUS
elif username == "khanza" and password != "065":
    print("Password salah. Tetapi Username Anda benar, Silakan ulangi.")
elif username != "khanza" and password == "065":
    print("Username salah. Tetapi password Anda benar. Silakan ulangi.")
else:
    print("Maaf, Username dan Password salah. Program tidak dapat diakses.")