import sys

Cash = 0
Bank = 0
rekening = [123, 412]
cuy = (1, 2)


def transfer(Bank):
    Transfer = int(input("Berapa yang mau di transferkan: "))
    Tujuan = int(input("Masukkan rekening yang mau di transfer: "))

    while True:
        if Tujuan not in rekening:
            ulang = int(input("Rekening tidak ditemukan, coba lagi: "))
            Tujuan = ulang
        else:
            Bank -= Transfer + 5000
            if Bank < 0:
                print("Transfer gagal, dana kurang.")
                Bank += Transfer + 5000
            else:
                print("Transfer berhasil, Anda akan dikenakan biaya 5000.")
            return Bank
            
# function pemasukan
def pemasukan (Cash,Bank):
    JumlahPemasukan = int(input("masukan pemasukan : ")
    Deskripsi = input("keterangan : ")
    print ("1. Cash")
    print ("2. Bank")

    MasukinKemana = int(input("Mau dimasukin kemana : ")

    if MasukinKemana == 1:
        Cash += JumlahPemasukan
    elif MasukinKemana == 2:
        Bank += JumlahPemasukan
    else : 
        print("pilihan tidak ada")
    return Cash, Bank

MasukanUang = int(input("Masukkan jumlah uang: "))
print("1) Cash")
print("2) Bank")
MasukanKemana = int(input("Mau dimasukkan kemana: "))

if MasukanKemana == 1:
    Cash += MasukanUang
elif MasukanKemana == 2:
    Bank += MasukanUang
else:
    print("Salah")

DecisionCounter = 0

while DecisionCounter == 0:
    print("Jumlah uang cashmu adalah:", Cash)
    print("Jumlah uang di bankmu adalah:", Bank)
    print()
    print("===== 0) ga ngapa ngapain 2 jam =====")
    print("===== 1) transfer ===================")
    print()
    Ngapain = input("")
    if Ngapain == "0":
        print("heeee, ok")
        sys.exit()
    elif Ngapain == "1":
        Bank = transfer(Bank)
    
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
#OTW

# def pemasukan():
# def history():
# def pengeluaran():
