#Name: Manjit Gurcha
#Filters for CST205 project

from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps

#no filter
def none (picture):
    picture.save("temp.png")

#posterize image
def posterize(picture):
    picture = ImageOps.posterize(picture, 1)
    picture.save("temp.png")

def solarize(picture):
    picture = ImageOps.solarize(picture)
    picture.save("temp.png")

#sharpen image
def sharpen(picture):
    picture = picture.filter(ImageFilter.EDGE_ENHANCE)
    picture.save("temp.png")

#convert to black & white
def black_white(picture):
    picture = picture.convert("1")
    picture.save("temp.png")

#blur image
def blur(picture):
    picture = picture.filter(ImageFilter.BLUR)
    picture.save("temp.png")

#negative image
def negative(picture):
    picture = ImageOps.invert(picture)
    picture.save("temp.png")

#temporary for sepia
def temp_grayscale(picture):
    new_list = []
    for p in picture.getdata():
        new_red = int(p[0] * 0.299)
        new_green = int(p[1] * 0.587)
        new_blue = int(p[2] * 0.114)
        luminance = new_red + new_green + new_blue
        temp = (luminance, luminance, luminance)
        new_list.append(temp)
    return(new_list)

#sepia image
def sepia(picture):
    width, height = picture.size
    mode = picture.mode
    temp_list = []
    pic_data = temp_grayscale(picture)

    for p in pic_data:
        # tint shadows
        if p[0] < 63:
            red_val = int(p[0] * 1.1)
            green_val = p[1]
            blue_val = int(p[2] * 0.9)

        # tint midtones
        if p[0] > 62 and p[0] < 192:
            red_val = int(p[0] * 1.15)
            green_val = p[1]
            blue_val = int(p[2] * 0.85)

        # tint highlights
        if p[0] > 191:
            red_val = int(p[0] * 1.08)
            if red_val > 255:
                red_val = 255
            green_val = p[1]
            blue_val = int(p[2] * 0.5)
        temp_list.append((red_val, green_val, blue_val))
    picture.putdata(temp_list)
    picture.save("temp.png")

#Thumbnail
def thumbnail (picture):
    canvas = Image.new( "RGB" , ( 640 , 480 ), "white")
    target_x = 0
    for source_x in range(0, picture.width, 2):
        target_y = 0
        for source_y in range(0, picture.height, 2):
            color = picture.getpixel((source_x, source_y))
            canvas.putpixel((target_x, target_y), color)
            target_y += 1
        target_x += 1
    canvas.save("temp.png")


def image_functions(im):
    if style == "None":
        none(im)
    if style == "Sharpen":
        sharpen(im)
    if style == "Blur":
        blue(im)
    if style == "Negative":
        negative(im)
    if style == "Posterize":
        posterize(im)
    if style == "Black & White":
        black_white(im)
    if style == "Solarize":
        solarize(im)
    if style == "Thumbnail":
        thumbnail(im)
    if style == "Sepia":
        sepia(im)
#example to try
# im = Image.open("Output.jpg")
# negative(im)
