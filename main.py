#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore
from mainwindow_ui import Ui_MainWindow
import products
import random

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.database = products.database
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initSignals()
        self.key_buf = []
        self.ui.codeBox.setFocus()
        self.total_price = 0

    def initSignals(self):
        self.ui.quitButton.clicked.connect(self.close)
        self.ui.codeBox.returnPressed.connect(self.search_add_prod)
        self.ui.newButton.clicked.connect(self.new_list)


    def search_add_prod(self):
        search_code = str(self.ui.codeBox.text())
        self.ui.codeBox.setText("")
        print("Searching and adding code %s"%search_code)
        if self.database.has_key(search_code):
            price = self.database[search_code]["price"]
            human_name = self.database[search_code]["name"]
            pixmap = QtGui.QPixmap()
            pixmap.load("products/" + self.database[search_code]["picture"])
            pixmap = pixmap.scaledToWidth(self.ui.imgLabel.size().width())
            self.ui.imgLabel.setPixmap(pixmap)
        else:
            human_name = search_code
            price = int(random.random()*20)

        self.add_to_list(human_name,price)
        self.update_total()


    def add_to_list(self,product_name,price):
        self.ui.listProducts.addItem(product_name)
        self.ui.listPrices.addItem(str(price))
        self.ui.listProducts.scrollToBottom()
        self.ui.listPrices.scrollToBottom()
        self.total_price += price


    def update_total(self):
        self.ui.totalBox.setText("%d"%self.total_price)


    def new_list(self):
        self.total_price = 0
        self.ui.listProducts.clear()
        self.ui.listPrices.clear()
        self.update_total()
        self.ui.codeBox.setFocus()

    # def get_image


def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    ex.showFullScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()