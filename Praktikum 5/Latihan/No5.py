kode = int (input("Masukan Kode Karyawan      : "))
nama = str(input("Masukan nama karyawan       : "))
gol = str(input("Masukan golongan (A/B/C/D    : "))
nkh = str(input("Mauskan Status(menikah/belum menikah  : "))
anak = int("Masukan jumlah anak(jika ngga ada 0)   : ")

#potongan gaji golongan
if( gol == "A"):
    gaji = 10000000
    potongan = 2.5
elif( gol == "B"):
    gaji = 8500000
    potongan = 2.0
elif( gol == "c"):
    gaji = 7000000
    potongan = 1.5
elif( gol == "D"):
    gaji = 5500000
    potongan = 1.0
else:
    print("anda Salah input golongan")
    exit()

#tunjangan
if(nkh == "menikah"):
    tunistri = gaji /10
tunanak = anak*ganjil/20
print("")
print("=======================================")
print("STRUCK RINCIAN GAJI KARYAWAN")
print("----------------------------------------")
print("Nama Karyawan    : " , nama)
print("Golongan      : " , gol)
print("Status Menikah     : ", nkh )
if (nkh == "menikah"):
    print("Jumlah anak     : ", anak , "anak")
print("---------------------------------------------")
print("Gaji pokok   : Rp ", int(gaji))
print("Tunjangan Istri/Suami   : Rp ", int(tunistri))
print("Tunjangan anak     : Rp", (tunanak))
print("------------------------------------------")
print("Gaji kotor      :", int(kotor))
print("potongan (xxxx %   :", potongan, "%")
print("--------------------------------------------")
print("Gaji Bersih    : Rp ", int(bersih))
