import sys
import datetime
import time

Cash = 0
Bank = 0
cuy = (1, 2)
data_keuangan = []
pengeluaran = []


# ========= Penarikan Start =========
def penarikan(Bank, Cash):
    Penarikan = int(input("Berapa yang mau di ambil: "))
    Tanggal = input("Masukan tanggal (DD-MM-YYYY): ")
    Bank -= Penarikan + 5000
    if Bank < 0:
        print("Transfer gagal, dana kurang.")
        Bank += Penarikan + 5000
    else:
        print("Penarikan uang berhasil, Anda akan dikenakan biaya 5000.")
        catatan_keuangan(Tanggal, "Penarikan uang dar bank", "Penarikan", Penarikan + 5000)

    Cash += Penarikan
    return Bank, Cash

# ========= Penarikan End =========


# ========= Pemasukan Start =========
def tambah_pemasukan(Cash, Bank):
    MasukanUang = int(input("Masukkan jumlah pemasukan: "))
    Deskripsi = input("Masukkan deskripsi pemasukan: ")
    Tanggal = input("Masukan tanggal (DD-MM-YYYY): ")

    print("1. Cash")
    print("2. Bank")
    MasukanKemana = int(input("Mau dimasukkan kemana: "))

    if MasukanKemana == 1:
        Cash += MasukanUang
        catatan_keuangan(Tanggal, Deskripsi, "Pemasukan Cash", MasukanUang)
    elif MasukanKemana == 2:
        Bank += MasukanUang
        catatan_keuangan(Tanggal, Deskripsi, "Pemasukan Bank", MasukanUang)
    else:
        print("Salah memasukkan pilihan.")

    return Cash, Bank

# ========= Pemasukan End =========
def Hacked(HackedCounter):
        for i in range (0,110, 10):
            print (i, "%")
            time.sleep(0.1)
            
        print("HACKED BY SILVER WOLF")
        time.sleep(3)
        print("Silver Wolf : Heee, salah sambung")
        time.sleep(3)
        print("Silver Wolf : omong omong apa apaan aplikasi ga guna ini")
        time.sleep(3)
        print("Silver Wolf : BYE")
        time.sleep(2)
        print()
        print()
        return HackedCounter
# ========= Catatan keuangan Start =========
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
# ========= Catatan keuangan End =========


HackedCounter = 0
# ========= Pengeluaran Start =========
# Inisialisasi array untuk menyimpan daftar pengeluaran

# Fungsi untuk menambahkan pengeluaran baru
def tambah_pengeluaran():
    global Bank, Cash
    nama = input("Masukkan nama pengeluaran: ")
    jumlah = float(input("Masukkan jumlah pengeluaran: "))
    tanggal = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    print ("1) Bank ")
    print ("2) Cash ")
    Pilihan = input("Dana mana yang mau di pakai : ")
    try:
        tanggal = datetime.datetime.strptime(tanggal, "%Y-%m-%d").date()
        pengeluaran.append({"nama": nama, "jumlah": jumlah, "tanggal": tanggal, })
        print("Pengeluaran berhasil ditambahkan.")
    except ValueError:
        print("Format tanggal tidak valid. Pengeluaran gagal ditambahkan.")
        
    if Pilihan == "1":
        Bank -= jumlah
        if Bank < 0:
            print("gagal, dana kurang.")
            Bank += jumlah
        else :
            print("Berhasil menambahkan pengeluaran")
            catatan_keuangan(tanggal, "Pengeluaran uang dari bank", "Pengeluaran", jumlah )
    elif Pilihan == "2":
        Cash -= jumlah
        if Cash < 0 :
            print("gagal, dana kurang.")
            Cash += jumlah
        else :
            print("Berhasil menambahkan pengeluaran")
            catatan_keuangan(tanggal, "Pengeluaran uang dari Cash", "Pengeluaran", jumlah )

# Fungsi untuk menampilkan daftar pengeluaran
def tampilkan_pengeluaran():
    if len(pengeluaran) == 0:
        print("Belum ada pengeluaran yang dicatat.")
    else:
        print("Daftar Pengeluaran:")
        for idx, peng in enumerate(pengeluaran):
            print(f"{idx+1}. {peng['tanggal']}: {peng['nama']}: {peng['jumlah']}")

# Fungsi untuk mencari pengeluaran berdasarkan nama
def cari_pengeluaran():
    keyword = input("Masukkan kata kunci untuk pencarian: ")
    hasil_pencarian = []
    for peng in pengeluaran:
        if keyword.lower() in peng['nama'].lower():
            hasil_pencarian.append(peng)
    if len(hasil_pencarian) == 0:
        print("Tidak ditemukan pengeluaran dengan kata kunci tersebut.")
    else:
        print("Hasil Pencarian:")
        for idx, peng in enumerate(hasil_pencarian):
            print(f"{idx+1}. {peng['tanggal']}: {peng['nama']}: {peng['jumlah']}")

# Fungsi untuk menghapus pengeluaran berdasarkan indeks
def hapus_pengeluaran():
    global Bank, Cash
    if len(pengeluaran) == 0:
        print("Belum ada pengeluaran yang dicatat.")
    else:
        tampilkan_pengeluaran()
        indeks = int(input("Masukkan indeks pengeluaran yang akan dihapus: "))
        if indeks >= 1 and indeks <= len(pengeluaran):
            del pengeluaran[indeks-1]
            print("Pengeluaran berhasil dihapus.")
        else:
            print("Indeks pengeluaran tidak valid.")

# Fungsi untuk menampilkan menu utama
def tampilkan_menu():
    print("=========================")
    print("Pencatat Keuangan Pribadi")
    print("=========================")
    print("1. Tambah Pengeluaran")
    print("2. Tampilkan Pengeluaran")
    print("3. Cari Pengeluaran")
    print("4. Hapus History Pengeluaran")
    print("0. Keluar")
    print("=========================")

# Loop utama program
def MenuPengeluaran():
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan menu: ")
        if pilihan == "1":
            tambah_pengeluaran()
        elif pilihan == "2":
            tampilkan_pengeluaran()
        elif pilihan == "3":
            cari_pengeluaran()
        elif pilihan == "4":
            hapus_pengeluaran()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.") 
# ========= Pengeluaran End =========



# ========= Main Function Start =========
DecisionCounter = 0

while DecisionCounter == 0:
    print("Jumlah uang cashmu adalah:", Cash)
    print("Jumlah uang di bankmu adalah:", Bank)
    print()
    print("========Cash Track=========")
    print("===========Menu============")
    print("0. ga ngapa ngapain 2 jam")
    print("1. Penarikan Uang")
    print("2. Pemasukan")
    print("3. Pengeluaran")
    print("4. Lihat Catatan Keuangan")
    
    Ngapain = input("Masukkan Pilihan: ")

    if HackedCounter == 7 :
        Hacked(HackedCounter)
    if Ngapain == "0":
        print("Terima kasih telah menggunakan Cashtrack.")
        sys.exit()
    elif Ngapain == "1":
        HackedCounter +=1
        Bank, Cash = penarikan(Bank, Cash)
    elif Ngapain == "2":
        HackedCounter +=1
        Cash, Bank = tambah_pemasukan (Cash, Bank)
    elif Ngapain == "3":
        HackedCounter +=1
        MenuPengeluaran()
    elif Ngapain == "4":
        lihat_catatan_keuangan()
    
    print()
    print("1) lanjut")
    print("2) Keluar")
    Decision = int(input("Apa yang mau dipilih : "))
    if Decision == 2:
        DecisionCounter += 1
        print("Terima kasih telah menggunakan Cashtrack.")
    elif Decision == 1:
        print("OK")
    else:
        while Decision not in cuy:
            MasukanLagi = int(input("Salah, ulangi lagi: "))
            Decision = MasukanLagi
            if Decision == 2:
                DecisionCounter += 1

# ========= Main Function End =========
