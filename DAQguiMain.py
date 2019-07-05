'''
DESCRIPTION:
    Main file to control BASF sensor prototype bring up. Starts all GUI functions and controls labjack.
    LabJack instance is set as a global parameter used in functions.
    Refer to to wiring diagram/hook up guide for connection details (:/FILENAME_HERE)

STATE:
    GUI launches and runs, labJack shows no errors. Not tested with actual sensors.

MODIFIED DATE:
    June 3, 2019

Author:
    Chris Antle
'''

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

#define labjack I/O names
motorEnable = "DAC0"
motorDirection = "DIO0"
motorPWM = "DIO1"
pressureVoltage = "AIN0"
proxStopLow = "AIN6"
proxStopHigh = "AIN7"
loadCellOutput = "AIN1"


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # set up button control
        self.ui.motorRunBtn.clicked.connect(lambda:self.motorRun())
        #self.ui.motorRunBtn.setText("STOP")
        #self.updateProxBar(

        #labjack setup
        global handle
        handle = ljm.openS("T7", "ANY", "ANY")  # T7 device, Any connection, Any identifier
        info = ljm.getHandleInfo(handle)
        print("Opened a LabJack with Device type: %i, Connection type: %i,\n"
              "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i" %
              (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5]))

        deviceType = info[0]


    def motorRun(self):
        # Check that the motor isn't stopped
        if self.ui.motorRadioStop.isChecked():
            #self.ui.motorRunBtn.setDisabled(True)
            print ("Motor in STOP condition")
        else:
            global motorEnabled, motorDirection
            if motorEnabled and not self.ui.motorRadioStop.isChecked(): #motor is running, click to stop
                #motorEnabled = not motorEnabled
                print("Motor Stopped")
                print(" ")
                self.ui.motorRunBtn.setText("RUN") #change label for next state
            else: #motor is stopped, click to start running
                print("Motor Started")
                #print(" ")
                #Determine motor direction and set parameter
                if self.ui.motorRadioFWD.isChecked():
                    motorDirection = 1
                    print("Direction: Forward")
                elif self.ui.motorRadioREV.isChecked():
                    motorDirection = 0
                    print("Direction: Reverse")
                else:
                    print("No direction defined: ERROR")
                self.ui.motorRunBtn.setText("STOP") #change label for next state

            motorEnabled = not motorEnabled
        print(str(motorEnabled))

    '''
    Start the PWM signal and configure a test pin to check.
    Hard coded to test generate signal on DIO1 and test on DIO3
    '''
    def startPWM(self, pin, dutyCycle, targetFreq):
        pin = motorPWM

        # Set up the clock
        DIO_EF_CLOCK0_ENABLE = 0
        DIO_EF_CLOCK0_DIVISOR = 1
        DIO_EF_CLOCK0_ROLL_VALUE = (80e6) / (DIO_EF_CLOCK0_DIVISOR * targetFreq)  # based on 80MHz clock
        DIO_EF_CLOCK0_ENABLE = 1

        # Set up PWM signal
        DIO1_EF_ENABLE = 0
        DIO1_EF_INDEX = 0
        DIO1_EF_CONFIG_A = (dutyCycle * (8000 / 100))
        DIO1_EF_ENABLE = 1
        DIO_DUTY_CYCLE = 80000 * (dutyCycle / 100)

        # Set up signal check for DIO3
        DIO3_EF_ENABALE = 0
        DIO3_EF_INDEX = 5
        DIO3_EF_OPTONS = 0
        DIO3_EF_ENABALE = 1

        print("Roll Value: " + str(DIO_EF_CLOCK0_ROLL_VALUE))
        print("CONFIG A: " + str(DIO1_EF_CONFIG_A))
        print("Configuring clock.....")

        # Configure Clock Registers:
        ljm.eWriteName(handle, "DIO_EF_CLOCK0_ENABLE", 0)  # Disable clock source
        # Set Clock0's divisor and roll value to configure frequency: 80MHz/1/80000 = 1kHz
        ljm.eWriteName(handle, "DIO_EF_CLOCK0_DIVISOR", 1)  # Configure Clock0's divisor
        # ljm.eWriteName(handle, "DIO_EF_CLOCK0_ROLL_VALUE", 80000)# Configure Clock0's roll value
        ljm.eWriteName(handle, "DIO_EF_CLOCK0_ROLL_VALUE", DIO_EF_CLOCK0_ROLL_VALUE)  # Configure Clock0's roll value
        ljm.eWriteName(handle, "DIO_EF_CLOCK0_ENABLE", 1)  # Enable the clock source

        # Configure EF Channel Registers for signal:
        ljm.eWriteName(handle, "DIO1_EF_ENABLE", 0)  # Disable the EF system for initial configuration
        ljm.eWriteName(handle, "DIO1_EF_INDEX", 0)  # Configure EF system for PWM
        ljm.eWriteName(handle, "DIO1_EF_OPTIONS", 0)  # Configure what clock source to use: Clock0
        # ljm.eWriteName(handle, "DIO0_EF_CONFIG_A",40000)# Configure duty cycle to be: 50%
        ljm.eWriteName(handle, "DIO1_EF_CONFIG_A", DIO_DUTY_CYCLE)  # Configure duty cycle to be: 50%
        ljm.eWriteName(handle, "DIO1_EF_ENABLE", 1)  # Enable the EF system, PWM wave is now being outputted

        # Configure EF Channel Registers for digital input check:
        ljm.eWriteName(handle, "DIO3_EF_ENABLE", 0)
        ljm.eWriteName(handle, "DIO3_EF_INDEX", 5)
        ljm.eWriteName(handle, "DIO3_EF_OPTIONS", 0)
        ljm.eWriteName(handle, "DIO3_EF_ENABLE", 1)

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
