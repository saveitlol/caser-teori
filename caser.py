class Node:
    def __init__(self, noSKU, namaBarang, hargaSatuan, jumlahStock):
        self.noSKU = noSKU
        self.namaBarang = namaBarang
        self.hargaSatuan = hargaSatuan
        self.jumlahStock = jumlahStock
        self.left = None
        self.right = None

class BEESTI:
    def __init__(self):
        self.root = None

    def search(self, noSKU):
        if self.root is None:
            return None
        tara = self.root
        while tara is not None:
            if noSKU < tara.noSKU:
                tara = tara.left
            elif noSKU > tara.noSKU:
                tara = tara.right
            else:
                return tara
        return None
    
    def insert(self, noSKU, namaBarang, hargaSatuan, jumlahStock):
        newNode = Node(noSKU, namaBarang, hargaSatuan, jumlahStock)
        if self.root is None:
            self.root = newNode
            return True
        tara = self.root
        while (True):
            if newNode.noSKU == tara.noSKU:
                print("Nomor SKU sudah ada. Penambahan anda akan ditolak.")
                return False
            if newNode.noSKU < tara.noSKU:
                if tara.left is None:
                    tara.left = newNode
                    return True
                tara = tara.left

            else :
                if tara.right is None:
                    tara.right = newNode
                    return True
                tara= tara.right


    def update(self, noSKU, stokBaru):
        barangLama = self.search(noSKU)
        if barangLama is not None:
            barangLama.jumlahStock += stokBaru
            print("Data Stok Barang berhasil diperbarui.")
            return True
        else:
            print("Data Stok Barang tidak ditemukan.")

    def tampilkan(self):
        self.ulangtampil(self.root)
    def ulangtampil(self, tara):
        if tara is not None:
            self.ulangtampil(tara.left)
            print("-"*40)
            print("Nomor SKU:", tara.noSKU)
            print("Nama Barang:", tara.namaBarang)
            print("Harga Satuan:", tara.hargaSatuan)
            print("Jumlah Stok:", tara.jumlahStock)
            print("-"*40)
            self.ulangtampil(tara.right)
    def cek(self,noSku):
        if len(noSku) != 4 or not noSku.isdigit():
            return False
        return True
def bubbleSort(transaksi):
    n = len(transaksi)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if transaksi[j]["subTotal"] < transaksi[j + 1]["subTotal"]:
                transaksi[j], transaksi[j + 1] = transaksi[j + 1], transaksi[j]

bst = BEESTI()
#untuk simpan data sementara
transaksi = []

def subOne():
    while True:    
        print("\nAnda berada di menu kelola stok barang")
        print("-"*40)
        print("1. Input data stok")
        print("2. Restok barang")
        print("3. kembali")
        print("-"*40)
        menu = int(input("masukkan pilihan: "))
        match menu:
            case 1:
                while True:
                    print("-"*40)
                    noSKU = input("Masukkan Nomor SKU (e untuk exit/keluar) : ")
                    if noSKU == "e":
                        break
                    if not bst.cek(noSKU):
                        print("NoMOR SKU harus terdiri dari 4 digit angka!")
                        continue
                    if bst.search(noSKU):
                        print("Nomor SKU sudah ada. Penambahan akan dibatalkan.")
                        continue
                    namaBarang = input("Masukkan Nama Barang: ")
                    hargaSatuan = float(input("Masukkan Harga Satuan: "))
                    jumlahStock = int(input("Masukkan Jumlah Stock: "))
                    bst.insert(noSKU, namaBarang, hargaSatuan, jumlahStock)
                    
                hasillihat= input("ingin melihat hasil ? (y/n): ")
                if hasillihat == "y":
                    noSKU= input("masukkan no SKU: ")
                    tara = bst.search(noSKU)
                    if tara:
                        print("-"*40)
                        print("hasil dari ->" + noSKU)
                        print("Nomor SKU:", tara.noSKU)
                        print("Nama Barang:", tara.namaBarang)
                        print("Harga Satuan:", tara.hargaSatuan)
                        print("Jumlah Stock:", tara.jumlahStock)
                        print("-"*40)
                        pin = input("kembali tekan y : ")
                        if pin == "y":
                            continue                        
                    else:
                        print("Nomor SKU tidak ditemukan.")
                        continue

                continue
            case 2:
                print("\nData Stock Barang Sekarang:")
                bst.tampilkan()
                while True:
                    noSKU = input("Masukkan Nomor SKU yang ingin di update: ")
                    if bst.search(noSKU) is not None:
                        print("Nomor SKU ada nih.")
                        stokBaru = int(input("Silahkan Masukkan Jumlah Stok baru: "))
                        bst.update(noSKU,stokBaru)
                        print("\nData Stok Barang Setelah Di Update")
                        bst.tampilkan()
                        cobae = input("apakah ingin update lagi ? (y/n): ")
                        if cobae == "y":
                            continue
                        else:
                            break
                    pin = input("kembali tekan y : ")
                    if pin == "y":
                        continue
                    else:
                        print("Nomor SKU tidak ada. update ditolak. silahkan input dahulu")
                        continue
            case 3:
                break
            case _:
                print("Maaf pilihan Anda salah")
                return False
def subTwo():
    while True:
        print("-"*40)
        print("\nAnda berada di menu kelola transaksi")
        print("-"*40)
        print("1. Input data transaksi baru")
        print("2. lihat data seluruh transaksi")
        print("3. lihat data dari subtotal")
        print("4. kembali")
        print("-"*40)
        menu = int(input("masukkan pilihan: "))
        match menu:
            case 1:
                namaKonsu = input("Masukkan Nama Konsumen: ")
                while True:
                    ulang = False
                    noSKU = input("Masukkan Nomor SKU yang dibeli: ")
                    barang = bst.search(noSKU)
                    if barang:
                        while True:
                            jumlahBeli = int(input("Masukkan Jumlah Barang yang dibeli: "))
                            
                            if jumlahBeli >= barang.jumlahStock:
                                print("Jumlah Stok Barang yang Anda beli tidak mencukupi.")
                                pilihan = input("Apakah ingin melanjutkan transaksi? (y/n): ")
                                if pilihan == "y":
                                    continue
                                elif pilihan == "n":
                                    print("Transaksi dibatalkan.")
                                    break

                            subTotal = jumlahBeli * barang.hargaSatuan

                            transaksi.append({
                                "namaKonsu": namaKonsu,
                                "noSKU": noSKU,
                                "jumlahBeli": jumlahBeli,
                                "subTotal": subTotal
                            })

                            bst.update(noSKU, -jumlahBeli)

                            print("Transaksi berhasil ditambahkan.")

                            pilihan = input("Apakah ingin melanjutkan transaksi? (y/n): ")
                            if pilihan == "y":
                                ulang = True
                                break
                            elif pilihan == "n":
                                break
                        if not ulang:
                            break
                    else:

                        print("Nomor SKU tidak ditemukan.")
                        pilihan = input("Apakah ingin memasukkan Nomor SKU lagi? (y/n): ")
                        if pilihan == "y":
                            continue
                        elif pilihan == "n":
                            break
                continue

            case 2:
                if not transaksi:
                    print("Tidak ada transaksi yang tersimpan.")
                else:
                    print("Daftar Transaksi:")
                    for i, listTrans in enumerate(transaksi, start=1):
                        print(f"Transaksi {i}:")
                        print("Nama Konsumen:", listTrans["namaKonsu"])
                        print("Nomor SKU:", listTrans["noSKU"])
                        print("Jumlah Beli:", listTrans["jumlahBeli"])
                        print("Sub Total:", listTrans["subTotal"])
                        print("------------------------")
                continue
            case 3:
                if not transaksi:
                    print("Tidak ada transaksi yang tersimpan.")
                else:
                    bubbleSort(transaksi)
                    print("Daftar Transaksi (Urutan Subtotal Terbesar ke Terkecil):")
                    for i, listTrans in enumerate(transaksi, start=1):
                        print(f"Transaksi {i}:")
                        print("Nama Konsumen:", listTrans["namaKonsu"])
                        print("Nomor SKU:", listTrans["noSKU"])
                        print("Jumlah Beli:", listTrans["jumlahBeli"])
                        print("Sub Total:", listTrans["subTotal"])
                        print("------------------------")
                continue
            case 4:
                return False
            case _:
                print("Maaf pilihan Anda salah")
                return False


# def menuHandler(menu):
#     match menu:
#         case 1:
#             subOne()
#             return True
#         case 2:
#             subTwo()
#             return True
#         case 3:
#             print("Terima kasih!")
#             return False
#         case _:
#             print("Maaf pilihan Anda salah")
#             return False

while True:
    print("\n---------- Perusahaan Retailee ---------")
    print("-"*40)
    print("Menu pilihan :")
    print("1. Kelola Stok Barang")
    print("2. Kelola Transaksi Konsumen")
    print("3. Exit")
    print("-"*40)
    menu = int(input("masukkan pilihan: "))
    # menuHandler(menu)
    # break
    if menu == 1:
        subOne()
    elif menu == 2:
        subTwo()
    else:
        print("terima kasih!")
        break