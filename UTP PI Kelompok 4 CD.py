#IMPORT
import time
import os

#DEKLARASI VARIABEL
fastTrack = 600000
regulerA = 500000
regulerB = 350000

#DEKLARASI LIST
nama = []  
umur = []
nomorTelepon = []
tiketFastTrack = 0
tiketRegulerA = 0
tiketRegulerB = 0

#FUNGSI HEADER()
def header():
    os.system('cls')
    print(" __ _   _  _   _   _  _   _  _ __ _ _   _ _    _   _  _     _   _  _ ")
    print("|_   /\ |  \/  | /\ | \| | | || | | _ ) | | | _ \  /\ | \| |   /\ | _ )/ _|")
    print("  | |/ _ \| |\/| |/ _ \| .` | | _ || || _ \ || |   / / _ \| .` |  / _ \| _ \ (__ ")
    print("  |// \_\_|  |// \_\_|\_| ||||_|_/\__/||\// \_\_|\_| // \\__/\__|")
    print("")

# FUNGSI JUMLAH PENGUNJUNG()
def pengunjung():
    global jumlahPengunjung
    while True:
        header()
        time.sleep(1)
        try:                                                 
            jumlahPengunjung = int(input("Jumlah Pengunjung : ")) 
            if jumlahPengunjung <=0:
                raise ValueError                                    #ERROR HANDLING 
            break
        except ValueError:
            print("")                                       #ERROR HANDLING 
            print("Input yang Anda Masukkan Salah!")  
            time.sleep(1)
    time.sleep(1)

#FUNGSI DISPLAY()
def display():
    print("==================================================================================")
    print("||                            Jenis Tiket :                                     ||")
    print("|| 1. Fast Track (Tiket Bebas Antre Include Semua Wahana)                       ||")
    print("|| 2. Reguler A  (Tiket Tanpa Bebas Antre Include Semua Wahana)                 ||")
    print("|| 3. Reguler B  (Tiket Tanpa Bebas Antre Tidak Full Include Semua Wahana)      ||")
    print("==================================================================================")
    print("")

#FUNGSI PESANAN()
def pesanan():
    global totalHargaTiket
    print("Total Tiket Yang Dipesan : ")
    print("Fast Track =" , tiketFastTrack , "x 600000")
    print("Reguler A  =" , tiketRegulerA , "x 500000")
    print("Reguler B  =" , tiketRegulerB , "x 350000")
    print("")
    totalHargaTiket = (tiketFastTrack * 600000) + (tiketRegulerA * 500000) + (tiketRegulerB * 350000)
    print("Total Harga Tiket : " , totalHargaTiket)
    print("")

#FUNGSI METODEBAYAR()
def metodeBayar():
    global metodePembayaran
    while True:
        header()
        display()
        pesanan()
        print("Pilih Metode Pembayaran : ")
        print("1. Cash")
        print("2. Cashless")
        try:      
            metodePembayaran = int(input("Metode Pembayaran : "))
            if metodePembayaran < 1 or metodePembayaran > 2:
                raise ValueError
            break
        except ValueError:
            print(" ")
            print("Input yang Anda Masukkan Tidak Sesuai!")
            time.sleep(1)
    time.sleep(1)

#FUNGSI PEMBAYARAN()
def pembayaran():
    if (metodePembayaran == 1):
        while True:      
            try:
                header()
                display()
                pesanan()
                print("Masukkan Uang Sesuai dengan Total Pembayaran")
                totalBayarCash = int(input("Masukkan Uang :"))        
                if totalBayarCash <= 0 :
                    raise ValueError
                break
            except ValueError:
                print("")  
                print("Input yang Anda Masukkan Tidak Sesuai!")
                time.sleep(1)
                
        while(totalBayarCash < totalHargaTiket):
            while True:          
                print("")
                print("Uang yang Anda Masukkan Kurang! Silakan Masukkan Uang Kembali")
                time.sleep(1)
                print("")
                kurangBayar = totalHargaTiket - totalBayarCash
                print("Uang Kurang Sebanyak :", kurangBayar)
                try:
                    bayarCash = int(input("Bayar :"))
                    if bayarCash <= 0 :
                        raise ValueError
                    break
                except ValueError:
                    print("")
                    print("Inputan Anda Tidak Sesuai!")
                    time.sleep(1)       
            totalBayarCash += bayarCash

        kembalian=totalBayarCash-totalHargaTiket

        time.sleep(1)
        header()

        print("Uang Anda : ", totalBayarCash)
        print("Kembalian anda: ", kembalian)
        print("Pembayaran Anda Berhasil")
        header()

        print("=======================================")
        print("================ STRUK ================")
        print("=======================================")
        print("Nama              :", nama)
        print("Umur              :", umur)
        print("Total Tiket       :", jumlahPengunjung)
        print("Total Harga Tiket :", totalHargaTiket)
        print("Bayar             :", totalBayarCash)
        print("Kembalian anda    :", kembalian)
        print("=======================================")
        print("")
        print("        Pembayaran Anda Berhasil")
        print("")
        print("--------------Terima Kasih-------------")
        print("")
        print("                HAVE FUN")
        print("")

    elif (metodePembayaran == 2):
        header()
        display()
        print("Total Harga Tiket : ", totalHargaTiket)
        print("Transfer Ke Rekening Dana 081234567890")
        print("")
        print("Nama: ", nama)
        print("Umur: ", umur)
        print("jenis Tiket: ", jenisTiket)
        print("Total Harga Tiket: ", totalHargaTiket)
        print("")
        print("Tolong cek ulang nominal pembayaran yang anda inputkan,")
        print("karena nominal yang sudah dikirim tidak dapat dikembalikan lagi!!")
        while True:
            print("")
            try:
                nominalTf=int(input("Inputkan nominal transfer: "))
                if nominalTf <= 0 :
                    raise ValueError
                break
            except ValueError:
                print("")
                print("Inputan Anda Tidak Sesuai")
                time.sleep(1)

        while(nominalTf < totalHargaTiket):
            print("")
            print("Uang yang Anda Masukkan Kurang! Silakan Masukkan Uang Kembali")
            time.sleep(1)
            kurang = totalHargaTiket - nominalTf
            print("")
            print("Uang Kurang Sebanyak :", kurang)
            while True:
                try:
                    nominalTambahan = int(input("Bayar :"))
                    break
                except ValueError:
                    print("")
                    print("Inputan Anda Tidak Sesuai")
                    time.sleep(1)
            nominalTf += nominalTambahan
        time.sleep(1)

        header()
        time.sleep(1)
        print("=======================================")
        print("================ STRUK ================")
        print("=======================================")
        print("Nama              :", nama)
        print("Umur              :", umur)
        print("jenis Tiket       :", jenisTiket)
        print("Total Harga Tiket :" , totalHargaTiket)
        print("Bayar             :", nominalTf)
        print("")
        print("        Pembayaran Anda Berhasil")
        print("")
        print("--------------Terima Kasih-------------")
        print("")
        print("                HAVE FUN")
        print("")
#------------------------------------------------------------------------------

#FUNGSI MAIN

pengunjung()

for i in range(0, jumlahPengunjung):
    while True:
        header()
        display()
        print("Pengunjung ", i+1)                       #OPERATOR ARITMATIKA
        try:
            jenisTiket =int(input("Jenis Tiket\t: "))
            if jenisTiket < 1 or jenisTiket > 3:
                raise ValueError                        #ERROR HANDLING
            break
        except ValueError:                              #ERROR HANDLING 
            print("")
            print("Input yang Anda Masukkan Tidak Sesuai!") 
            time.sleep(1)

    match jenisTiket:
        case 1:
            tiketFastTrack += 1
        case 2:
            tiketRegulerA += 1
        case 3:
            tiketRegulerB += 1   
    
    nama.append(input("Nama\t\t: "))                    #METHOD APPEND LIST
    umur.append(input("Umur\t\t: "))
    nomorTelepon.append(input("Nomor Telepon\t: "))
    nama[i] = nama[i].capitalize()                      #STRING METHOD UPPER
    i =+ 1                                              #OPERATOR ASSIGNMENT
    time.sleep(1)

metodeBayar()

pembayaran()
