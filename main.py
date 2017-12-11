#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore
from mainwindow_ui import Ui_MainWindow

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initSignals()
        self.key_buf = []
        self.ui.codeBox.setFocus()
        self.total_price = 0

    def initSignals(self):
        self.ui.quitButton.clicked.connect(self.close)
        self.ui.codeBox.returnPressed.connect(self.search_add_prod)


    def search_add_prod(self):
        search_code = self.ui.codeBox.text()
        self.ui.codeBox.setText("")
        print("Searching and adding code %s"%search_code)
        # TODO
        price = 5
        human_name = "Milk"
        ##
        self.add_to_list(human_name,price)
        self.update_total()


    def add_to_list(self,product_name,price):
        self.ui.listProducts.addItem(product_name)
        self.ui.listProducts.scrollToBottom()
        self.total_price += price


    def update_total(self):
        self.ui.totalBox.setText("%d"%self.total_price)
def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()