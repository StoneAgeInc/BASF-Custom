'''
DESCRIPTION:
    Main file to control BASF sensor prototype bring up. Starts all GUI functions and controls labjack.
    LabJack instance is set as a global parameter used in functions.
    Refer to to wiring diagram/hook up guide for connection details (:/FILENAME_HERE)

STATE:
    GUI launches and runs, labJack shows no errors. Not tested with actual sensors.

MODIFIED DATE: 7.12.19

Author: Chris Antle


Configuration Details:

Motor Direction I/O: DIO1
Motor
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
motorEnabled = False # Control for motor logic
handle = ""
microstep = 4000 # Microstep setting on Kollmorgen stepper drive


# Define I/O Pins
motorEnable = 5
motorDirectionPin = 1 # Defined as DIO pin number
motorEnablePin = 2 # Defined as DIO pin number
motorPWM = 0 # Defined as DIO pin number
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
        #self.ui.motorRunBtn.clicked.connect(lambda:self.motorRun())
        #self.ui.motorRunBtn.setText("STOP")

        self.ui.stepFwdBTN.clicked.connect(lambda:self.goStep(motorPWM, 1, self.ui.spinBox.value(),100, 0.1))
        self.ui.stepRevBTN.clicked.connect(lambda:self.goStep(motorPWM, 0, self.ui.spinBox.value(), 100, 0.1))
        self.ui.enableBTN.clicked.connect(lambda:self.enableMotorToggle())

        #labjack setup
        self.labJackSetUp()

    def labJackSetUp(self):
        global handle
        handle = ljm.openS("T7", "ANY", "ANY")  # T7 device, Any connection, Any identifier
        info = ljm.getHandleInfo(handle)
        print("Opened a LabJack with Device type: %i, Connection type: %i,\n"
              "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i" %
              (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5]))

    def motorRun(self):
       global motorDirection
       if motorEnabled:
            if fwd.ra

    def enableMotorToggle(self):
        global motorEnabled
        if self.ui.enableBTN.isChecked(): # If the motor is hot, disable it and reset
            motorEnabled = True
            ljm.eWriteName(handle, "DIO" + str(motorEnablePin), 0) # 0V high to disable motor
            self.ui.enableBTN.setText("DISABLE") # Reset label
        else:
            motorEnabled = False
            ljm.eWriteName(handle, "DIO" + str(motorEnablePin), 5)  # 5V high to disable motor
            self.ui.enableBTN.setText("ENABLE")  # Reset label

    '''
    Generates a specific number of pulse outputs for motor movement. 
    Assumes direction and enable are pre-configured
    Frequency calculation based on desired RPM and configured microstep
    Outputs on user-defined pin
    Assumes a low to high transition at 0, and computes high to low based on duty cycle
    Input duty cycle expressed as decimal (not percent)
    '''
    def goStep(self, pin, direction, steps, RPM, duty):
        if motorEnabled:
            ljm.eWriteName(handle, "DAC" + str(pin), direction)
            # Check output pin valid
            if pin == 0 or pin in range(2, 6):
                # Set up math
                clock = 80E6
                clockDivisor = 1
                lowToHigh = 0

                freq = RPM / ((1 / microstep) * 60)
                rollValue = (clock / clockDivisor) / freq
                dutyConfig = rollValue * duty
                clockFreq = clock / clockDivisor
                highToLow = duty * clockFreq + lowToHigh
                lowToHigh = 0

                # Enable clock
                ljm.eWriteName(handle, "DIO_EF_CLOCK0_DIVISOR", clockDivisor)
                ljm.eWriteName(handle, "DIO_EF_CLOCK0_ROLL_VALUE", rollValue)
                ljm.eWriteName(handle, "DIO_EF_CLOCK0_ENABLE", 1)

                # Configure pulse
                ljm.eWriteName(handle, "DIO" + str(pin) + "_EF_ENABLE", 0)
                ljm.eWriteName(handle, "DIO" + str(pin), 0)
                ljm.eWriteName(handle, "DIO" + str(pin) + "_EF_INDEX", 2)
                ljm.eWriteName(handle, "DIO" + str(pin) + "_EF_CONFIG_A", highToLow)
                ljm.eWriteName(handle, "DIO" + str(pin) + "_EF_CONFIG_B", lowToHigh)
                ljm.eWriteName(handle, "DIO" + str(pin) + "_EF_CONFIG_A", highToLow)
                ljm.eWriteName(handle, "DIO" + str(pin) + "_EF_CONFIG_C", steps)
                ljm.eWriteName(handle, "DIO" + str(pin) + "_EF_ENABLE", 1)

                # Print statement for debug
                print("Output Pin: " + str(pin))
                print("Total Steps Out: " + str(steps))
                print("Motor RPM: " + str(RPM))
                print("PWM Frequency: " + str(freq))
                print("PWM Duty Cycle: " + str(duty * 100))
                print("")

            else:
                print("IO Input Pin Not Valid *(T7 LabJack DIO 0, 2-5 ONLY)")
        else:
            print("MOTOR DISABLED")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = mywindow()
    # w.setStyleSheet("background-image: url(image.png)")
    w.show()
    sys.exit(app.exec_())
