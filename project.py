import sys
Cash = 0
Bank = 0
rekening = [123, 412]
cuy = (1, 2)


def penarikan(Bank, Cash):
    Penarikan = int(input("Berapa yang mau di ambil: "))
    Tanggal = input("Masukan tanggal : ")
    Bank -= Penarikan + 5000
    Cash += Penarikan
    if Bank < 0:
        print("Transfer gagal, dana kurang.")
        Bank += Penarikan + 5000
    else:
        print("Transfer berhasil, Anda akan dikenakan biaya 5000.")
    return Bank, Cash


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
        Bank, Cash = penarikan(Bank, Cash)
    
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
