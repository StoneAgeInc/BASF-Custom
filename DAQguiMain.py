'''
DESCRIPTION:
    Main file to control BASF sensor prototype bring up. Starts all GUI functions and controls labjack.
    LabJack instance is set as a global parameter used in functions.
    Refer to to wiring diagram/hook up guide for connection details (:/FILENAME_HERE)
STATE:
    GUI launches and runs, labJack shows no errors. Not tested with actual sensors. Real time plotting working with
    two independent axis, two tabs that are for manual control and life cycle testing.
    Motor control debugged and working, and will stop on AIN0 voltage flag. LCD will update, but real-time plot bogs
    down program and does not seem to be working.
MODIFIED DATE: 9.12.19
Author: Chris Antle
Configuration Details:
Motor Direction I/O: DIO1
Motor
'''

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from labjack import ljm
from mainwindow import Ui_MainWindow
import pyqtgraph as pg
import threading
from threading import Lock
import time
import datetime
from datetime import timedelta
import numpy as np
import sys
import traceback


# Define Globals
motorEnabled = False # Control for motor logic
lifeTestMotorDirection = 1 # Assume motor starts in forward direction
lifeTestActive = False
handle = ""
microstep = 200 # Microstep setting on Kollmorgen stepper drive
defaultFreq = 10000# Default PWM Freq
defaultDuty = 0.9
defaultsampleFreq = 1 # Defined in Hz

#Life Test Globals
startTime = 0
endTime = 0
runPeriod = 0

# Define I/O Pins
motorEnable = 5 #5V high to disable motors
motorDirectionPin = 1 # Defined as DIO pin number
motorEnablePin = 1 # Defined as DAC pin number
motorPWM = 0 # Defined as DIO pin number
pressureVoltage = "AIN0"
loadVoltage = "AIN1"
px1Low = "AIN3" # Tool stop, pin 1 EuroSwitch Prox Sensor
px1High = "AIN2" # Tool stop, pin 3, EuroSwitch Prox Sensor, updated or switch polarity
px2Low = "AIN8" # RPM1
px2High = "AIN9" # RPM1
px3Low = "AIN10" # RPM2
px3High = "AIN11" # RPM2

#Define prox style sheet for toggle
redProxStyle = "QRadioButton::indicator {width: 15px; height: 15px; border-radius: 7px;}"\
               "QRadioButton::indicator:unchecked { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "\
               "stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5)); border: 2px solid gray;}"

greenProxStyle = "QRadioButton::indicator {width: 15px; height: 15px; border-radius: 7px;}" \
                 "QRadioButton::indicator:unchecked {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1," \
                 "stop: 0 rgb(0, 242, 0), " \
                 "stop: 1 rgb(0, 170, 0)); border: 2px solid gray;}"

yellowProxStyle = "QRadioButton::indicator {width: 15px; height: 15px; border-radius: 7px;}" \
                 "QRadioButton::indicator:unchecked {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1," \
                 "stop: 0 rgb(242, 242, 0), " \
                 "stop: 1 rgb(170, 142, 0)); border: 2px solid gray;}"

#set up locks
enableLock = Lock()

class Task(QtCore.QObject):
    updated = QtCore.pyqtSignal(int, int)
    def __init__(self):
        """ If useEmit True, emits a signal. If False, uses a callback. """
        super(Task, self).__init__()
        self.useEmit = True

class Worker(QRunnable):
    '''
    Worker thread
    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.
    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function
    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.T1.setCurrentIndex(0)
        self.lifeTestParamClear() #Null life test parameters
        self.ui.lifeTestProgBar.setValue(0.0)

        #Plot set up
        self.ui.plotWidget.setBackground(background=None)
        self.ui.plotWidget.setBackground(background=[0, 0, 0, 80])
        self.ui.plotWidget.setYRange(-1000,1000)
        self.ui.plotWidget.setTitle(title="Real Time Sensor Output")
        self.ui.plotWidget.showGrid(True, True, 0.5)
        self.ui.plotWidget.setLimits(xMin=0, xMax=None, yMin=None, yMax=None)
        self.ui.plotWidget.setLabel('bottom', 'Elapsed Time', 's')
        self.ui.plotWidget.setLabel('left', 'Pressure', 'PSI')
        self.ui.plotWidget.setLabel('right', 'Force', 'Lbf')

        # set up button control
        # Control tab
        self.ui.stepFwdBTN.clicked.connect(lambda:self.goStep(motorPWM, 1, self.ui.spinBox.value(),100, 0.1))
        self.ui.stepRevBTN.clicked.connect(lambda:self.goStep(motorPWM, 0, self.ui.spinBox.value(), 100, 0.1))
        self.ui.enableBTN.clicked.connect(lambda:self.enableMotorToggle())
        self.ui.startStopBTN.clicked.connect(lambda:self.motorRun())
        self.ui.sensorBTN.clicked.connect(lambda:self.runSensorSession())
        self.ui.proxRadio1.setStyleSheet(greenProxStyle)
        self.ui.proxRadio2.setStyleSheet(greenProxStyle)
        self.ui.proxRadio3.setStyleSheet(greenProxStyle)

        # Life cycle tab
        self.ui.paramSaveBTN.clicked.connect(lambda:self.lifeTestParamSample())
        self.ui.paramClearBTN.clicked.connect(lambda:self.lifeTestParamClear())
        self.ui.lifeCycleStartBTN.clicked.connect(lambda:self.simpleLifeTest())
        self.ui.lifeCycleSuspendBTN.clicked.connect(lambda:self.lifeTestSuspend())
        self.ui.proxLifeRadio1.setStyleSheet(greenProxStyle)
        self.ui.proxLifeRadio2.setStyleSheet(greenProxStyle)
        self.ui.proxLifeRadio3.setStyleSheet(greenProxStyle)
        self.ui.RPMinEdit.setText("25")
        self.ui.RPMoutEdit.setText("100")

        #labjack setup
        self.labJackSetUp()

        #Set the default LCD info
        self.ui.PWMLCD.display(0)
        self.ui.pressureLCD1.display(0.0)# display data on GUI

        #Ensure motor is off
        ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 5) # 0V high to disable
        ljm.eWriteName(handle, "DIO" + str(motorPWM) + "_EF_ENABLE", 0)  # Disable the EF system

        #Set up threading
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        #set up locks
        enableLock = Lock()
        self.redrawLock = Lock()


    def labJackSetUp(self):
        global handle
        handle = ljm.openS("T7", "ANY", "ANY")  # T7 device, Any connection, Any identifier
        info = ljm.getHandleInfo(handle)
        print("Opened a LabJack with Device type: %i, Connection type: %i,\n"
              "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i" %
              (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5]))

    def lifeTestParamSample(self):
        global runTime, cutOffForce, stepsOut, stepsIn, RPMout, RPMin
        # Get variables from line edit
        runTime = int(self.ui.runTimeEdit.text())
        cutOffForce = int(self.ui.forceCutOffEdit.text())
        stepsOut = int(self.ui.stepsOutEdit.text())
        stepsIn = int(self.ui.stepsInEdit.text())
        RPMout = int(self.ui.RPMoutEdit.text())
        RPMin = int(self.ui.RPMinEdit.text())

    def lifeTestParamClear(self):
        global runTime, cutOffForce, stepsOut, stepsIn, RPMout, RPMin
        runTime = 0
        cutOffForce = 0
        stepsOut = 0
        stepsIn = 0
        RPMout = 0
        RPMin = 0

        self.ui.runTimeEdit.setText(str(runTime))
        self.ui.forceCutOffEdit.setText(str(cutOffForce))
        self.ui.stepsOutEdit.setText((str(stepsOut)))
        self.ui.stepsInEdit.setText(str(stepsIn))
        self.ui.RPMoutEdit.setText(str(RPMout))
        self.ui.RPMinEdit.setText(str(RPMin))

    '''
    Life Cycle Test alternate function
    Based off of hose reel hard calculations
    Assume that "steps out" can be swapped for "feet out" and a total run time determined from that value 
    NOT USED
    '''
    def lifeTest2(self):
        print("Starting Life Cycle Started")
        global runTime, cutOffForce, stepsOut, stepsIn, RPMout, RPMin, lifeTest, lifeTestMotorDirection, motorEnabled
        self.lifeTestParamSample()  # sample the user-input and get values (assigned to global)
        lifeTest = True
        motorEnabled = True  # Hardcode motor enabled option

        # Configure runTime
        # startTime = datetime.datetime.now().strftime("%H:%M:")
        startTime = datetime.datetime.now().strftime("%H:%M")
        endTime = (datetime.datetime.now() + timedelta(minutes=runTime)).strftime("%H:%M")
        runPeriod = timedelta(minutes=runTime)
        stopTime = datetime.datetime.now() + runPeriod
        minutes = 0
        # Print to check
        print("Start Time: " + startTime)
        print("End Time: " + endTime)
        print("")

        while lifeTest:
            progBarVal = 100 * ((runPeriod - (stopTime - datetime.datetime.now())) / runPeriod)
            self.ui.lifeTestProgBar.setValue(progBarVal)

            if datetime.datetime.now() <= stopTime:  # Check that the test is still live
                print("Life Test Active")
                progBarVal = 100 * ((runPeriod - (stopTime - datetime.datetime.now())) / runPeriod)
                self.ui.lifeTestProgBar.setValue(progBarVal)

                if motorEnabled:  # Check that the motor is hot
                    if lifeTestMotorDirection == 1:  # Motor is going forward/out
                        print("Motor Direction: Forward")
                        print("Feet Out: ")
                        calcedVal = 30
                        testEpoch = timedelta(seconds=30)
                        localStop = datetime.datetime.now() + testEpoch
                        freq = 1000
                        ljm.eWriteName(handle, "DIO" + str(motorDirectionPin), lifeTestMotorDirection)
                        self.generateUserPWM(motorPWM, freq,
                                             defaultDuty)  # Potentially change freq/duty based on desired RPM
                        print("Running Motor Forward")
                        print("Timer Started")
                        time.sleep(calcedVal)
                        print("Timer Ended")
                        print("")

                        lifeTestMotorDirection = 0  # Reset motor direction once loop executes
                        print("Changing Motor Direction")
                        print("---------------------------------------------------------------------")

                    elif lifeTestMotorDirection == 0:  # Motor is going reverse/in
                        print("Motor Direction: Reverse")
                        print("Feet Out: ")
                        calcedVal = 30
                        testEpoch = timedelta(seconds=30)
                        localStop = datetime.datetime.now() + testEpoch
                        freq = 1000
                        ljm.eWriteName(handle, "DIO" + str(motorDirectionPin), lifeTestMotorDirection)
                        self.generateUserPWM(motorPWM, freq,
                                             defaultDuty)  # Potentially change freq/duty based on desired RPM

                        print("Running Motor Reverse")
                        print("Timer Started")
                        time.sleep(calcedVal)
                        print("Timer Ended")
                        print("")

                        lifeTestMotorDirection = 0  # Reset motor direction once loop executes
                        print("Changing Motor Direction")
                        print("---------------------------------------------------------------------")
                    else:
                        print("Motor Direction Out of Range")

            else:
                lifeTest = False

        self.ui.lifeTestProgBar.setValue(100)
        print("")
        print("End Life Test Run")
        print("")


    def lifeCycleRun(self):
        print("Starting Life Cycle Started")
        global runTime, cutOffForce, stepsOut, stepsIn, RPMout, RPMin, lifeTest, lifeTestMotorDirection, motorEnabled
        self.lifeTestParamSample() # sample the user-input and get values (assigned to global)
        lifeTest = True
        motorEnabled = True #Hardcode motor enabled option

        #Configure runTime
        #startTime = datetime.datetime.now().strftime("%H:%M:")
        startTime = datetime.datetime.now().strftime("%H:%M")
        endTime = (datetime.datetime.now() + timedelta(minutes=runTime)).strftime("%H:%M")
        runPeriod = timedelta(minutes=runTime)
        stopTime = datetime.datetime.now() + runPeriod
        minutes = 0
        # Print to check
        print("Start Time: " + startTime)
        print("End Time: " +  endTime)
        print("")

        while lifeTest:
            progBarVal = 100*((runPeriod-(stopTime - datetime.datetime.now()))/runPeriod)
            self.ui.lifeTestProgBar.setValue(progBarVal)

            if datetime.datetime.now() <= stopTime: #Check that the test is still live
                print("Life Test Active")
                if motorEnabled: # Check that the motor is hot
                    if lifeTestMotorDirection == 1: # Motor is going forward/out
                        print("Motor Direction: Forward")
                        print("Going Steps: " + str(stepsOut))
                        localStep = 0
                        while localStep <= stepsOut:
                            self.goStep(motorPWM, lifeTestMotorDirection,5,RPMout,0.1)# jump 5 step increments
                            # Check load cell and limit switches
                            time.sleep(0.1) # 100ms pause
                            localStep += 1

                        lifeTestMotorDirection = 0 #Reset motor direction once loop executes
                        time.sleep(1)
                        print("Changing Motor Direction")
                        print("---------------------------------------------------------------------")

                    elif lifeTestMotorDirection == 0: # Motor is going reverse/in
                        print("Motor Direction: Reverse")
                        print("Going Steps: " + str(stepsIn))
                        localStep = 0
                        while localStep <= stepsIn:
                            self.goStep(motorPWM, lifeTestMotorDirection, 5, RPMin, 0.1)  # jump 5 step increments
                            # Check load cell and limit switches
                            time.sleep(0.1)  # 100ms pause
                            localStep += 1

                        lifeTestMotorDirection = 1  # Reset motor direction once loop executes
                        time.sleep(1)
                        print("Changing Motor Direction")
                        print("---------------------------------------------------------------------")


                    else:
                        print("Motor Direction Out of Range")

            else:
                lifeTest = False

        self.ui.lifeTestProgBar.setValue(100)
        print("")
        print("End Life Test Run")
        print("")

    def lifeTestSuspend(self):
        global motorEnabled, lifeTestActive

        if not lifeTestActive: #Test is not active, restart:
            print("Restarting life cycle test")
            motorEnabled = True
            lifeTestActive = True
            self.ui.lifeCycleSuspendBTN.setChecked(False)
            self.ui.lifeCycleSuspendBTN.setText("SUSPEND")
            self.ui.lifeCycleStartBTN.setDisabled(True)
            self.ui.lifeCycleStartBTN.setChecked(True)
            self.ui.lifeCycleStartBTN.setText("RUNNING")
            self.simpleLifeTest() #Restart the test

        elif lifeTestActive: # Test is live, shut it down
            print("Suspending life cycle test")
            motorEnabled = False
            lifeTestActive = False
            ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 5)  # 0V high to disable
            ljm.eWriteName(handle, "DIO" + str(motorPWM) + "_EF_ENABLE", 0)  # Disable the EF system

            self.ui.lifeCycleSuspendBTN.setChecked(True)
            self.ui.lifeCycleSuspendBTN.setText("SUSPENDED")
            self.ui.lifeCycleStartBTN.setDisabled(False)
            self.ui.lifeCycleStartBTN.setChecked(False)
            self.ui.lifeCycleStartBTN.setText("START")

    def lifeTestSuspend2(self):
        global motorEnabled, lifeTestActive

        if self.ui.lifeCycleStartBTN.isChecked(): #Test is suspended, restart:
            print("Restarting life cycle test")
            motorEnabled = True
            lifeTestActive = True
            #self.ui.lifeCycleSuspendBTN.setChecked(False)
            #self.ui.lifeCycleSuspendBTN.setText("SUSPEND")
            self.ui.lifeCycleStartBTN.setChecked(True)
            self.ui.lifeCycleStartBTN.setText("RUNNING")

        else: # Test is live, shut it down
            print("Suspending life cycle test")
            motorEnabled = False
            lifeTestActive = False
            ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 5)  # 0V high to disable
            ljm.eWriteName(handle, "DIO" + str(motorPWM) + "_EF_ENABLE", 0)  # Disable the EF system
            # self.ui.lifeCycleSuspendBTN.setChecked(True)
            # self.ui.lifeCycleSuspendBTN.setText("SUSPENDED")
            self.ui.lifeCycleStartBTN.setChecked(False)
            self.ui.lifeCycleStartBTN.setText("START")

    def clockSetup(self):
        print("Setting up life-test clock")

    '''
    Simple function to toggle the direction and speed during life cycle test.
    Does NOT control motor, but toggle parameters
    '''
    def lifeCycleToggle(self):
        RPMout = int(self.ui.RPMoutEdit.text())
        RPMin = int(self.ui.RPMinEdit.text())
        global lifeTestMotorDirection

        if lifeTestMotorDirection == 1: # Motor is driving out, toggle it to in
            lifeTestMotorDirection = 0
            freq = (RPMin*microstep)/60
        else:
            lifeTestMotorDirection = 1
            freq = (RPMout*microstep)/60


        print("Motor Parameters: ")
        print("Direction: " + str(lifeTestMotorDirection))
        print("RPM: " + str((1/microstep)*freq*60))
        print("")

        self.generateUserPWM(motorPWM, freq, defaultDuty)  # Potentially change freq/duty based on desired RPM
        ljm.eWriteName(handle, "DIO" + str(motorDirectionPin), lifeTestMotorDirection)

    def simpleLifeTest(self):
        # Initial variables
        global lifeTestActive, lifeTestMotorDirection, motorEnabled
        if not self.ui.lifeCycleStartBTN.isChecked(): # A test is running, make non-active
            lifeTestActive= True
            resetFlag = False #flag to check if action has been taken, but sensor still reading high
            self.lifeTestParamSample() #get user inputs
            self.ui.lifeCycleStartBTN.setText("RUNNING")
            self.ui.lifeCycleStartBTN.setDisabled(True)

            #sample start/stop time and get parameters
            #startTime = datetime.datetime.now().strftime("%H:%M")
            startTime = 0
            #endTime = (datetime.datetime.now() + timedelta(minutes=runTime)).strftime("%H:%M")
            #runPeriod = timedelta(minutes=runTime)
            runPeriod = int(self.ui.runTimeEdit.text())*60
            endTime = startTime + runPeriod
            minutes = 0

            #Start initial test
            lifeTestMotorDirection = 1
            freq = (RPMout * microstep) / 60
            self.generateUserPWM(motorPWM, freq, defaultDuty)  # Potentially change freq/duty based on desired RPM
            ljm.eWriteName(handle, "DIO" + str(motorDirectionPin), lifeTestMotorDirection)
            ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 0)  # Enable motor
            motorEnabled = True

            print("Initial motor running, starting threads")
            print(" ")

            # Pass the function to execute
            sensorWorker = Worker(self.lifeSensorSample)  # Any other args, kwargs are passed to the run function
            motorWorker = Worker(self.generateUserPWM, motorPWM, freq, defaultDuty)
            #progBarWorker = Worker(self.progTask, startTime, endTime, runPeriod)
            self.threadpool.start(sensorWorker)
            self.threadpool.start(motorWorker)
            #self.threadpool.start(progBarWorker)

        else:
            print("Test Running")
            self.ui.lifeCycleStartBTN.setDisabled(True)

    def motorRun(self):
       global motorDirection
       RPM = int(self.ui.RPMlineEdit.text())
       freq = (RPM/60)*microstep
       defaultFreq = freq

       print("RPM: " + str(RPM))
       print("Frequency: " + str(defaultFreq))

       if self.ui.startStopBTN.isChecked() and motorEnabled: # Motor stopped, so turn it on
            print("Turning Motor On")
            self.ui.startStopBTN.setText("STOP")
            if self.ui.fwdDirRadioBTN.isChecked(): # direction is forward, motor is enabled
                #begin PWM signal and write outputs high
                #self.motorRamp(1, RPM, 1)
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
           #ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 5) #5V high to disablemotor ---- POTENTIAL ERROR, SHOULD PULL LOW? ----
           ljm.eWriteName(handle, "DIO" + str(motorPWM) + "_EF_ENABLE", 0)  # Disable the EF system

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
        #self.ui.proxRadio1.setStyleSheet(redProxStyle)

        global motorEnabled
        if self.ui.enableBTN.isChecked(): # Motor is turned on
            print("Motor Enabled")
            print("")
            motorEnabled = True
            ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 0) # 0V high to enable
            self.ui.enableBTN.setText("DISABLE") # Reset label
        else:
            print("Motor Disabled")
            print("")
            motorEnabled = False
            ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 5)  # 5V high to disable motor
            ljm.eWriteName(handle, "DIO" + str(motorPWM) + "_EF_ENABLE", 0)  # Disable the EF system
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
    Input parameters: pin = output pin for DAC direction, direction = 1/0 direction, steps = numeric steps
    RPM = user driven RPM, duty = waveform duty cycle
    '''
    def goStep(self, pin, direction, steps, RPM, duty):
        if motorEnabled and steps > 0:
            ljm.eWriteName(handle, "DIO" + str(pin), direction)
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

                self.ui.motorRPMLCD.display(int(RPM))
                self.ui.PWMLCD.display(int(freq))

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
            ljm.eWriteName(handle, "DIO" + str(pin) + "_EF_ENABLE", 1)  # Enable the EF system, PWM wave is now being outputted

        else:
            print("IO Input Pin Not Valid *(T7 LabJack DIO 0, 2-5 ONLY)")

    def sampleSensorData(self):
        # test = datetime.datetime.now().strftime("%H:%M:%S")
        # print(test)
        global motorEnabled, lifeTestMotorDirection
        timeStamp = datetime.datetime.now().strftime("%H:%M:%S")
        V1 = ljm.eReadName(handle, pressureVoltage)  # Sample analog pressure input
        L1 = ljm.eReadName(handle, loadVoltage)  # Sample analog load cell input
        P1 = 61.121*V1-43.622
        #L1 = 61.121 * V2 - 43.622

        #testing purposes only
        flag = ljm.eReadName(handle, "AIN0")
        if flag > 3:
            #print("High Voltage Detected")
            motorEnabled = False
            ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 5)  # 5V high to disable motor

            print("Motor Directon: " + str(lifeTestMotorDirection))
            if lifeTestMotorDirection == 1:  # Direction is forward, put it in reverse
                lifeTestMotorDirection = 0
            else:  # direction is reverse, put er' in forward
                lifeTestMotorDirection = 1

            print("New Motor Direction: " + str(lifeTestMotorDirection))
            print("")
            time.sleep(10)
        else:
            motorEnabled = True
            ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 0)  # Ov low to enable motor
            ljm.eWriteName(handle, "DIO" + str(motorDirectionPin), lifeTestMotorDirection)
        # End Testing

        pressureSample = [timeStamp, P1, L1]  # add data to local list

        # print(P1)
        self.ui.pressureLCD1.display(P1)# display data on GUI
        self.ui.load1LCD.display(L1)
        #self.ui.pressureLCD2.display(P2)  # display data on GUI

        # Print for debug
        # print("P1 Voltage Reading: " + str(P1))
        # print("L1 Voltage Reading: " + str(L1))
        # print("Pressure Sample: " + str(pressureSample))
        return pressureSample

    def runSensorSession(self):
        sessionActive = self.ui.sensorBTN.isChecked() # Check initial state
        global sessionData
        if sessionActive:
            sessionData = []  # Generate empty list for local session data
            self.ui.sensorBTN.setText("STOP")

            while sessionActive:
                QApplication.processEvents()  # Check to see if session ended
                sessionActive = self.ui.sensorBTN.isChecked() # Check that session is running
                sessionData.append(self.sampleSensorData()) # sample data and write to session list
                self.plotSessionData2(sessionData)

        else:
            self.ui.sensorBTN.setText("START")

    '''
    Initial plot sensor session data to display real-time plot
    Carry-over from previous project, but locks up GUI
    See new version (2) below
    '''
    def plotSessionData(self, sessionData):
        global p1, p2
        #print("Plotting Data")
        self.ui.plotWidget.clear()
        self.ui.plotWidget.addLegend()
        curve1 = self.ui.plotWidget.plot(pen='r', name="PRESSURE")  # Tool pressure curve
        curve2 = self.ui.plotWidget.plot(pen='g', name="LOAD")

        p2 = pg.ViewBox()
        self.ui.plotWidget.scene().addItem(p2)
        self.ui.plotWidget.getAxis('right').linkToView(p2)
        p2.setXLink(self.ui.plotWidget)
        p2.setYRange(-15,15)
        p2.addItem(curve2)

        P1 = [] # Local list for pressure data
        L1 = [] # Local list for load cell data
        i = 0 # increment variable

        for set in sessionData:  # grab invidudal data points and make a list
            P1.append(sessionData[i][1])
            L1.append(sessionData[i][2])
            i += 1

        #print("P1: " + str(P1))
        #print("L1: " + str(L1))

        curve1.setData(P1) # Add pressure to curve
        curve2.setData(L1) # Add load cell voltage to curve
        # app.processEvents()
        P1A = np.array(P1) # format in array for plotting
        L1A = np.array(L1) # format in array for plotting

        def updateViews():
            global p1, p2
            p2.setGeometry(self.ui.plotWidget.getViewBox().sceneBoundingRect())
            p2.linkedViewChanged(self.ui.plotWidget.getViewBox(), p2.XAxis)

        def update():
            global curve1, curve2, P1A, L1A
            curve1.setData(P1A) # Plot pressure
            curve2.setData(L1A) # Plot load

        updateViews()
        #self.ui.plotWidget.getViewBox().sigResized.connect(updateViews)

        timer = QtCore.QTimer()
        timer.timeout.connect(update)
        timer.start(10000) # wait to refresh

    '''
    Version 2 - Calls daemon thread object to just plot while rest of program stays active. 
    Thread dies when program exits. 
    '''
    def plotSessionData2(self, sessionData):
        def plot():
            global p1, p2
            # print("Plotting Data")
            self.ui.plotWidget.clear()
            self.ui.plotWidget.addLegend()
            curve1 = self.ui.plotWidget.plot(pen='r', name="PRESSURE")  # Tool pressure curve
            curve2 = self.ui.plotWidget.plot(pen='g', name="LOAD")

            p2 = pg.ViewBox()
            self.ui.plotWidget.scene().addItem(p2)
            self.ui.plotWidget.getAxis('right').linkToView(p2)
            p2.setXLink(self.ui.plotWidget)
            p2.setYRange(-15, 15)
            p2.addItem(curve2)

            P1 = []  # Local list for pressure data
            L1 = []  # Local list for load cell data
            i = 0  # increment variable

            for set in sessionData:  # grab invidudal data points and make a list
                P1.append(sessionData[i][1])
                L1.append(sessionData[i][2])
                i += 1

            # print("P1: " + str(P1))
            # print("L1: " + str(L1))

            curve1.setData(P1)  # Add pressure to curve
            curve2.setData(L1)  # Add load cell voltage to curve
            # app.processEvents()
            P1A = np.array(P1)  # format in array for plotting
            L1A = np.array(L1)  # format in array for plotting

            def updateViews():
                global p1, p2
                p2.setGeometry(self.ui.plotWidget.getViewBox().sceneBoundingRect())
                p2.linkedViewChanged(self.ui.plotWidget.getViewBox(), p2.XAxis)

            def update():
                global curve1, curve2, P1A, L1A
                curve1.setData(P1A)  # Plot pressure
                curve2.setData(L1A)  # Plot load

            updateViews()
            # self.ui.plotWidget.getViewBox().sigResized.connect(updateViews)

            timer = QtCore.QTimer()
            timer.timeout.connect(update)
            timer.start(10000)  # wait to refresh

        plotThread = threading.Thread(name='plotThread', target=plot(), daemon=True)
        plotThread.start()

    def motorRamp(self, start, target, direction):
        ljm.eWriteName(handle, "DIO" + str(motorDirectionPin), direction)
        while start < target:
            incrementFreq = (start/60)*microstep
            self.generateUserPWM(motorPWM, incrementFreq, defaultDuty)  # Potentially change freq/duty based on desired RPM
            ljm.eWriteName(handle, "DIO" + str(motorDirectionPin), direction)
            time.sleep(1)
            start +=40

        # incrementFreq = (start / 60) * microstep
        # self.generateUserPWM(motorPWM, incrementFreq, defaultDuty)  # Potentially change freq/duty based on desired RPM
        # time.sleep(1)
        #
        # incrementFreq = (400 / 60) * microstep
        # self.generateUserPWM(motorPWM, incrementFreq, defaultDuty)  # Potentially change freq/duty based on desired RPM
        # time.sleep(1)
        #
        # incrementFreq = (550 / 60) * microstep
        # self.generateUserPWM(motorPWM, incrementFreq, defaultDuty)  # Potentially change freq/duty based on desired RPM
        # time.sleep(1)


        finalFreq = (target/60)*microstep
        self.generateUserPWM(motorPWM, finalFreq, defaultDuty)  # Potentially change freq/duty based on desired RPM

    def simpleSensorRead(self):
        name = "AIN0"
        voltage = ljm.eReadName(handle, name)
        print("Voltage Reading: " + str(voltage))
        time.sleep(.2)
        while True:
            voltage = ljm.eReadName(handle, name)
            print("Voltage Reading: " + str(voltage))
            time.sleep(0.1)
        return "Done"

    def lifeSensorSample(self):
        global motorEnable, lifeTestMotorDirection, motorEnabled, lifeTestActive
        lifeTestActive = True
        actionFlag = False
        actionTaken = False

        sessionData = []  # Generate empty list for local session data
        cutOffForce = int(self.ui.forceCutOffEdit.text())

        while lifeTestActive:
            timeStamp = datetime.datetime.now().strftime("%H:%M:%S")
            V1 = ljm.eReadName(handle, pressureVoltage)  # Sample analog pressure input
            LV1 = ljm.eReadName(handle, loadVoltage)  # Sample analog load cell input
            P1 = 61.121*V1-43.622
            load = LV1*1 #UPDATE NEEDED TO LOAD CELL
            prox1Low = ljm.eReadName(handle, px1Low) #read proximity sensor low
            prox1High = ljm.eReadName(handle, px1High) #read proximity sensor low

            #sessionData.append(self.sampleSensorData())  # sample data and write to session list
            #self.plotSessionData2(sessionData)

            print("Action Flag: " + str(actionFlag))
            print("Prox Val: " + str(prox1High))

            # Check first proximity sensor
            if prox1High > 3 and not actionTaken:
                print("Prox1 flagged, motor stopped)")
                self.ui.proxLifeRadio1.setStyleSheet(redProxStyle)
                motorEnabled = False #shut down motor
                motorEnable = 5 #shut down motor
                ljm.eWriteName(handle, "DAC" + str(motorEnablePin), motorEnable)  # 5V high to disable motor
                ljm.eWriteName(handle, "DIO" + str(motorPWM) + "_EF_ENABLE", 0)  # Disable the EF system

                #start timer to give a stop delay
                print("five second dwell....")
                time.sleep(5)
                print("toggling motor direction")
                self.lifeCycleToggle() #Toggle the motor direction and RPM
                print("New Motor Direction: " + str(lifeTestMotorDirection))
                print("")

                actionTaken = True #action has been taken based off of sensor flag
                motorEnabled = True #set indicator to true
                motorEnable = 0 #set global variable to allow motor to be durned on
                ljm.eWriteName(handle, "DAC" + str(motorEnablePin), motorEnable)  # Ov low to enable motor
                self.ui.proxLifeRadio1.setStyleSheet(yellowProxStyle)

            elif prox1High > 3 and actionTaken: #condition where sensor is still flagging but action has been taken
                timeVal = 0
                timeout = 10
                print("Timeout starting for " + str(timeout) + " seconds")
                time.sleep(timeout)
                prox1High = ljm.eReadName(handle, px1High)

                if prox1High > 3: #see if sensor resets, if not, shut it down
                    print("No sensor reset, shutting down permanently)")
                    motorEnable = 5  # shut down motor
                    ljm.eWriteName(handle, "DAC" + str(motorEnablePin), motorEnable)  # 5V high to disable motor
                    ljm.eWriteName(handle, "DIO" + str(motorPWM) + "_EF_ENABLE", 0)  # Disable the EF system
                    lifeTestActive = False
                    while True:
                        self.ui.proxLifeRadio1.setStyleSheet(yellowProxStyle)
                        time.sleep(.25)
                        self.ui.proxLifeRadio1.setStyleSheet(redProxStyle)
                        time.sleep(.25)


                else: #sensor reset, all clear
                    actionTaken = False
                    self.ui.proxLifeRadio1.setStyleSheet(greenProxStyle)

            elif prox1High < 3:
                self.ui.proxLifeRadio1.setStyleSheet(greenProxStyle)
                actionTaken = False

            #check load cell
            # if load >= cutOffForce:
            #     print("Max Load Exceeded")
            #     self.lifeTestSuspend()
            #     print("Suspending life cycle test")
            #     motorEnabled = False
            #     lifeTestActive = False
            #     motorEnable = 5
            #     ljm.eWriteName(handle, "DAC" + str(motorEnablePin), motorEnable)  # 0V high to disable
            #     ljm.eWriteName(handle, "DIO" + str(motorPWM) + "_EF_ENABLE", 0)  # Disable the EF system

            print("Life Test Running")
            self.ui.pressureLifeLCD.display(P1)# display data on GUI
            self.ui.loadLifeLCD.display(load)
            time.sleep(0.1)

    def checkLoadMax(self):
        global motorEnabled, lifeTestActive, motorEnable
        cutOffForce = int(self.ui.forceCutOffEdit.text())
        Vload = ljm.eReadName(handle, loadVoltage)  # Sample analog load cell input
        L1 = 61.121 * Vload - 43.622 # compute load cell from linear interpolated curve

        if L1 >= cutOffForce:
            print("Max Load Exceeded")
            self.lifeTestSuspend()
            print("Suspending life cycle test")
            motorEnabled = False
            lifeTestActive = False
            motorEnable = 5
            ljm.eWriteName(handle, "DAC" + str(motorEnablePin), motorEnable)  # 0V high to disable
            ljm.eWriteName(handle, "DIO" + str(motorPWM) + "_EF_ENABLE", 0)  # Disable the EF system

    def progTask(self):
        task = Task()
        print(task.updated.connect(self.progBarUpdate))

    def progBarUpdate(self, startTime, endTime, runPeriod):
        with self.redrawLock:
            elapsedTime = 0
            while lifeTestActive:
                if elapsedTime <= runPeriod: # While the test is active, update
                    progBarVal = 100 * ((runPeriod - (endTime - elapsedTime)) / runPeriod)
                    self.ui.lifeTestProgBar.setValue(progBarVal)
                    elapsedTime += 2 #update in 1 sec intervals
                    time.sleep(2)
                else:
                    print("Life Test Suspended - No prog bar update")







if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = mywindow()
    # w.setStyleSheet("background-image: url(image.png)")
    w.show()
    sys.exit(app.exec_())