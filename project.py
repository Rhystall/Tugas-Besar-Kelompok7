import sys
Cash = 0
Bank = 0
cuy = (1, 2)
data_keuangan = []

#Function Catatan Keuangan (Aufa)
def catatan_keuangan(tanggal, deskripsi, jenis, jumlah):
    data = {
        'Tanggal': tanggal,
        'Deskripsi': deskripsi,
        'Jenis': jenis,
        'Jumlah': jumlah
    }
    data_keuangan.append(data)

def lihat_catatan_keuangan():
    print("=== Catatan Keuangan ===")
    for data in data_keuangan:
        print("Tanggal:", data['Tanggal'])
        print("Deskripsi:", data['Deskripsi'])
        print("Jenis:", data['Jenis'])
        print("Jumlah:", data['Jumlah'])
        print("=======================")

#Function Penarikan (Aubrey)
def penarikan(Bank, Cash):
    Penarikan = int(input("Berapa yang mau di ambil: "))
    Tanggal = input("Masukan tanggal : ")
    Bank -= Penarikan + 5000
    if Bank < 0:
        print("Transfer gagal, dana kurang.")
        Bank += Penarikan + 5000
    else:
        print("Transfer berhasil, Anda akan dikenakan biaya 5000.")
    Cash += Penarikan
    return Bank, Cash

#Function Pemasukan (Edgar)
def tambah_pemasukan(Cash, Bank):
    MasukanUang = int(input("Masukkan jumlah pemasukan: "))
    Deskripsi = input("Masukkan deskripsi pemasukan: ")

    print("1. Cash")
    print("2. Bank")
    MasukanKemana = int(input("Mau dimasukkan kemana: "))

    if MasukanKemana == 1:
        Cash += MasukanUang
    elif MasukanKemana == 2:
        Bank += MasukanUang
    else:
        print("Salah memasukkan pilihan.")

    return Cash, Bank

#Function Pengeluaran (Nadia)


#Function Main (Aubrey)
DecisionCounter = 0

while DecisionCounter == 0:
    print("Jumlah uang cashmu adalah:", Cash)
    print("Jumlah uang di bankmu adalah:", Bank)
    print()
    print("========Cash Track=========")
    print("===========Menu============")
    print("0. ga ngapa ngapain 2 jam")
    print("1. Transfer Uang")
    print("2. Catat Pemasukan")
    print("3. Catat Pengeluaran")
    print("5. Lihat Catatan Keuangan")
    print("6. Keluar")
    
    Ngapain = input("Masukkan Pilihan: ")
    if Ngapain == "0":
        print("heeee, ok")
        sys.exit()
    elif Ngapain == "1":
        Bank, Cash = penarikan(Bank, Cash)
    elif Ngapain == "2":
        Cash, Bank = tambah_pemasukan (Cash, Bank)
    elif Ngapain == "5":
        lihat_catatan_keuangan()
    
    print()
    print("1) lanjut")
    print("2) Keluar")
    Decision = int(input("Apa yang mau dipilih : "))
    if Decision == 2:
        DecisionCounter += 1
    elif Decision == 1:
        print("OK")
    else:
        while Decision not in cuy:
            MasukanLagi = int(input("Salah, ulangi lagi: "))
            Decision = MasukanLagi
            if Decision == 2:
                DecisionCounter += 1

