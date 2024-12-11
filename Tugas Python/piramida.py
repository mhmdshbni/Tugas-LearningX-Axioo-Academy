# Meminta pengguna untuk memasukkan jumlah baris piramida
rows = int(input("5:"))

# Menampilkan piramida
for i in range(1, rows + 1):
    # Mencetak spasi
    for j in range(rows - i):
        print(" ", end="")
    # Mencetak bintang
    for k in range(2 * i - 1):
        print("*", end="")
    print()