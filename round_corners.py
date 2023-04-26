from PIL import Image, ImageDraw

# if this doesn't run, write "pip3 install pillow" in the terminal and press enter

# EDIT THIS

INPUT_IMAGE_NAME = "sato-code-promo-1.jpg"
ROUNDED_CORNER_RADIUS = 50 # Lower number = lower "roundedness"

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

def execute(filename:str, radius:int):
    im = Image.open(filename)
    im = add_corners(im, radius)
    im.save(f"{filename}_rounded_{radius}.png")

execute(INPUT_IMAGE_NAME, ROUNDED_CORNER_RADIUS)