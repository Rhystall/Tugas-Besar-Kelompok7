Cash = 0
Bank = 0

MasukanUang = int(input("Masukan jumlah uang : "))
print("1) Cash")
print("2) Bank")
MasukanKemana = int(input("Mau dimasukan kemana : "))

if MasukanKemana == 1 :
    Cash =+ MasukanUang
elif MasukanKemana == 2 :
    Bank =+ MasukanUang
else :
    print("salah")

DecisionCounter = 0

cuy = (1,2)

while DecisionCounter == 0:
    print("jumlah uang cash mu adalah :", Cash)
    print("jumalah uang di bank mu adalah :", Bank)
    # MauNgapain = input("Mau ngapain :")
    Decision = int(input("ketik 1. untuk lanjut dan 2. untuk stop : "))
    if Decision == 2 :
        DecisionCounter =+ 1
    elif Decision == 1 :
        print("ok")
    else :
        while Decision not in cuy :
            MasukanLagi = int(input("Salah ulang lagi :"))
            Decision = MasukanLagi
            if Decision == 2 :
                DecisionCounter =+ 1

#OTW
def tranfer()

def history()
