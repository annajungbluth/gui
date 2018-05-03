#!/usr/bin/env python3

import serial
import time

import sys

# for the gui
from PyQt5 import QtCore, QtGui, QtWidgets
import template

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    QtWidgets.QMainWindow.__init__(self)
    
    # Set up the user interface from Designer
    self.ui = template.Ui_MainWindow()
    self.ui.setupUi(self)
    
    self.connected = False

    self.ui.gotoButton.clicked.connect(self.handleWavelengthButton)
    self.ui.connectButton.clicked.connect(self.connectToMono)
    
  def __del__(self):
    try:
      self.p.close()
    except:
      pass    
    
  def connectToMono(self):
    self.p = serial.Serial('/dev/ttyUSB0', 9600, timeout=0)
    self.p.write('HELLO\r'.encode())
    time.sleep(30)
    self.connected = self.waitForOK()

  def handleWavelengthButton(self):
      wavelength = self.ui.pickNM.value()
      self.chooseWavelength(wavelength)
  
  def chooseGrating(self, gratingNo):
    if self.connected:
      self.p.write('{:d} grating\r'.format(gratingNo).encode())
      self.waitForOK()
    else:
      print('Not Connected')
    
  def chooseWavelength(self, wavelength):
    if self.connected:
      self.p.write('{:.2f} GOTO\r'.format(wavelength).encode())
      self.waitForOK()
    else:
      print('Not Connected')
    
  def waitForOK(self):
    ret = False
    self.p.timeout = 30000
    shouldbEOk = self.p.readline()
    
    if (shouldbEOk == ' ok\r\n'.encode()) or (shouldbEOk == '  ok\r\n'.encode()):
        print('yay!')
        ret = True
    else:
        print('sad :-(')

    self.p.timeout = 0
    return ret


def main():
  app = QtWidgets.QApplication(sys.argv)
  monoUI = MainWindow()
  monoUI.show()
  sys.exit(app.exec_())

if __name__ == "__main__":
  main()
