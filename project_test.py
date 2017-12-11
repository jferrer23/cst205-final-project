#import pygame to use the Sound and Mixer libraries.
from pygame import *

#make a list of music files to be used for our slideshow application
#how it works: 1. let person choose a song and add it to the length of the video
#
music_list = ["jazz.mp3","pink.mp3","reggae.mp3","train.mp3","rainbow.mp3"]
mixer.init()


mixer.music.load(music_list[0])

mixer.music.play(1, 0.0)

while mixer.music.get_busy():
    time.Clock().tick()
