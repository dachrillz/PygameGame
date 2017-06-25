#Heavily inspired by: https://www.hackerearth.com/practice/notes/beautiful-python-a-simple-ascii-art-generator-from-images/
from PIL import Image
ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

def scale_image(image, new_width=100):
    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image, new_width, new_height

def convert_to_grayscale(image):
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width=25):
    """Maps each pixel to an ascii char based on the range
    in which it lies.

    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[int(pixel_value/range_width)] for pixel_value in
            pixels_in_image]

    return "".join(pixels_to_chars)

def convert_image_to_ascii(image, new_width=100):
    image,new_width, new_height = scale_image(image)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in
            range(0, len_pixels_to_chars, new_width)]

    
    return ".".join(image_ascii),new_width, new_height
    
def convertStringToArray(image_ascii,height,width):
    array = [[None for _ in range(width)] for _ in range(height)]
    import numpy as np
    k = 0
    for i in range(height):
        for j in range(width):
            nextchar = image_ascii[k]
            array[i][j]  = nextchar
            k += 1
            
    return array

def handle_image_conversion(image_filepath,height,width):
    image = None
    try:
        image = Image.open(image_filepath)
    except Exception:
        print("Unable to open image file.")
        return

    image_ascii,new_width, new_height = convert_image_to_ascii(image)
    
    array = convertStringToArray(image_ascii,new_width, new_height)
    
    return array
