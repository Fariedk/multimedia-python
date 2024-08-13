from PIL import ImageFilter, Image

# Membuka gambar
image = Image.open('robin.png')

# Mengubah ukuran gambar
resized_image = image.resize((100, 100))

# Menambahkan efek blur
filtered_image = resized_image.filter(ImageFilter.BLUR)

# Menyimpan gambar hasil sebagai PNG tanpa perlu mengonversi mode warna
filtered_image.save('filtered_result.png')