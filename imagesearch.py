#Author: Jason Ferrer
#Course: CST205
#Date: 12/10/2017
#Title: imagesearch.py
#Abstract: Function to grab images from API and also grab image based on search term
#Link to project: https://github.com/jferrer23/cst205-final-project

import requests
import json
from random import randint, random
from PIL import Image

def getimage(word, index):
    res = {'fields', 'comp'}
    url =\
    "https://api.gettyimages.com/v3/search/images?phrase="+word

    my_headers = {
        "Api-Key" : "7yx22tu46kd9ympu5w9r8jcf"
    }

    response = requests.get(url, headers=my_headers)#, params=res)
    json_body = response.json() # to translate into python
    b = randint(0,20)
    pic= str(json_body["images"][index]["display_sizes"][0]["uri"])
    im = Image.open(requests.get(pic, stream=True).raw)
    return im


picture = getimage("kitty", 0)
