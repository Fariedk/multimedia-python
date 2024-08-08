from PIL import Image
from PIL import ImageFilter
from resizing import resized_image

image = Image.open('claire.jpg')
filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('filtered_result.jpg')