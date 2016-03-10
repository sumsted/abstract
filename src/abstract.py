from io import BytesIO
from PIL import Image
from sense_hat_client import set_pixels, rotation, clear

__author__ = 'scottumsted'


MATRIX_SIZE = 8


def start():
    image = get_image()
    new_image = resize_image(image)
    colors = get_color_matrix(new_image)
    to_hat(colors)



def get_image(file_name=None):
    infile = 'sarah.jpg' if file_name is None else file_name
    image_bytes = open(infile, 'rb').read()
    fp = BytesIO(image_bytes)
    return Image.open(fp)


def resize_image(image):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    width, height = image.size
    if width > ((height*3)//2):
        new_width = (3 * height) // 2
        x1 = width//2 - new_width//2
        y1 = 0
        x2 = new_width + x1
        y2 = height
    else:
        new_height = (2 * width) // 3
        x1 = 0
        y1 = height//2 - new_height//2
        x2 = width
        y2 = new_height + y1
    return image.crop((x1, y1, x2, y2))


def get_camera_image():
    pass


def get_average_color(image):
    image_data = image.getdata()
    r, g, b = 0, 0, 0
    num_pixels = len(image_data)
    for i in range(num_pixels):
        r += image_data[i][0]
        g += image_data[i][1]
        b += image_data[i][2]
    ar = r / num_pixels
    ag = g / num_pixels
    ab = b / num_pixels
    return [ar, ag, ab]


def get_color_matrix(image):
    block_width = image.size[0] // MATRIX_SIZE
    block_height = image.size[1] // MATRIX_SIZE
    pixels = []
    cell_coordinates = [(x, y) for x in range(0, MATRIX_SIZE) for y in range(0, MATRIX_SIZE)]
    h2 = 0
    v2 = 0
    for coor in cell_coordinates:
        # get random block in work image
        wx1 = block_width * coor[0]
        wy1 = block_height * coor[1]
        wx2 = wx1 + block_width
        wy2 = wy1 + block_height
        block = image.crop((wx1, wy1, wx2, wy2))
        color = get_average_color(block)
        pixels.append(color)
    return pixels


def to_hat(pixels):
    # rotation(90)
    set_pixels(pixels)


if __name__ =='__main__':
    # clear()
    start()
