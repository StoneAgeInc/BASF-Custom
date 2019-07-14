'''
DESCRIPTION:
    Main file to control BASF sensor prototype bring up. Starts all GUI functions and controls labjack.
    LabJack instance is set as a global parameter used in functions.
    Refer to to wiring diagram/hook up guide for connection details (:/FILENAME_HERE)

STATE:
    GUI launches and runs, labJack shows no errors. Not tested with actual sensors.

MODIFIED DATE: 7.13.19
Author: Chris Antle

Configuration Details:
Motor Direction I/O: DIO1
Motor
'''

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from labjack import ljm
from mainwindow import Ui_MainWindow

import time
import datetime
import numpy as np
import sys


# Define Globals
motorEnabled = False # Control for motor logic
handle = ""
microstep = 4000 # Microstep setting on Kollmorgen stepper drive
defaultFreq = 10000
defaultDuty = 0.05

# Define I/O Pins
motorEnable = 5
motorDirectionPin = 1 # Defined as DIO pin number
motorEnablePin = 1 # Defined as DAC pin number
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
        self.ui.stepFwdBTN.clicked.connect(lambda:self.goStep(motorPWM, 1, self.ui.spinBox.value(),100, 0.1))
        self.ui.stepRevBTN.clicked.connect(lambda:self.goStep(motorPWM, 0, self.ui.spinBox.value(), 100, 0.1))
        self.ui.enableBTN.clicked.connect(lambda:self.enableMotorToggle())
        self.ui.startStopBTN.clicked.connect(lambda:self.motorRun())

        #labjack setup
        self.labJackSetUp()

        #Set the default LCD info
        self.ui.PWMLCD.display(str(defaultFreq))


    def labJackSetUp(self):
        global handle
        handle = ljm.openS("T7", "ANY", "ANY")  # T7 device, Any connection, Any identifier
        info = ljm.getHandleInfo(handle)
        print("Opened a LabJack with Device type: %i, Connection type: %i,\n"
              "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i" %
              (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5]))

    def motorRun(self):
       global motorDirection
       if self.ui.startStopBTN.isChecked() and motorEnabled: # Motor stopped, so turn it on
            print("Turning Motor On")
            self.ui.startStopBTN.setText("STOP")
            if self.ui.fwdDirRadioBTN.isChecked(): # direction is forward, motor is enabled
                #begin PWM signal and write outputs high
                self.generateUserPWM(motorPWM,defaultFreq, defaultDuty) # Potentially change freq/duty based on desired RPM
                ljm.eWriteName(handle, "DIO" + str(motorDirectionPin), 1)
                print("Direction: Forward")
                print("")

            elif self.ui.revDirRadioBTN.isChecked(): # reverse direction
                self.generateUserPWM(motorPWM, defaultFreq, defaultDuty) # Potentially change freq/duty based on desired RPM
                ljm.eWriteName(handle, "DIO" + str(motorDirectionPin), 0)
                print("Direction: Reverse")
                print("")

       elif not self.ui.startStopBTN.isChecked() and motorEnabled: #Motor running, stop it
           print("Turning Motor Off")
           print("")
           self.ui.startStopBTN.setText("START")
           ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 5) #5V high to disablemotor

       else: # Motor disabled
           prompt = QMessageBox.warning(self, 'Motor Disabled',
                                                 'Motor disabled - enable to run',
                                                 QMessageBox.Ok | QMessageBox.Cancel)
           if prompt == QMessageBox.Ok:
               print("Ok")
               self.ui.startStopBTN.setChecked(False)
           else:
               sys.exit(app.exec_())

    def enableMotorToggle(self):
        global motorEnabled
        if self.ui.enableBTN.isChecked(): # Motor is turned on
            print("Motor Enabled")
            print("")
            motorEnabled = True
            ljm.eWriteName(handle, "DIO" + str(motorEnablePin), 0) # 0V high to enable
            self.ui.enableBTN.setText("DISABLE") # Reset label
        else:
            print("Motor Disabled")
            print("")
            motorEnabled = False
            ljm.eWriteName(handle, "DIO" + str(motorEnablePin), 5)  # 5V high to disable motor
            self.ui.enableBTN.setText("ENABLE")  # Reset label
            self.ui.startStopBTN.setChecked(False)
            self.ui.startStopBTN.setText("START")
            self.ui.motorRPMLCD.display(str(0))
            self.ui.PWMLCD.display(str(defaultFreq))

    '''
    Generates a specific number of pulse outputs for motor movement. 
    Assumes direction and enable are pre-configured
    Frequency calculation based on desired RPM and configured microstep
    Outputs on user-defined pin
    Assumes a low to high transition at 0, and computes high to low based on duty cycle
    Input duty cycle expressed as decimal (not percent)
    '''
    def goStep(self, pin, direction, steps, RPM, duty):
        if motorEnabled and steps > 0:
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

                self.ui.motorRPMLCD.display(str(RPM))
                self.ui.PWMLCD.display(str(freq))

            else:
                print("IO Input Pin Not Valid *(T7 LabJack DIO 0, 2-5 ONLY)")
        elif motorEnabled:
            prompt = QMessageBox.warning(self, 'Step Size Error',
                                         'Zero step size - no movement possible',
                                         QMessageBox.Ok | QMessageBox.Cancel)
            if prompt == QMessageBox.Ok:
                print("Ok")

        else:
            print("MOTOR DISABLED")
            prompt = QMessageBox.warning(self, 'Motor Disabled',
                                         'Motor disabled - enable to run',
                                         QMessageBox.Ok | QMessageBox.Cancel)
            if prompt == QMessageBox.Ok:
                print("Ok")

    '''
    Creates a user-defined PWM signal with variables of output pin, frequency, and duty cycle
    RPM calculation depends on microstep size
    Assumes 80MHz clock and clock divisor of 1
    T7 Pro valid PWM outputs are 0, 2-5 only
    '''
    def generateUserPWM(self, pin, freq, duty):
        # Check output pin valid
        if pin == 0 or pin in range(2, 6):
            # Set up math
            clock = 80E6
            clockDivisor = 1
            rollValue = (clock / clockDivisor) / freq
            dutyConfig = rollValue * duty
            RPM = (1 / microstep) * freq * 60

            # Print statements for debug
            print("Output Pin (DIO): " + str(pin))
            print("PWM Frequency (Hz): " + str(freq))
            print("Roll Value: " + str(rollValue))
            print("Duty Cycle (%): " + str(duty * 100))
            print("Motor RPM: " + str(RPM))
            print(" ")

            self.ui.motorRPMLCD.display(str(RPM))
            self.ui.PWMLCD.display(str(freq))

            # Configure Clock Registers:
            ljm.eWriteName(handle, "DIO_EF_CLOCK0_ENABLE", 0)  # Disable clock source
            # Set Clock0's divisor and roll value to configure frequency: 80MHz/1/80000 = 1kHz
            ljm.eWriteName(handle, "DIO_EF_CLOCK0_DIVISOR", clockDivisor)  # Configure Clock0's divisor
            # ljm.eWriteName(handle, "DIO_EF_CLOCK0_ROLL_VALUE", 80000)# Configure Clock0's roll value
            ljm.eWriteName(handle, "DIO_EF_CLOCK0_ROLL_VALUE", rollValue)  # Configure Clock0's roll value
            ljm.eWriteName(handle, "DIO_EF_CLOCK0_ENABLE", 1)  # Enable the clock source

            # Configure EF Channel Registers for signal:
            ljm.eWriteName(handle, "DIO" + str(pin) + "_EF_ENABLE",
                           0)  # Disable the EF system for initial configuration
            ljm.eWriteName(handle, "DIO" + str(pin) + "_EF_INDEX", 0)  # Configure EF system for PWM
            ljm.eWriteName(handle, "DIO" + str(pin) + "_EF_OPTIONS", 0)  # Configure what clock source to use: Clock0
            ljm.eWriteName(handle, "DIO" + str(pin) + "_EF_CONFIG_A", dutyConfig)  # Configure duty cycle to be: 50%
            ljm.eWriteName(handle, "DIO" + str(pin) + "_EF_ENABLE",
                           1)  # Enable the EF system, PWM wave is now being outputted

        else:
            print("IO Input Pin Not Valid *(T7 LabJack DIO 0, 2-5 ONLY)")

    def sampleData(self):
        # test = datetime.datetime.now().strftime("%H:%M:%S")
        # print(test)
        timeStamp = datetime.datetime.now().strftime("%H:%M:%S")
        V1 = ljm.eReadName(handle, pressureVoltage)  # Sample labjack analog input 1
        #V2 = ljm.eReadName(handle, "AIN1")  # Sample labjack analog input 2
        P1 = 61.121 * V1 - 43.622
        #P2 = 61.121 * V2 - 43.622

        pressureSample = [timeStamp, P1, P2]  # add data to local list

        self.ui.pressureLCD1.display(P1)  # display data on GUI
        #self.ui.pressureLCD2.display(P2)  # display data on GUI

        # Print for debug
        # print("P1 Voltage Reading: " + str(P1))
        # print("P2 Voltage Reading: " + str(P2))

        #return pressureSample

    def plotSessionData(self, sessionData):
        self.ui.plotWidget.clear()
        self.ui.plotWidget.addLegend()
        curve1 = self.ui.plotWidget.plot(pen='r', name="P1")
        #curve2 = self.ui.plotWidget.plot(pen='g', name="P2")
        P1 = []
        #P2 = []
        i = 0

        for set in sessionData:  # grab invidudal data points and make a list of just pressure values
            P1.append(sessionData[i][1])
            #P2.append(sessionData[i][2])
            i += 1

        curve1.setData(P1)
        #curve2.setData(P2)
        # app.processEvents()
        timer = QtCore.QTimer()
        P1A = np.array(P1)
        #P2A = np.array(P2)

        def update():
            global curve1, curve2, P1A
            curve1.setData(P1A)
            #curve2.setData(P2A)

        timer.timeout.connect(update)
        timer.start(100)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = mywindow()
    # w.setStyleSheet("background-image: url(image.png)")
    w.show()
    sys.exit(app.exec_())
