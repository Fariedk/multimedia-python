from PIL import Image

# Memuat gambar
image = Image.open('claire.jpg')

# Menyimpan gambar
image.save('result.jpg')