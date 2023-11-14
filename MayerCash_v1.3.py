s = False
h = 1
toh = 0

while not s:
    try:
        tah = int(input("\nHarga barang ke-{}: Rp".format(h)))
    except ValueError:
        print("Input bukan angka!")
        continue

    while True:
        try:
            jb = int(input("jumlah barang ke-{}: ".format(h)))
            break
        except ValueError:
            print("Input bukan angka!\n")

    tsh = tah * jb
    toh += tsh

    h += 1

    ty = input("Tambah barang Lagi? [y/t]: ")

    if ty == "t" or ty == "T":
        s = True
        print(f"\nTotal harganya: Rp{toh}")

while True:
    try:
        ug = int(input("\n\nBerapa Uangnya?: Rp"))
        break
    except ValueError:
        print("Input bukan angka!")

ss = ug - toh

if ss == int(0):
    print("\nPAS!, Tidak ada kembalian..\n")

elif ug < toh:
    print(f"\nUangnya kurang!, butuh Rp{-ss} lagi...\n")

else:
    print(f"\nKEMBALIAN: Rp{ss} \n")

# CODE EVALUATE AND CREATE BY @MAYERAS 27/10/2023
# CODE DEVELOPED BY @MAYERAS 12/11/2023
# This program is very fast in its calculations but has few features