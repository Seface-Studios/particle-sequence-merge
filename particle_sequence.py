import sys
from PIL import Image
from glob import glob

def merge():
  images_path = glob("images/*.png")
  images = []

  for image_path in images_path:
    image = Image.open(image_path)
    
    if (image.size[0] != image.size[1]):
      print("The image must have the same width and height.")
      sys.exit(1)
    
    images.append(image)

  new_image_size = (images[0].size[0], images[0].size[1] * len(images))
  new_image = Image.new('RGB', new_image_size, (250, 250, 250))

  current_image_position = 0
  for image in images:
    new_image.paste(image, (0, current_image_position))
    current_image_position += image.size[0]

  new_image.save("image_gerada.png", "PNG")
