print("\n======================= PROGRAM KASIR MAYER =========================");

stop = False
hitung = 1
totalharga = 0
totalbarang = []

while (not stop):
    
    tambahbarang = input("\nMasukkan nama barang ke-{}: ".format(hitung));
    totalbarang.append(tambahbarang);

    tambahharga = int(input("Masukkan harga barang ke-{}: Rp".format(hitung)));
    banyakbarang = int(input("Berapa banyak barang ke-{}: ".format(hitung)));
    jumlahharga = (banyakbarang * tambahharga);
    totalharga += jumlahharga

    hitung += 1

    tanya = input("\nApakah ada barang yang ingin ditambah? [ya/tidak]: ");

    if (tanya == "tidak" or tanya == "Tidak" or tanya == "t" or tanya == "T"):
        stop = True

        print("\nTotal ada {} barang yaitu:".format(len(totalbarang)));
        for i in totalbarang:
            print(f"=> {i}");

        print(f"\nTotal dari semua jumlah harga barang: Rp{totalharga}");

uang = int(input("\nMasukkan nominal uang: Rp"));
kembalian = (uang - totalharga);

if (kembalian == int(0)):
    print("\nPAS!, TIDAK ADA KEMBALIAN...\n")

else:
    print(f"\nJadi kembaliannya adalah: Rp{kembalian} \n");

# PROGRAM CODE CREATE BY @MAYER-25/10/2023
# PROGRAM CODE DEVELOPED BY @MAYER-26/10/2023
# PROGRAM CODE DEVELOPED BY @MAYER-27/10/2023

""" This program is complete but not fast for 
calculations because it has a feature of displaying
 a list of names of items purchased as well as the 
 number of items purchased one by one """