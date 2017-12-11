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

    def initSignals(self):
        self.ui.quitButton.clicked.connect(self.close)




def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    ex.showFullScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()