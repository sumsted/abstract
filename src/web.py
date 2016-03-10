import base64
from PIL import Image, ImageDraw
from bottle import get, debug, run, view
# import picamera
# import cStringIO
import io
from tools import handle_padded
import common_views


debug_mode = True
port = 8082


@get("/")
@view("index.html")
def landing():
    return {}

@get("/bs")
@view("bs.html")
def landing():
    return {}


class GopiImage():
    COLORS = {
        'red': ((80, 0, 0), (255, 80, 80)),
        'green': ((0, 110, 0), (100, 255, 50)),
        'blue': ((50, 80, 50), (110, 150, 110))
    }

    # COLORS = {
    #     'red': ((110, 0, 0), (255, 100, 100)),
    #     'green': ((0, 150, 0), (100, 255, 100)),
    #     'blue': ((0, 0, 150), (100, 100, 255))
    # }

    IMAGE_SIZE = (320, 240)
    SPOT_MAP = {
        -15: (20, 100, 60, 140),
        -10: (60, 100, 100, 140),
        -5: (100, 100, 140, 140),
        0: (140, 100, 180, 140),
        5: (180, 100, 220, 140),
        10: (220, 100, 260, 140),
        15: (260, 100, 300, 140)
    }

    def __init__(self):
        self.image_byte_array = ''

    def write(self, image_byte_array):
        self.image_byte_array += image_byte_array

    def get_image_target_overlay(self):
        image = Image.open(cStringIO.StringIO(self.image_byte_array))
        red = '#FF0000'
        green = '#48BD41'
        draw = ImageDraw.Draw(image)

        width = image.size[0]
        height = image.size[1]

        xc = width / 2
        yc = height / 2
        radius = width / 5
        center_space = radius / 5
        fat_space = radius / 2
        x0 = xc - radius
        x1 = xc + radius
        y0 = yc - radius
        y1 = yc + radius
        for i in range(5):
            box = (x0 + i, y0 + i, x1 - i, y1 - i)
            draw.ellipse(box, outline=green)

        line = (x0, yc, xc - center_space, yc)
        draw.line(line, fill=green, width=3)
        line = (x1, yc, xc + center_space, yc)
        draw.line(line, fill=green, width=3)
        line = (xc, y1, xc, yc + center_space)
        draw.line(line, fill=green, width=3)

        line = (x0, yc, xc - fat_space, yc)
        draw.line(line, fill=green, width=5)
        line = (x1, yc, xc + fat_space, yc)
        draw.line(line, fill=green, width=5)
        line = (xc, y1, xc, yc + fat_space)
        draw.line(line, fill=green, width=5)

        box = (xc - 2, yc - 2, xc + 2, yc + 2)
        draw.ellipse(box, fill=red)

        fp = io.BytesIO()
        image.save(fp, 'PNG')
        image_byte_array = fp.getvalue()
        fp.close()
        return 'data:image/png;base64,' + base64.b64encode(image_byte_array)

    def get_image_byte_array(self):
        return self.image_byte_array

    def get_b64(self):
        return 'data:image/png;base64,' + base64.b64encode(self.image_byte_array)


@get('/cam/target')
@handle_padded
def cam_image(kargs):
    gpi = GopiImage()

    with picamera.PiCamera() as camera:
        camera.resolution = gpi.IMAGE_SIZE
        camera.capture_sequence([gpi], format="jpeg", use_video_port=False)

    return {'image': gpi.get_image_target_overlay()}


if __name__ == '__main__':
    debug(debug_mode)
    run(host='localhost', port=port, debug=debug_mode)