## Created by: Jason Ferrer
## Date: 10/9/2017
## CST205- Multimedia Design & Programming
## Description: This piece of code contains the functions used to search for a picture
## based on search terms entered by user. It also has the functions that apply the
## filters chosen by the user.

import math
from PIL import Image
from pic_info import image_info

def pickPic(input_info):
    for i in range(len(image_info)):
        if input_info.lower() == image_info[i]["title"].lower():
            return [image_info[i]["title"],image_info[i]["id"]]

    searchterms = input_info.split()
    pic_titles = []
    image_value = 0
    for ii in range(len(image_info)):
        val = 0
        for i in range(len(searchterms)):
            for word in range(len(image_info[ii]["tags"])):
                if searchterms[i].lower() == image_info[ii]["tags"][word].lower():
                    val+=1

        if(val != 0):
            if image_value == val:
                    pic_titles.append(image_info[ii]["title"])
            elif image_value < val:
                image_value = val
                pic_titles = [image_info[ii]["title"]]

    sorted(pic_titles)
    for i in range(len(image_info)):
        if image_info[i]["title"] == pic_titles[0]:
            # return [pic_titles[0], image_info[i]["id"]]
            return [pic_titles[0], image_info[i]["id"]]

def applyFilter(filterChoice, imageUrl):
    picture = Image.open(imageUrl)

    if filterChoice == "none":
        picture.save("images/resultImage.jpg")
        return "images/resultImage.jpg"
    elif filterChoice == "sepia":
        sepiaFilter(picture)
        return "images/resultImage.jpg"
    elif filterChoice == "grayscale":
        grayscaleFilter(picture)
        return "images/resultImage.jpg"
    elif filterChoice == "negative":
        negativeFilter(picture)
        return "images/resultImage.jpg"
    elif filterChoice == "thumbnail":
        thumbnailFilter(picture)
        return "images/resultImage.jpg"

def sepiaFilter(picture):
    canvas = Image.new("RGB", (picture.width, picture.height), "white")

    target_x = 0
    for source_x in range(picture.width):
        target_y = 0
        for source_y in range(picture.height):

            color = picture.getpixel((source_x,source_y))

            outputRed = math.floor((color[0] * .393) + (color[1] *.769) + (color[2] * .189))
            outputGreen = math.floor((color[0] * .349) + (color[1] *.686) + (color[2] * .168))
            outputBlue = math.floor((color[0] * .272) + (color[1] *.534) + (color[2] * .131))

            if outputRed > 255:
                outputRed = 255
            if outputGreen > 255:
                outputGreen = 255
            if outputBlue > 255:
                outputBlue = 255

            color = (outputRed,outputGreen,outputBlue)

            canvas.putpixel((target_x,target_y), color)
            target_y += 1
        target_x += 1
    canvas.save("images/resultImage.jpg")

def grayscaleFilter(picture):
    canvas = Image.new("RGB", (picture.width, picture.height), "white")

    target_x = 0
    for source_x in range(picture.width):
        target_y = 0
        for source_y in range(picture.height):

            color = picture.getpixel((source_x,source_y))

            outputPixel = math.floor((color[0]+color[1]+color[2])/3)

            color = (outputPixel,outputPixel,outputPixel)

            canvas.putpixel((target_x,target_y), color)
            target_y += 1
        target_x += 1
    canvas.save("images/resultImage.jpg")

def negativeFilter(picture):
    canvas = Image.new("RGB", (picture.width, picture.height), "white")

    target_x = 0
    for source_x in range(picture.width):
        target_y = 0
        for source_y in range(picture.height):

            color = picture.getpixel((source_x,source_y))

            outputRed = 255 - color[0]
            outputGreen = 255 - color[1]
            outputBlue = 255 - color[2]

            color = (outputRed,outputGreen,outputBlue)

            canvas.putpixel((target_x,target_y), color)
            target_y += 1
        target_x += 1
    canvas.save("images/resultImage.jpg")

def thumbnailFilter(picture):
    canvas = Image.new("RGB", (math.ceil(picture.width/2), math.ceil(picture.height/2)), "white")

    target_x = 0
    for source_x in range(0,picture.width,2):
        target_y = 0
        for source_y in range(0,picture.height,2):

            color = picture.getpixel((source_x,source_y))

            canvas.putpixel((target_x,target_y), color)
            target_y += 1
        target_x += 1
    canvas.save("images/resultImage.jpg")
