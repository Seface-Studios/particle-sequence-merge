import os
import sys
from PIL import Image
from glob import glob
from termcolor import colored

def main():
  print(colored("Where is the image sequence path?", "green"), "(Default: images/)")
  images_dir = input("› ")
  
  print("")
  print(colored("What should the name of the image be?", "green"), "(Default: particle.png)")
  image_name = input("› ")
  
  if (len(images_dir) == 0):
    images_dir = os.path.join(os.getcwd(), 'images')
    
  if (len(image_name) == 0):
    image_name = "particle.png"
  
  if (images_dir[-1] != '\\'):
    images_dir = os.path.join(images_dir, '')
  
  if not (os.path.isdir(images_dir)):
    print(colored("\nOps!", "red") + " This path doesn't exist.")
    input('Press enter to exit...\n')
    sys.exit(1)
  
  images_path = glob(images_dir + '*.png')
  images = []

  for image_path in images_path:
    image = Image.open(image_path)
    
    if (image.size[0] != image.size[1]):
      print(colored("\nOps!", "red") + " The image must have the same width and height.")
      input('Press enter to exit...\n')
      sys.exit(1)

    images.append(image)

  new_image_size = (images[0].size[0], images[0].size[1] * len(images))
  new_image = Image.new('RGBA', new_image_size, (255, 255, 255, 255))

  current_image_position = 0
  for image in images:
    new_image.paste(image, (0, current_image_position))
    current_image_position += image.size[0]

  new_image_dir = os.path.join(os.getcwd(), image_name)
  new_image.save(new_image_dir, "PNG")

if __name__ == '__main__':
  main()
