import sys
import os
from PIL import Image

def main():
    #grab first and second argument
    image_folder = sys.argv[1]
    new_folder = sys.argv[2]
    #check if the new file exists, if not then create a new one
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    #loop through the jpegs and convert to png
    for filename in os.listdir(image_folder):  #makes the image folder iterable
        image = Image.open(f'{image_folder}{filename}')
        noJPEGname = os.path.splitext(filename)[0] #returns a tuple of the filename and .jpeg 
        image.save(f'{new_folder}{noJPEGname}.png', "png") #use[0] because we dont want .jpeg
if __name__ == "__main__":
   main()