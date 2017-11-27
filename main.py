## Created by: Jason Ferrer
## Date: 10/9/2017
## CST205- Multimedia Design & Programming
## Description: This piece of code creates the GUI of an Enhanced Image Search Engine.
## It has a search box in which one can enter key words and when the search button
## is pressed, a corresponding picture is displayed if available. A filter drop box
## also exists with which one can apply on the image displayed.

from functions import (pickPic, applyFilter)
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox, QGroupBox)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap

my_list = ["none","sepia","grayscale","negative","thumbnail"]

class Window(QWidget):
    def __init__(self):
        super().__init__()
        starter_string = "Pick a Value"

        self.title_label = QLabel("<h1>Enhanced Image Search Engine</h1>", self)

        self.searchterm = QWidget()
        search_layout = QHBoxLayout()
        self.my_line_edit = QLineEdit(self)
        self.search_btn = QPushButton("Search", self)
        search_layout.addWidget(self.my_line_edit)
        search_layout.addWidget(self.search_btn)
        self.searchterm.setLayout(search_layout)

        self.my_combo_box = QComboBox()
        self.my_combo_box.addItems(my_list)

        self.result = QWidget()
        result_layout = QVBoxLayout()
        self.pic_title = QLabel(self)
        self.pic = QLabel(self)
        result_layout.addWidget(self.pic_title)
        result_layout.addWidget(self.pic)
        self.result.setLayout(result_layout)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.title_label)
        v_layout.addWidget(self.searchterm)
        v_layout.addWidget(self.my_combo_box)
        v_layout.addWidget(self.result)

        self.setLayout(v_layout)
        self.my_combo_box.currentIndexChanged.connect(self.update_ui)
        self.search_btn.clicked.connect(self.on_click)
        self.setWindowTitle("Image Search Engine")


    @pyqtSlot()
    def on_click(self):
        line_edit_value = self.my_line_edit.text()
        if line_edit_value == "":
            self.pic_title.setText("<h2>Please enter search term in text box</h2>")
        else:
            try:
                pictureInfo = pickPic(line_edit_value)
                self.pic_title.setText("<h2>"+pictureInfo[0]+"</h2>")
                imageUrl = "images/"+pictureInfo[1]+".jpg"
                picUrl = applyFilter(self.my_combo_box.currentText(),imageUrl)
                self.picmap = QPixmap(picUrl)
                self.pic.setPixmap(self.picmap)
            except IndexError:
                self.pic_title.setText("<h2>No Matching Images</h2>")

    @pyqtSlot()
    def update_ui(self):
        line_edit_value = self.my_line_edit.text()
        if line_edit_value == "":
            self.pic_title.setText("<h2>Please enter search term in text box</h2>")
        else:
            try:
                pictureInfo = pickPic(line_edit_value)
                self.pic_title.setText("<h2>"+pictureInfo[0]+"</h2>")
                imageUrl = "images/"+pictureInfo[1]+".jpg"
                picUrl = applyFilter(self.my_combo_box.currentText(),imageUrl)
                self.picmap = QPixmap(picUrl)
                self.pic.setPixmap(self.picmap)

            except IndexError:
                self.pic_title.setText("<h2>No Matching Images</h2>")


app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())
