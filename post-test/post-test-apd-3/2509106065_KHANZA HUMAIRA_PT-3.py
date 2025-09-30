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
    print("5. Konversi Mata Uang") # POIN PLUS
    pilihan = input("Pilih menu (1-5): ")

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
            f = float(input("Masukkan nilai dalam Fahrenheit: "))
            k = (f-32) * 5.0/9.0 + 273.15
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

# --- KONVERSI MATA UANG POIN PLUS ---
    elif pilihan == "5":
        print("Pilihlah sub menu mata uang yang ingin Anda konversi:")
        print("a. Rupiah ke Dolar")
        print("b. Dolar ke Rupiah")
        print("c. Rupiah ke Yen")
        print("d. Yen ke Rupiah")
        print("e. Rupiah ke Won")
        print("f. Won ke Rupiah")
        sub = input("Pilih konversi dengan sub menu dari (a-f): ")

        if sub == "a":
            rupiah = float(input("Masukkan jumlah Rupiah: "))
            usd = rupiah / 15000  # asumsi 1 USD = 15000 IDR
            print(f"{rupiah} Rupiah = {usd} Dolar AS")
        elif sub == "b":
            usd = float(input("Masukkan jumlah Dolar AS: "))
            rupiah = usd * 15000
            print(f"{usd} Dolar AS = {rupiah} Rupiah")
        elif sub == "c":
            rupiah = float(input("Masukkan jumlah Rupiah: "))
            yen = rupiah / 110  # asumsi 1 Yen = 110 IDR
            print(f"{rupiah} Rupiah = {yen} Yen Jepang")
        elif sub == "d":
            yen = float(input("Masukkan jumlah Yen: "))
            rupiah = yen * 110
            print(f"{yen} Yen Jepang = {rupiah} Rupiah")
        elif sub == "e":
            rupiah = float(input("Masukkan jumlah Rupiah: "))
            won = rupiah / 12  # asumsi 1 Won = 12 IDR
            print(f"{rupiah} Rupiah = {won} Won Korea")
        elif sub == "f":
            won = float(input("Masukkan jumlah Won: "))
            rupiah = won * 12
            print(f"{won} Won Korea = {rupiah} Rupiah")
        else:
            print("Maaf, Anda salah memilih sub menu.")

    else:
        print("Maaf, Harap memilih menu yang tersedia (1-4).")

    print("Terimakasih telah menggunakan kalkulator konversi! Kritik dan saran sangat diharapkan demi kesuksesan program ini.")

# --- LOGIN GAGAL --- POIN PLUS
elif username == "khanza" and password != "065":
    print("Password salah. Tetapi Username Anda benar, Silakan ulangi.")
elif username != "khanza" and password == "065":
    print("Username salah. Tetapi password Anda benar. Silakan ulangi.")
else:
    print("Maaf, Username dan Password salah. Program tidak dapat diakses.")