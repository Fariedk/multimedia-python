from PIL import Image

image = Image.open('claire.jpg')

resized_image = image.resize((100, 100))
resized_image.save('resized_result.jpg')