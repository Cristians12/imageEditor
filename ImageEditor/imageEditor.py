from PIL import Image, ImageEnhance, ImageFilter
import os

# folder for unedited images
path = '/home/cristian/Desktop/Begginer_Projects/Automation1/ImageEditor/ImageEditor/imgs'
# folder for edited images
pathOut = '/home/cristian/Desktop/Begginer_Projects/Automation1/ImageEditor/ImageEditor/editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(0)

    factor = 1.5

    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f"{pathOut}/{clean_name}_edited.jpg")
