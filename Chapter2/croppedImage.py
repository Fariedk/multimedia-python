from PIL import Image

image = Image.open('claire.jpg')

cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('cropped_result.jpg')