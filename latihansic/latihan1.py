nama = "melvin zainul bahtiar"
umur = 16
sekolah = "smk satya praja 2 petarukan "
alamat = "desa kendalrejo"
rt = 5
rw = 2

print("nama ", nama,  "umur :", umur, "sekolah di :", sekolah, "alamat :", alamat)


# operasi perhitungan
barang1 = 100000
barang2 = 200000
totalharga = barang1 + barang2
print(totalharga)


# pengukur keliling bangunan 
keliling1 = 1000
keliling2 = 2000


angka_1 = 10
angka_2 = 20
angka_3 = 10
angka_4 = 40
angka_5 = 50
angka_6 = 23
angka_7 = 12

penjumlahan = angka_1 + angka_2
print("hasil penjumlahan adalah : ", penjumlahan)

pengurangan = angka_3 - angka_4
print("hasil pengurangan adalah : ", pengurangan)

perkalian = angka_2 * angka_3
print("hasil perkalian adalah : ", perkalian)

pembagian = angka_2 / angka_3
print("hasil pembagian adalah : ", pembagian)

pembagian_double = angka_2 // angka_1
print("hasil pembagian double adalah : ", pembagian_double)

modulus = angka_2 // angka_4
print("modulus nya adalah : ", modulus)

pangkat = angka_1 ** angka_6
print("hasil pangkat adalah : ", pangkat)


sama_dengan = 1 == 0
print(sama_dengan)

# operator logika 
semi_konduktor = 10 + 0 and 10 - 20
print(semi_konduktor)



umur = 16
izin_orang_tua = True

if umur >= 17 and izin_orang_tua:
    print("sudah dapat buat ktp")
else:
    print("belum dapat buat ktp")

if umur <= 17 or izin_orang_tua:
    print("sudah dapat buat sim")
else:
    print("belum dapat buat sim")


romantis = 20 != 20
print(romantis)


bangunan = 30
bangunan -= 20
print(bangunan)


# baru = int(input("masukan nilai anda"))

# if baru < 17:
#     print("umur kamu di bawah 17 tahun")
# elif baru == 17:
#     print("selamat usia pas sekali")
# elif baru >= 17:
#     print("umur kamu  di atas 17 tahun")
# else:
#     print("umur kamu melebihi batas deh")


umur = 16
punya_ktp = False

if umur >= 17:
    if punya_ktp:
        print("Boleh bikin SIM")
    else:
        print("Sudah cukup umur tapi belum punya KTP")
else:
    print("Belum cukup umur")



bilangan1 = 10 
sudah_umur17 = True
sudah_belajar = True

if bilangan1 > 5:
    if sudah_umur17:
        print("yeah kamu sudah bisa bikin sim")
    else:
        print("semoga kamu bisa lagi ya ")
else:
    print("semoga kamu bisa lanjut lagi ya ")


 