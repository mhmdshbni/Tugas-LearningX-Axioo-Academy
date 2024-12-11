# Data kualitas udara dengan variabel dictionary (Map)
data_kualitas_udara = {
    "Lokasi 1": 65,
    "Lokasi 2": 30,
    "Lokasi 3": 55,
    "Lokasi 4": 70,
    "Lokasi 5": 25,
    "Lokasi 6": 45,
    "Lokasi 7": 62,
    "Lokasi 8": 39,
    "Lokasi 9": 50,
    "Lokasi 10": 75
}

# Menggunakan control flow untuk memeriksa kualitas udara di setiap lokasi
for lokasi, kualitas in data_kualitas_udara.items():
    if kualitas > 60:
        status = "CLEAR"
    elif 40 <= kualitas <= 60:
        status = "POLUSI RINGAN"
    else:
        status = "POLUSI BERAT"
    
    # Menampilkan hasil untuk setiap lokasi
    print(f"{lokasi}: {kualitas} - {status}")