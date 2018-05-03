# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monoGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(323, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(180, 240, 99, 27))
        self.connectButton.setObjectName("connectButton")
        self.gotoButton = QtWidgets.QPushButton(self.centralwidget)
        self.gotoButton.setGeometry(QtCore.QRect(180, 70, 99, 27))
        self.gotoButton.setObjectName("gotoButton")
        self.pickNM = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.pickNM.setGeometry(QtCore.QRect(40, 70, 131, 27))
        self.pickNM.setDecimals(2)
        self.pickNM.setMinimum(200.0)
        self.pickNM.setMaximum(1200.0)
        self.pickNM.setProperty("value", 700.0)
        self.pickNM.setObjectName("pickNM")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 323, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.gotoButton.setText(_translate("MainWindow", "GOTO"))
        self.pickNM.setSuffix(_translate("MainWindow", " [nm]"))

