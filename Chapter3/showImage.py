import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Aplikasi Multimedia")

# Memuat gambar menggunakan Pillow
image = Image.open('claire.jpg')
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack()

root.mainloop()