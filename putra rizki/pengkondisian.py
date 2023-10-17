import math
import tkinter as tk
from tkinter import ttk

Nim = input("masukkan nim anda :")
Nama = input("masukkan nama anda :")
Nilai_kehadiran = float(input("masukkan nilai kehadiran anda :"))
Nilai_Tugas = float(input("masukan nilai tugas anda :"))
Nilai_UTS = float(input("masukkan nilai UTS anda :"))
Nilai_UAS = float(input("masukkan nilai UAS anda :"))

def tentukan_nilai_muthu (nilai_akhir):
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
    


nilai_akhir = 0.1 * Nilai_kehadiran + 0.2 * Nilai_Tugas + 0.3 * Nilai_UTS + 0.4 * Nilai_UAS

nilai_muthu = tentukan_nilai_muthu(nilai_akhir)




print("nim anda :\n", Nim )
print("Nama anda :\n", Nama)
print("Kehadiran anda sebanyak:\n", Nilai_kehadiran)
print("nilai tugas anda sebesar :\n", Nilai_Tugas)
print("nilai uts anda sebesar :\n", Nilai_UTS)
print("nilai uas anda sebesar :\n", Nilai_UAS)




print("Nilai akhir anda adalah sebesar :\n", nilai_akhir)
print("nilai muthu anda adalah :\n", nilai_muthu)