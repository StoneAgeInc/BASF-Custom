from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap

from PyQt5.QtWidgets import *
from labjack import ljm
import time

from mainwindow import Ui_MainWindow

import sys


# Define Globals
motorEnabled = False # Initially have motor stopped
motorFreq = 1000 # Hz
motorDuty = 50 # %
position = True


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # set up button control
        self.ui.motorRunBtn.clicked.connect(lambda:self.motorRun())
        #self.updateProxBar()
        self.ui.motorRunBtn.setText("change")


    def motorRun(self):
        # Check that the motor isn't stopped
        if self.ui.motorRadioStop.isChecked():
            print ("Motor in STOP condition")
        else:
            global motorEnabled

            if motorEnabled and not self.ui.motorRadioStop.isChecked():
                #motorEnabled = not motorEnabled
                print ("Motor Stopped")
                print (" ")
            else:
                print ("Motor Started")
                print (" ")
            motorEnabled = not motorEnabled
        print(str(motorEnabled))

    def motorSpeedCalc(self):
        print("Calculating Motor Speed")
        print(" ")

    def sampleProx(self):
        print("Sampling Proximity Sensor")

    def labJackSetUp(self):
        handle = ljm.openS("T7", "ANY", "ANY")  # T7 device, Any connection, Any identifier
        info = ljm.getHandleInfo(handle)
        print("Opened a LabJack with Device type: %i, Connection type: %i,\n"
              "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i" %
              (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5]))

    # def updateProxBar(self):
    #     global position
    #     print("Updating progress bar")
    #     #self.proxProgBar = QtGui.QProgressBar('', self)
    #     if position:
    #         print("Prox detected")
    #         self.ui.proxProgBar.setValue(100)
    #     else:
    #         print("Prox not detected")
    #         self.ui.proxProgBar.setValue(0)
    #     position = not position
    #     time.sleep(1)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = mywindow()
    # w.setStyleSheet("background-image: url(image.png)")
    w.show()
    sys.exit(app.exec_())
