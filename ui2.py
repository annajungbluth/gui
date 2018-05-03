#!/usr/bin/env python3

import serial
import time

import sys

# for the gui
from PyQt5 import QtCore, QtGui, QtWidgets
import template2

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    QtWidgets.QMainWindow.__init__(self)
    
    # Set up the user interface from Designer
    self.ui = template2.Ui_MainWindow()
    self.ui.setupUi(self)
    
    self.connected = False

    self.ui.gotoButton.clicked.connect(self.handleWavelengthButton)
    self.ui.connectButton.clicked.connect(self.connectToMono)
    self.ui.scanButton.clicked.connect(self.handleScanButton)
    self.ui.gratingButton.clicked.connect(self.handleGratingButtons)
 
   
    # Close connection when window is closed
  def __del__(self):        
    try:
      self.p.close()
    except:
      pass    


    # Establish serial connection to monochromator    
  def connectToMono(self):
    self.p = serial.Serial('/dev/ttyUSB0', 9600, timeout=0)
    self.p.write('HELLO\r'.encode())        # "Hello" initializes the monochromator
    time.sleep(30)      # Sleep function makes window time out. This is to avoid that the user sends signals while the monochromator is still initializing
    self.connected = self.waitForOK()       # Checks for OK response of monochromator

    # Check monochromator response
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
    
    # Set and GOTO wavelength
  def handleWavelengthButton(self):         # Function sets desired wavelength and calls chooseWavelength function
      wavelength = self.ui.pickNM.value()
      self.chooseWavelength(wavelength)
      
  def chooseWavelength(self, wavelength):       # Function to send GOTO command to monochromator
    if self.connected:
      self.p.write('{:.2f} GOTO\r'.format(wavelength).encode())
      self.waitForOK()
    else:
      print('Not Connected')

    # Set and move to grating 
  def handleGratingButtons(self):         # Function sets desired grating number and calls chooseGrating function
     if self.ui.Blaze_300.isChecked():
         gratingNo = 1
     elif self.ui.Blaze_750.isChecked():
         gratingNo = 2
     elif self.ui.Blaze_1600.isChecked():
         gratingNo = 3
     self.chooseGrating(gratingNo)
      
  def chooseGrating(self, gratingNo):
    if self.connected:
      self.p.write('{:d} grating\r'.format(gratingNo).encode())
      self.waitForOK()
    else:
      print('Not Connected')
    
    
    # Scan through wavelength range    
  def handleScanButton(self):
      start = self.ui.StartNM.value()
      stop = self.ui.StopNM.value()
      speed = self.ui.ScanSpeed.value()
      self.Scan(start, stop, speed)
       
  def Scan(self, start, stop, speed):
    if self.connected:
      self.p.write('{:.2f} GOTO\r'.format(start).encode())
      self.p.write('{:.2f} NM/MIN\r'.format(speed).encode())
      self.p.write('{:.2f} NM\r'.format(stop).encode())
    else:
      print('Not Connected')

           



def main():
  app = QtWidgets.QApplication(sys.argv)
  monoUI = MainWindow()
  monoUI.show()
  sys.exit(app.exec_())

if __name__ == "__main__":
  main()
