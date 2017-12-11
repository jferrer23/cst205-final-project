#Author: Manjit Gurcha
#Course: CST205
#Date: 12/10/2017
#Title: rename_images.py
#Abstract:Renames the image files to "img{x}.png", where x is a number starting at 1 and moving upwards
#GitHub Link: https://github.com/jferrer23/cst205-final-project

import os

def rename_images():
    x = 1
    for i in os.listdir("."):
        if  i.endswith(".png"):
            os.rename(i, "img"+str(x)+".png")
            x+=1
