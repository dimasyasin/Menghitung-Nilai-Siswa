print("MINI PORGRAM MENGHITUNG NILAI SISWA DAN MENAMPILKANYA")

awal = 1
nilai = []
n = int(input("Masukan jumlah siswa ="))
while awal<=n:
    data=int(input("Masukan nilai siswa ="))
    nilai.append(data)
    awal=awal+1

print("Hasil rata-rata adalah = {}".format(sum(nilai)/n))

while True:
    shd = int(input("Apakah ingin melihat nilai ? 1. ya 2. tidak     "))
    if shd == 1:
        lihat_nilai = int(input("Lihat nilai siswa ke ="))
        print("Nilai siswa ke", lihat_nilai,"adalah =", nilai[lihat_nilai-1])
    if shd == 2:
        print("TERIMA KASIH")
        break