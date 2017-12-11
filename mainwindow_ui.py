# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../register.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(620, 488)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.gridLayout.addWidget(self.quitButton, 2, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.imgLabel = QtGui.QLabel(self.centralwidget)
        self.imgLabel.setFrameShape(QtGui.QFrame.Box)
        self.imgLabel.setObjectName(_fromUtf8("imgLabel"))
        self.gridLayout.addWidget(self.imgLabel, 1, 0, 1, 1)
        self.codeBox = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.codeBox.setFont(font)
        self.codeBox.setObjectName(_fromUtf8("codeBox"))
        self.gridLayout.addWidget(self.codeBox, 0, 0, 1, 2)
        self.totalBox = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.totalBox.setFont(font)
        self.totalBox.setObjectName(_fromUtf8("totalBox"))
        self.gridLayout.addWidget(self.totalBox, 2, 1, 1, 1)
        self.listProducts = QtGui.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.listProducts.setFont(font)
        self.listProducts.setObjectName(_fromUtf8("listProducts"))
        self.gridLayout.addWidget(self.listProducts, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 50)
        self.gridLayout.setRowStretch(0, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.quitButton.setText(_translate("MainWindow", "Quit", None))
        self.label.setText(_translate("MainWindow", "Total Price", None))
        self.imgLabel.setText(_translate("MainWindow", "Product Image", None))

