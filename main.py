#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui


class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):
        quitButton = QtGui.QPushButton("Quit")
        quitButton.clicked.connect(self.close)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(quitButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        # self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Cash Register')
        self.showFullScreen()




def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()