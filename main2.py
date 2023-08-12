import sys
import os
from subprocess import run, PIPE

if os.path.isdir('.lib'):
    lib_path = os.path.dirname(__file__) + '/.lib'
    sys.path.append(lib_path)

import PIL.Image
from PIL import Image

class SpriteResizer:

    def __init__(self):
        pass

    def get_file(self) -> tuple:
        """
        # Summary:
            Gets a file path.

        ## Parameters:
            None

        ## Returns:
            bool : True if there was no error and False otherwise
            str : The output of the subcommand
        """
        data = run(["zenity", "--file-selection"], text=True, stderr=PIPE, stdout=PIPE)
        if len(data.stderr) > 0:
            return False, data.stderr.strip()
        return True, data.stdout.strip()

    def get_dir(self):
        """
        # Summary:
            Gets the dir path.

        ## Parameters:
            None

        ## Returns:
            bool : True if there was no error and False otherwise
            str : The output of the subcommand
        """
        data = run(["zenity", "--file-selection", "--directory"], text=True, stdout=PIPE, stderr=PIPE)
        if len(data.stderr > 0):
            return False, data.stderr.strip()
        return True, data.stdout.strip()

    def get_image(file_path):
        """
        # Summary:
            Gets an image and finds the pixel width and height.

        ## Parameters:
            file_path(str): The file path to the image.

        ## Returns:
            str: 
        """
        for file in file_names:
            img = Image.open(file)
            width = img.size[0]
            height = img.size[1]
            create_new_img(img, width, height, tile_sizes)



    def find_new_img_size(dimension, tile_sizes):
        new_dimension = 0
        if tile_sizes[0] == 48 and tile_sizes[1] == 16:
            new_dimension = dimension / 3
        elif tile_sizes[0] == 48 and tile_sizes[1] == 32:
            new_dimension = (dimension / 3) * 2
        elif tile_sizes[0] == 32 and tile_sizes[1] == 16:
            new_dimension = dimension / 2
        elif tile_sizes[0] == 32 and tile_sizes[1] == 48:
            new_dimension = (dimension / 2) * 3
        elif tile_sizes[0] == 16 and tile_sizes[1] == 32:
            new_dimension = dimension * 2
        elif tile_sizes[0] == 16 and tile_sizes[1] == 48:
            new_dimension = dimension * 3
        else:
            print("Error in find_new_img_size(). Non-matching cases")
            exit()
        return new_dimension



    def get_jump(tile_sizes):
        if tile_sizes[0] == 48:
            return 3
        elif tile_sizes[0] == 32:
            return 2
        elif tile_sizes[0] == 16:
            return 1
        else:
            print("Error in get_step(). Non-matching value")
            exit()



    def add_pixels(tile_sizes, new_pixels, i, j, r, g, b, a):
        if tile_sizes[0] == 48 and tile_sizes[1] == 16:
            new_pixels[i/3, j/3] = r,g,b,a
        elif tile_sizes[0] == 48 and tile_sizes[1] == 32:
            new_pixels[(i/1.5), (j/1.5)] = r,g,b,a
            new_pixels[(i/1.5), (j/1.5)+1] = r,g,b,a
            new_pixels[(i/1.5)+1, (j/1.5)] = r,g,b,a
            new_pixels[(i/1.5)+1, (j/1.5)+1] = r,g,b,a
        elif tile_sizes[0] == 32 and tile_sizes[1] == 16:
            new_pixels[i/2, j/2] = r,g,b,a
        elif tile_sizes[0] == 32 and tile_sizes[1] == 48:
            new_pixels[(i*1.5), (j*1.5)] = r,g,b,a
            new_pixels[(i*1.5), (j*1.5)+1] = r,g,b,a
            new_pixels[(i*1.5), (j*1.5)+2] = r,g,b,a
            new_pixels[(i*1.5)+1, (j*1.5)] = r,g,b,a
            new_pixels[(i*1.5)+2, (j*1.5)] = r,g,b,a
            new_pixels[(i*1.5)+1, (j*1.5)+1] = r,g,b,a
            new_pixels[(i*1.5)+2, (j*1.5)+1] = r,g,b,a
            new_pixels[(i*1.5)+1, (j*1.5)+2] = r,g,b,a
            new_pixels[(i*1.5)+2, (j*1.5)+2] = r,g,b,a
        elif tile_sizes[0] == 16 and tile_sizes[1] == 32:
            new_pixels[(i*2), (j*2)] = r,g,b,a
            new_pixels[(i*2), (j*2)+1] = r,g,b,a
            new_pixels[(i*2)+1, (j*2)] = r,g,b,a
            new_pixels[(i*2)+1, (j*2)+1] = r,g,b,a
        elif tile_sizes[0] == 16 and tile_sizes[1] == 48:
            new_pixels[(i*3), (j*3)] = r,g,b,a
            new_pixels[(i*3), (j*3)+1] = r,g,b,a
            new_pixels[(i*3), (j*3)+2] = r,g,b,a
            new_pixels[(i*3)+1, (j*3)] = r,g,b,a
            new_pixels[(i*3)+2, (j*3)] = r,g,b,a
            new_pixels[(i*3)+1, (j*3)+1] = r,g,b,a
            new_pixels[(i*3)+2, (j*3)+1] = r,g,b,a
            new_pixels[(i*3)+1, (j*3)+2] = r,g,b,a
            new_pixels[(i*3)+2, (j*3)+2] = r,g,b,a
        else:
            print("Error in get_step(). Non-matching cases")
            exit()
        return new_pixels




    def create_new_img(img, width, height, tile_sizes):
        # Old image
        img_rgba = img.convert("RGBA")
        pixels = img_rgba.load()
        # New image
        new_width = int(find_new_img_size(width, tile_sizes))
        new_height = int(find_new_img_size(height, tile_sizes))
        new_sizes = (new_width, new_height)
        new_img = PIL.Image.new("RGBA", new_sizes)
        new_pixels = new_img.load()
        # Add pixels to new image
        jump = get_jump(tile_sizes)
        for i in range(0, width, jump):
            for j in range(0, height, jump):
                r,g,b,a = pixels[i, j]
                new_pixels = add_pixels(tile_sizes, new_pixels, i, j, r, g, b, a)
        # Saves the new image
        new_img.save("test5.png")



    def main():
        file_names = []
        tile_sizes = get_tile_sizes()
        get_file_names(file_names)
        get_image(file_names, tile_sizes)



main()