import sys
import datetime

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
    Tanggal = input("Masukan tanggal (DD-MM-YYYY): ")
    Bank -= Penarikan + 5000
    if Bank < 0:
        print("Transfer gagal, dana kurang.")
        Bank += Penarikan + 5000
    else:
        print("Transfer berhasil, Anda akan dikenakan biaya 5000.")
        catatan_keuangan(Tanggal, "Penarikan uang dar bank", "Penarikan", Penarikan + 5000)

    Cash += Penarikan
    return Bank, Cash

#Function Pemasukan (Edgar)
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

# ========= Pengeluaran =========
# Inisialisasi array untuk menyimpan daftar pengeluaran
pengeluaran = []

# Fungsi untuk menambahkan pengeluaran baru
def tambah_pengeluaran():
    nama = input("Masukkan nama pengeluaran: ")
    jumlah = float(input("Masukkan jumlah pengeluaran: "))
    tanggal = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    try:
        tanggal = datetime.datetime.strptime(tanggal, "%Y-%m-%d").date()
        pengeluaran.append({"nama": nama, "jumlah": jumlah, "tanggal": tanggal})
        print("Pengeluaran berhasil ditambahkan.")
    except ValueError:
        print("Format tanggal tidak valid. Pengeluaran gagal ditambahkan.")

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
    print("4. Hapus Pengeluaran")
    print("0. Keluar")
    print("=========================")

# Loop utama program
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
        print("Terima kasih telah menggunakan Cashtrack.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.") 
