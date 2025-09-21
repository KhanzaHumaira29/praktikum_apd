suhu = [0] * (6)

print ("Masukkan suhu ke-1 dalam Celcius:")
suhu [0] = int (input())
print ("Masukkan suhu ke-2 dalam Celcius:")
suhu [1] = int (input())
print ("Masukkan suhu ke-3 dalam Celcius:")
suhu [2] = int (input())
print ("Masukkan suhu ke-4 dalam Celcius:")
suhu [3] = int (input())
print ("Masukkan suhu ke-5 dalam Celcius:")
suhu [4] = int (input())
print ("Masukkan suhu ke-6 dalam Celcius:")
suhu [5] = int (input())
fah1 = float (suhu[0]*9)/5+32
fah2 = float (suhu[1]*9)/5+32
kel1 = float (suhu[2])+273.15
kel2 = float (suhu[3])+273.15
rea1 = float (suhu[4]*4)/5
rea2 = float (suhu[5]*4)/5
jumlah = fah1 + fah2 + kel1 + kel2 + rea1 + rea2
ratarata= jumlah / 6
print ("Masukkan dua digit NIM terakhir Anda:")
nIM = int (input())
bolean = nIM < ratarata
print ("Suhu ke-1=" + str (suhu [0]))
print ("Suhu ke-2=" + str (suhu [1]))
print ("Suhu ke-3=" + str (suhu [2]))
print ("Suhu ke-4=" + str (suhu [3]))
print ("Suhu ke-5=" + str (suhu [4]))
print ("Suhu ke-6=" + str (suhu [5]))
print ("Fahrenheit1=" + str (fah1))
print ("Fahrenheit2=" + str (fah2))
print ("Kelvin1=" + str (kel1))
print ("Kelvin2=" + str (kel2))
print ("Reamur1=" + str (rea1))
print ("Reamur2=" + str (rea2))
print ("Jumlah=" + str (jumlah))
print ("Rata-rata=" + str (ratarata))
print ("NIM Anda=" + str (nIM))
print ("Bolean:" + str (bolean))
print ("Slice suhu ke-3=" + str (suhu[2]))
print ("Slice suhu ke-4=" + str (suhu[3]))
print ("Slice suhu ke-5=" + str (suhu[4]))
print ("Slice suhu ke-6=" + str (suhu[5]))
