#Course: CST205
#Title: main.py
#Authors: Jason Ferrer, Sean Quevedo, Manjit Gurcha
#Date: 12/10/2017
#Abstract: This is the main function file that creates the GUI
#           and applies the functions we created.


from imagesearch import (getimage)
from PIL import Image
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox, QGroupBox)
from PyQt5.QtCore import pyqtSlot
from PIL.ImageQt import ImageQt
from pygame import *
from img_filters import apply_filters

mixer.init()

music_list = {
    "None" : "",
    "Jazz" :"jazz.mp3",
    "Beachy" :"pink.mp3",
    "Reggae" : "reggae.mp3",
    "Drops of Jupiter" : "train.mp3",
    "Somewhere Over the Rainbow" : "rainbow.mp3"
}


#list of image filters for combobox
my_list = ["None", "Sharpen", "Blur", "Negative", "Posterize", "Black & White",
           "Solarize", "Thumbnail", "Sepia"]

image_list = []

class Window(QWidget):
    def __init__(self):
        super().__init__()
        starter_string = "Pick a Value"

        # App Title
        self.title_label = QLabel("<h1 style='text-align:center;'>Video Creator</h1>", self)

        # Search Layout
        search_layout = QVBoxLayout()
        search_box_layout = QHBoxLayout()

        # Search Widgets
        self.searcharea = QWidget()
        self.searchterm = QWidget()
        self.search_title_label = QLabel("Search for Images:", self)
        self.my_line_edit = QLineEdit(self)
        self.search_btn = QPushButton("Search", self)

        #Adding search widgets to  search layouts
        search_box_layout.addWidget(self.my_line_edit)
        search_box_layout.addWidget(self.search_btn)
        self.searchterm.setLayout(search_box_layout)
        search_layout.addWidget(self.search_title_label)
        search_layout.addWidget(self.searchterm)
        self.searcharea.setLayout(search_layout)

        # Resulting Image Search Layout
        result_image_layout = QVBoxLayout()
        filter_add_layout = QHBoxLayout()

        # Resulting Image Search Widgets
        self.resultimage = QWidget()
        self.filteradd = QWidget()
        self.pic_title = QLabel(self)
        self.pic = QLabel(self)
        self.my_filter_list = QComboBox()
        self.my_filter_list.addItems(my_list)
        self.add_img_btn = QPushButton("Add Pic to Vid", self)

        #Adding resulting image widgets to  resulting image layouts
        filter_add_layout.addWidget(self.my_filter_list)
        filter_add_layout.addWidget(self.add_img_btn)
        self.filteradd.setLayout(filter_add_layout)
        result_image_layout.addWidget(self.pic_title)
        result_image_layout.addWidget(self.pic)
        result_image_layout.addWidget(self.filteradd)
        self.resultimage.setLayout(result_image_layout)

        #sound layouts
        audio_box_layout = QVBoxLayout()
        add_music_layout = QHBoxLayout()
        #initializing the drop down menu for the user to choose sound\
        self.sound = QWidget()
        self.addsound = QWidget()
        self.audio_label = QLabel("Select your audio:")
        self.audio_dropdown = QComboBox()
        self.audio_dropdown.addItems(music_list)    #insert list of mp3 files into dropdown
        self.add_audio_btn = QPushButton("Add Audio to Vid", self)

        #Adding sound widgets to sound layouts
        add_music_layout.addWidget(self.audio_dropdown)
        add_music_layout.addWidget(self.add_audio_btn)
        self.addsound.setLayout(add_music_layout)

        audio_box_layout.addWidget(self.audio_label)
        audio_box_layout.addWidget(self.addsound)
        self.sound.setLayout(audio_box_layout)

        #Video Creation layouts
        video_box_layout = QVBoxLayout()
        video_btns_layout = QHBoxLayout()

        self.video_box = QWidget()
        self.video_btns = QWidget()
        self.video_create_label = QLabel("Create video using assets:")
        self.reset_btn = QPushButton("Reset Assets", self)
        self.create_vid_btn = QPushButton("Create Video", self)

        video_btns_layout.addWidget(self.reset_btn)
        video_btns_layout.addWidget(self.create_vid_btn)
        self.video_btns.setLayout(video_btns_layout)
        video_box_layout.addWidget(self.video_create_label)
        video_box_layout.addWidget(self.video_btns)
        self.video_box.setLayout(video_box_layout)

        # Main Box Layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.title_label)
        mainLayout.addWidget(self.searcharea)
        mainLayout.addWidget(self.resultimage)
        mainLayout.addWidget(self.sound)
        mainLayout.addWidget(self.video_box)

        self.setLayout(mainLayout)
        self.setWindowTitle("Image Search Engine")

        #Connecting Buttons to sockets
        self.search_btn.clicked.connect(self.search_image_on_click)
        self.add_img_btn.clicked.connect(self.add_img_btn_on_click)
        self.reset_btn.clicked.connect(self.reset_btn_on_click)
        self.create_vid_btn.clicked.connect(self.create_vid_btn_on_click)

        #Connecting Combo Boxes to sockets
        self.my_filter_list.currentIndexChanged.connect(self.apply_filter)



    @pyqtSlot()
    def search_image_on_click(self):
        line_edit_value = self.my_line_edit.text()
        if line_edit_value == "":
            self.pic_title.setText("<h2>Please enter search term in text box</h2>")
        else:
            try:
                global currentimage
                currentimage = getimage(line_edit_value,0)
                qimage = ImageQt(currentimage)
                pixmap = QtGui.QPixmap.fromImage(qimage)

                self.pic.setPixmap(pixmap)
            except IndexError:
                self.pic_title.setText("<h2>No Matching Images</h2>")

    @pyqtSlot()
    def add_img_btn_on_click(self):
        image_list.append(currentimage)

    @pyqtSlot()
    def reset_btn_on_click(self):
        image_list = []

    @pyqtSlot()
    def create_vid_btn_on_click(self):
        return

    #applies the filters to the images and saves the images
    @pyqtSlot()
    def apply_filter(self):
        img1 = currentimage.save("temp.png")
        img = Image.open("temp.png")
        apply_filters(self.my_filter_list.currentText(), img)
        return


app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())
