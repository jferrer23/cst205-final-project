#Author: Manjit Gurcha
#Course: CST205
#Date: 12/10/2017
#Title: Image Filters
#Abstract: FIlters to be applied to the images selected by the user
#GitHub Link: https://github.com/jferrer23/cst205-final-project

from PIL import Image, ImageFilter, ImageOps

#no filter
def none (picture):
    picture.save("img1.png")
    img = Image.open("img1.png")
    img.resize((600,600)).save("img1.png")

#posterize image
def posterize(picture):
    picture = ImageOps.posterize(picture, 1)
    picture.save("img2.png")
    img = Image.open("img2.png")
    img.resize((600,600)).save("img2.png")

def solarize(picture):
    picture = ImageOps.solarize(picture)
    picture.save("img3.png")
    img = Image.open("img3.png")
    img.resize((600,600)).save("img3.png")

#sharpen image
def sharpen(picture):
    picture = picture.filter(ImageFilter.EDGE_ENHANCE)
    picture.save("img4.png")
    img = Image.open("img4.png")
    img.resize((600,600)).save("img4.png")
    

#convert to black & white
def black_white(picture):
    picture = picture.convert("1")
    picture.save("img5.png")
    img = Image.open("img5.png")
    img.resize((600,600)).save("img5.png")

#blur image
def blur(picture):
    picture = picture.filter(ImageFilter.BLUR)
    picture.save("img6.png")
    img = Image.open("img6.png")
    img.resize((600,600)).save("img6.png")

#negative image
def negative(picture):
    picture = ImageOps.invert(picture)
    picture.save("img7.png")
    img = Image.open("img7.png")
    img.resize((600,600)).save("img7.png")

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
    picture.save("img8.png")
    img = Image.open("img8.png")
    img.resize((600,600)).save("img8.png")

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
    canvas.save("img9.png")
    img = Image.open("img9.png")
    img.resize((600,600)).save("img9.png")


#to use with combo box in gui
def apply_filters(style, image):
    if style == "None":
        none(image)
    if style == "Sharpen":
        sharpen(image)
    if style == "Blur":
        blue(image)
    if style == "Negative":
        negative(image)
    if style == "Posterize":
        posterize(image)
    if style == "Black & White":
        black_white(image)
    if style == "Solarize":
        solarize(image)
    if style == "Thumbnail":
        thumbnail(image)
    if style == "Sepia":
        sepia(image)
