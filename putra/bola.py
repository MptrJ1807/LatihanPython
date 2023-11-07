import tkinter as tk
from tkinter import Label, Entry, Button, END, W
from index import *

def hitungluas():
    r = float(txtradius.get())

    L = Luas(r)
    
    
    txtLuasPermukaan.delete(0, END)
    txtLuasPermukaan.insert(END, L)

def hitungVolume():
    r = float(txtradius.get())

    v = volume(r)

    txtVolume.delete(0, END)
    txtVolume.insert(END, v)


def hitung():
    hitungluas()
    hitungVolume()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Volume dan Luas Permukaan Bola")

# Windows
frame = tk.Frame(app)
frame.pack(padx=60, pady=60)

# Label Nama
nama_label = Label(frame, text="Nama : Muhammad Putra Rizki Julianto  : 220511080")
nama_label.grid(row=0, column=0, columnspan=2, sticky=W, padx=5, pady=5)

# Label Radius
radius_label = Label(frame, text="Radius:")
radius_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox Radius
txtradius = Entry(frame)
txtradius.grid(row=1, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=0, columnspan=2, pady=5)

# Output Label Luas Permukaan
luas_permukaan_label = Label(frame, text="Luas Permukaan: ")
luas_permukaan_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuasPermukaan = Entry(frame)
txtLuasPermukaan.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Volume
volume_label = Label(frame, text="Volume: ")
volume_label.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)


app.mainloop()