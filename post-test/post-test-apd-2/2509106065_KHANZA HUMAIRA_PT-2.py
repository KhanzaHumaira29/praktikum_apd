#Data suhu dalam celcius
suhu = [27, 33, 46, 55, 67, 92]

#Konversi suhu ke dalam fahrenheit, kelvin, reamur
fah1 = float (suhu[0]*9)/5+32   
fah2 = float (suhu[1]*9)/5+32
kel1 = float (suhu[2])+273.15
kel2 = float (suhu[3])+273.15
rea1 = float (suhu[4]*4)/5
rea2 = float (suhu[5]*4)/5

#Menghitung jumlah dan rata-rata suhu setelah di konversi
jumlah = fah1 + fah2 + kel1 + kel2 + rea1 + rea2
ratarata= jumlah / 6
nIM = 65
bolean = nIM < ratarata
print ("Suhu ke-1=" + str (suhu [0]))
print ("Suhu ke-2=" + str (suhu [1]))
print ("Suhu ke-3=" + str (suhu [2]))
print ("Suhu ke-4=" + str (suhu [3]))
print ("Suhu ke-5=" + str (suhu [4]))
print ("Suhu ke-6=" + str (suhu [5]))
print ("Fahrenheit dari suhu 27 derajat celcius=" + str (fah1),"F")
print ("Fahrenheit dari suhu 33 derajat celcius=" + str (fah2), "F")
print ("Kelvin dari suhu 46 derajat celcius=" + str (kel1), "K")
print ("Kelvin dari suhu 55 derajat celcius=" + str (kel2), "K")
print ("Reamur dari suhu 67 derajat celcius=" + str (rea1), "R")
print ("Reamur dari suhu 92 derajat celcius=" + str (rea2), "R")
print ("Jumlah suhu setelah di konversi=" + str (jumlah))
print ("Rata-rata=" + str (ratarata))
print ("NIM Anda=" + str (nIM))
print ("Bolean:" + str (bolean))

#Poin Plus
print ("Berikut list suhu dari 46 sampai 92 (celcius):", suhu [-4:6])