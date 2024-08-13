from PIL import Image
from PIL import ImageFilter
from filtering import filtered_image

image = Image.open('claire.jpg')

if filtered_image.mode == 'RGBA':
    filtered_image = filtered_image.convert('RGB')
    filtered_image.save('convertedFiltered_result.jpg')