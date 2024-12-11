def print_pyramid(rows):
    if rows < 0:
        print("Jumlah baris tidak bisa kurang dari 0!")
    elif rows >= 10:
        print("Jumlah baris maksimal adalah 9!")
    else:
        for i in range(1, rows + 1):
            print(" " * (rows - i) + "*" * (2 * i - 1))

# Input jumlah baris
try:
    rows = int(input("Masukkan jumlah baris piramida (antara 1 hingga 9): "))
    print_pyramid(rows)
except ValueError:
    print("Input tidak valid. Silakan masukkan angka.")
