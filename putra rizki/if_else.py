def hitung_nilai_akhir(nama, nim, kehadiran, tugas, uts, uas):
    nilai_akhir = 0.1 * kehadiran + 0.2 * tugas + 0.3 * uts + 0.4 * uas
    return nilai_akhir

def tentukan_nilai_mutu(nilai_akhir):
    if 85 <= nilai_akhir <= 100:
        return 'A'
    elif 75 <= nilai_akhir <= 84:
        return 'B'
    elif 55 <= nilai_akhir <= 74:
        return 'C'
    elif 40 <= nilai_akhir <= 54:
        return 'D'
    else:
        return 'E'

# Input nilai dari pengguna
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
kehadiran = float(input("Masukkan Nilai Kehadiran: "))
tugas = float(input("Masukkan Nilai Tugas: "))
uts = float(input("Masukkan Nilai UTS: "))
uas = float(input("Masukkan Nilai UAS: "))

# Hitung nilai akhir
nilai_akhir = hitung_nilai_akhir(nama, nim, kehadiran, tugas, uts, uas)

# Tentukan nilai mutu
nilai_mutu = tentukan_nilai_mutu(nilai_akhir)

# Output hasil
print(f"\nNilai Akhir {nama}: {nilai_akhir}")
print(f"Nilai Mutu {nama}: {nilai_mutu}")