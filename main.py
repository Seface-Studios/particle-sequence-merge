import os
import sys
from PIL import Image
from glob import glob
from termcolor import colored

def main():
  print(colored("Where is the image sequence path?", "green"))
  print("Leave blank to use the default path (images/)")
  images_dir = input("› ")
  
  if (len(images_dir) == 0):
    images_dir = "images/"
  
  if not (os.path.exists(images_dir)):
    print(colored("\nOps!", "red") + " This path doesn't exist.")
    sys.exit(1)
  
  images_path = glob(images_dir + '*.png')
  images = []

  for image_path in images_path:
    image = Image.open(image_path)
    
    if (image.size[0] != image.size[1]):
      print(colored("\nOps!", "red") + " The image must have the same width and height.")
      sys.exit(1)
    
    images.append(image)

  new_image_size = (images[0].size[0], images[0].size[1] * len(images))
  new_image = Image.new('RGBA', new_image_size, (255, 255, 255, 255))

  current_image_position = 0
  for image in images:
    new_image.paste(image, (0, current_image_position))
    current_image_position += image.size[0]

  new_image.save("generated_image.png", "PNG")

main()
