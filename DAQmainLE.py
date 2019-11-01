'''
DESCRIPTION:
    Main file to control BASF hose reel for FAT Test. Current state is working with sensors reading out,
    motor controlled manual. Life cycle tab still under development.

STATE:
    Working. Load cell actual output it needed (conversion from mA) and potentially a display function to
    slow down updated of pressure and load cell to make easier to read (delay). Use encoder prox sensors to
    calculate the linear feed rate and display.

    Potentially automated function to lower reel from


MODIFIED DATE: 11.1.19
Author: Chris Antle
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
microstep = 400 # Microstep setting on Kollmorgen stepper drive
defaultFreq = 20000# Default PWM Freq
defaultDuty = 0.05
sampleRate = 10 # defined in mS

#Life Test Globals
startTime = 0
endTime = 0
runPeriod = 0

# Define I/O Pins
motorEnable = 5 #5V high to disable motors
motorDirectionPin = 1 # Defined as DIO pin number
motorEnablePin = 1 # Defined as DAC pin number
VCOPin = 0 # Defined as DAC pin for PWM generator
baseMax = 2 # Defined as DIO pin number with signal generator - pulled high to disable
stopRun = 0 #defined as DIO pin
pressureVoltage = "AIN0"
loadVoltage = "AIN1"

hoseStop = "AIN2"
RPMprox1 = "AIN3"
RPMprox2 = "AIN4"


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
        self.fn(*self.args, **self.kwargs)


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
        self.ui.RPMoutLineEdit.setText(str(600))
        self.ui.RPMinLineEdit.setText(str(1200))

        # set up button control
        # Control tab
        self.ui.enableBTN.clicked.connect(lambda:self.enableMotorToggle())
        self.ui.startStopBTN.clicked.connect(lambda:self.motorRun())
        self.ui.sensorBTN.clicked.connect(lambda:self.runSensorSession())
        self.ui.proxRadio1.setStyleSheet(greenProxStyle)
        self.ui.proxRadio2.setStyleSheet(greenProxStyle)
        self.ui.proxRadio3.setStyleSheet(greenProxStyle)
        self.ui.microStepLCD.display(str(microstep))
        sampleFreq = 1/(sampleRate/1000)
        self.ui.lineEdit.setText(str(sampleFreq))

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

        #Ensure motor is off and configure paramters
        ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 5) #5V high to disable
        ljm.eWriteName(handle, "DAC" + str(VCOPin), 0)  #4V for 16kHz max signal
        ljm.eWriteName(handle, "DIO" + str(baseMax), 1)  #Pull high to disable logic from controller
        ljm.eWriteName(handle, "DIO" + str(stopRun), 1)  #Pull low to enter single input mode

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

    def enableMotorToggle(self):
        #self.ui.proxRadio1.setStyleSheet(redProxStyle)

        global motorEnabled
        if self.ui.enableBTN.isChecked(): # Motor is turned on
            print("Motor Enabled")
            print("")
            motorEnabled = True
            ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 0) # 0V low to enable
            self.ui.enableBTN.setText("DISABLE") # Reset label
        else:
            print("Motor Disabled")
            print("")
            motorEnabled = False
            ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 5)  # 5V high to disable motor
            self.ui.enableBTN.setText("ENABLE")  # Reset label
            self.ui.startStopBTN.setChecked(False)
            self.ui.startStopBTN.setText("START")
            self.ui.PWMLCD.display(str(0))

    def motorRun(self):
       global motorDirection
       if self.ui.startStopBTN.isChecked() and motorEnabled: # Motor stopped, so turn it on
            print("Turning Motor On")
            self.ui.startStopBTN.setText("STOP")
            if self.ui.fwdDirRadioBTN.isChecked(): # direction is forward, motor is enabled
                #begin PWM signal and write outputs high
                #self.generateUserPWM(motorPWM,defaultFreq, defaultDuty) # Potentially change freq/duty based on desired RPM
                RPM = int(self.ui.RPMoutLineEdit.text())
                voltageTarget = ((RPM*microstep)/60)/(3960) #compute target voltage

                ljm.eWriteName(handle, "DIO" + str(motorDirectionPin), 1)
                ljm.eWriteName(handle, "DAC" + str(VCOPin), voltageTarget) #Set to 4v for 16kHz output
                ljm.eWriteName(handle, "DIO" + str(baseMax), 0) #Pull low to start ramp to max speed

                self.ui.PWMLCD.display(voltageTarget*3960)
                print("Direction: Forward")
                print("VCO Output: " + str(voltageTarget))
                print("")

            elif self.ui.revDirRadioBTN.isChecked(): # reverse direction
                #self.generateUserPWM(motorPWM, defaultFreq, defaultDuty) # Potentially change freq/duty based on desired RPM
                RPM = int(self.ui.RPMinLineEdit.text())
                voltageTarget = ((RPM * microstep) / 60)/(3960)  # compute target voltage
                ljm.eWriteName(handle, "DIO" + str(motorDirectionPin), 0)
                ljm.eWriteName(handle, "DAC" + str(VCOPin), voltageTarget)  # Set to 4v for 16kHz output
                ljm.eWriteName(handle, "DIO" + str(baseMax), 0)  #Pull low to start ramp to max speed

                self.ui.PWMLCD.display(voltageTarget * 3960)
                print("Direction: Reverse")
                print("VCO Output: " + str(voltageTarget))
                print("")

       elif not self.ui.startStopBTN.isChecked() and motorEnabled: #Motor running, stop it
           print("Turning Motor Off - Ramping Down")
           print("")
           self.ui.startStopBTN.setText("START")
           #ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 5) #5V high to disablemotor ---- POTENTIAL ERROR, SHOULD PULL LOW? ----
           ljm.eWriteName(handle, "DIO" + str(baseMax), 1) #Pull digital high to start ramp down

       else: # Motor disabled
           prompt = QMessageBox.warning(self, 'Motor Disabled',
                                                 'Motor disabled - enable to run',
                                                 QMessageBox.Ok | QMessageBox.Cancel)
           if prompt == QMessageBox.Ok:
               print("Ok")
               self.ui.startStopBTN.setChecked(False)
           else:
               sys.exit(app.exec_())

    def sampleSensorData(self):
        # test = datetime.datetime.now().strftime("%H:%M:%S")
        # print(test)
        global motorEnabled, lifeTestMotorDirection
        timeStamp = datetime.datetime.now().strftime("%H:%M:%S")
        V1 = ljm.eReadName(handle, pressureVoltage)  # Sample analog pressure input
        L1 = ljm.eReadName(handle, loadVoltage)  # Sample analog load cell input
        P1 = 61.121*V1-43.622
        #L1 = 61.121 * V2 - 43.622

        # print(P1)
        self.ui.pressureLCD1.display(P1)# display data on GUI
        self.ui.load1LCD.display(L1)


    def runSensorSession2(self):
        sessionActive = self.ui.sensorBTN.isChecked()  # Check initial state
        global sessionData, hoseStop, RPMprox1, RPMprox2

        if sessionActive:
            #sessionData = []  # Generate empty list for local session data
            self.ui.sensorBTN.setText("STOP")
            sessionActive = self.ui.sensorBTN.isChecked() # Check that session is running
            #self.sampleSensorData() # sample data and write to session list
            #self.checkProx(hoseStop, RPMprox1, RPMprox2)
            #self.plotSessionData2(sessionData)
            proxWorker = Worker(self.checkProx)  # Any other args, kwargs are passed to the run function
            self.threadpool.start(proxWorker)

        else:
            self.ui.sensorBTN.setText("START")


    def runSensorSession(self):
        global sessionActive
        sessionActive = self.ui.sensorBTN.isChecked()  # Check initial state
        global timerOn
        print(sessionActive)

        if sessionActive:
            #sessionData = []  # Generate empty list for local session data
            self.ui.sensorBTN.setText("STOP")

            self.qTimer = QTimer()
            # set interval to 1 s
            self.qTimer.setInterval(sampleRate)  # 1000 ms = 1 s
            # connect timeout signal to signal handler
            self.qTimer.timeout.connect(self.checkProx)
            # start timer
            self.qTimer.start()

        else:
            self.ui.proxRadio1.setStyleSheet(yellowProxStyle)
            self.ui.proxRadio2.setStyleSheet(yellowProxStyle)
            self.ui.proxRadio3.setStyleSheet(yellowProxStyle)
            self.ui.sensorBTN.setText("START")
            self.qTimer.stop()


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
            timer.start(1000)  # wait to refresh

        plotThread = threading.Thread(name='plotThread', target=plot(), daemon=True)
        plotThread.start()

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
            ljm.eWriteName(handle, "DIO" + str(baseMax) + "_EF_ENABLE", 0)  # Disable the EF system
            # self.ui.lifeCycleSuspendBTN.setChecked(True)
            # self.ui.lifeCycleSuspendBTN.setText("SUSPENDED")
            self.ui.lifeCycleStartBTN.setChecked(False)
            self.ui.lifeCycleStartBTN.setText("START")

    '''
    Simple function to toggle the direction and speed during life cycle test.
    Does NOT control motor, but toggle parameters
    '''
    def lifeCycleToggle(self):
        global lifeTestMotorDirection

        if lifeTestMotorDirection == 1: # Motor is driving out, toggle it to in
            lifeTestMotorDirection = 0
            RPM = int(self.ui.RPMinEdit.text())
            voltageTarget = ((RPM * microstep) / 60) / (3960)  # compute target voltage
            ljm.eWriteName(handle, "DIO" + str(motorDirectionPin), lifeTestMotorDirection)
            ljm.eWriteName(handle, "DAC" + str(VCOPin), voltageTarget)  # Set to 4v for 16kHz output
            ljm.eWriteName(handle, "DIO" + str(baseMax), 0)  # Pull low to start ramp to max speed

            self.ui.PWMLCD.display(voltageTarget * 3960)
            print("Direction: Reverse")
            print("VCO Output: " + str(voltageTarget))
            print("")

        else: #Motor is driving in, toggle it to out
            lifeTestMotorDirection = 1
            RPM = int(self.ui.RPMoutEdit.text())
            voltageTarget = ((RPM * microstep) / 60) / (3960)  # compute target voltage
            ljm.eWriteName(handle, "DIO" + str(motorDirectionPin), lifeTestMotorDirection)
            ljm.eWriteName(handle, "DAC" + str(VCOPin), voltageTarget)  # Set to 4v for 16kHz output
            ljm.eWriteName(handle, "DIO" + str(baseMax), 0)  # Pull low to start ramp to max speed

            self.ui.PWMLCD.display(voltageTarget * 3960)
            print("Direction: Forward")
            print("VCO Output: " + str(voltageTarget))
            print("")

        print("Motor Parameters: ")
        print("Direction: " + str(lifeTestMotorDirection))
        print("")

    def simpleLifeTest(self):
        # Initial variables
        global lifeTestActive, lifeTestMotorDirection, motorEnabled
        if self.ui.lifeCycleStartBTN.isChecked(): # A test is running, make non-active
            lifeTestActive= True
            resetFlag = False #flag to check if action has been taken, but sensor still reading high
            self.lifeTestParamSample() #get user inputs
            self.ui.lifeCycleStartBTN.setText("RUNNING")
            self.ui.lifeCycleStartBTN.setDisabled(True)

            startTime = 0
            runPeriod = int(self.ui.runTimeEdit.text())*60
            endTime = startTime + runPeriod
            minutes = 0

            #Start initial test, motor running forward
            lifeTestMotorDirection = 1
            ljm.eWriteName(handle, "DIO" + str(motorDirectionPin), lifeTestMotorDirection)
            ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 0)  # Enable motor
            motorEnabled = True
            RPM = int(self.ui.RPMoutEdit.text())
            voltageTarget = ((RPM * microstep) / 60) / (3960)  # compute target voltage
            ljm.eWriteName(handle, "DAC" + str(VCOPin), voltageTarget)  # Set to 4v for 16kHz output
            ljm.eWriteName(handle, "DIO" + str(baseMax), 0)  # Pull low to start ramp to max speed


            print("Initial motor running, starting threads")
            print(" ")

            timeset = 0
            timeout = 60

            while False:
                if timeset < timeout:
                    time.sleep(1)
                    timeset += 1
                    print("Time: " + str(timeset))
                else:
                    self.lifeCycleToggle()
                    timeset = 0
                    print("Resetting time function")
                    time.sleep(2)

            # Pass the function to execute
            sensorWorker = Worker(self.lifeSensorSample)  # Any other args, kwargs are passed to the run function
            #motorWorker = Worker(self.lifeTestMotorRun)
            #progBarWorker = Worker(self.progTask, startTime, endTime, runPeriod)

            self.threadpool.start(sensorWorker)
            #self.threadpool.start(motorWorker)
            #self.threadpool.start(progBarWorker)

        else:
            print("Test Running")
            self.ui.lifeCycleStartBTN.setDisabled(True)

    def lifeTestMotorRun(self, direction, speed):
        global motorDirection
        if direction == 1:  # Motor stopped, so turn it on
            RPM = int(self.ui.RPMoutEdit.text())
            voltageTarget = ((RPM * microstep) / 60) / (3960)  # compute target voltage
            ljm.eWriteName(handle, "DIO" + str(motorDirectionPin), 1)
            ljm.eWriteName(handle, "DAC" + str(VCOPin), voltageTarget)  # Set to 4v for 16kHz output
            ljm.eWriteName(handle, "DIO" + str(baseMax), 0)  # Pull low to start ramp to max speed

            self.ui.PWMLCD.display(voltageTarget * 3960)
            print("Direction: Forward")
            print("VCO Output: " + str(voltageTarget))
            print("")

        else:  # reverse direction
            RPM = int(self.ui.RPMinEdit.text())
            voltageTarget = ((RPM * microstep) / 60) / (3960)  # compute target voltage
            ljm.eWriteName(handle, "DIO" + str(motorDirectionPin), 0)
            ljm.eWriteName(handle, "DAC" + str(VCOPin), voltageTarget)  # Set to 4v for 16kHz output
            ljm.eWriteName(handle, "DIO" + str(baseMax), 0)  # Pull low to start ramp to max speed

            self.ui.PWMLCD.display(voltageTarget * 3960)
            print("Direction: Reverse")
            print("VCO Output: " + str(voltageTarget))
            print("")

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

        cutOffForce = int(self.ui.forceCutOffEdit.text())

        timeSet = 0
        timeout = 40 # CHANGE THIS FOR LONGER RUN TIME

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
            if timeSet > timeout and not actionTaken:
                ljm.eWriteName(handle, "DIO" + str(baseMax), 1)  # Pull high to start decel ramp
                print("Prox1 flagged, motor stopped)")
                self.ui.proxLifeRadio1.setStyleSheet(redProxStyle)
                motorEnabled = False #shut down motor
                ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 5)  # 5V high to disable motor

                #start timer to give a stop delay
                print("5 second dwell....")
                time.sleep(5)
                print("toggling motor direction")
                self.lifeCycleToggle() #Toggle the motor direction and RPM
                print("New Motor Direction: " + str(lifeTestMotorDirection))
                print("")

                print("Time Val: " + str(timeSet))

                actionTaken = True #action has been taken based off of sensor flag
                motorEnabled = True #set indicator to true
                ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 0)  # Ov low to enable motor
                self.ui.proxLifeRadio1.setStyleSheet(yellowProxStyle)
                timeSet = 0

            elif timeSet > timeout and actionTaken: #condition where sensor is still flagging but action has been taken
                timeVal = 0
                timeCheck = 10
                print("Timeout starting for " + str(timeCheck) + " seconds")
                time.sleep(timeCheck)
                prox1High = ljm.eReadName(handle, px1High)
                actionTaken = False
                self.ui.proxLifeRadio1.setStyleSheet(greenProxStyle)

                # if prox1High > 3: #see if sensor resets, if not, shut it down
                #     print("No sensor reset, shutting down permanently)")
                #     ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 5)  # 5V high to disable motor
                #     lifeTestActive = False
                #
                # else: #sensor reset, all clear
                #     actionTaken = False
                #     self.ui.proxLifeRadio1.setStyleSheet(greenProxStyle)


            elif timeSet <= timeout:
                self.ui.proxLifeRadio1.setStyleSheet(greenProxStyle)
                actionTaken = False
                time.sleep(1)
                timeSet += 1

        # #check load cell
            # if load >= cutOffForce:
            #     print("Max Load Exceeded")
            #     self.lifeTestSuspend()
            #     print("Suspending life cycle test")
            #     motorEnabled = False
            #     lifeTestActive = False
            #     motorEnable = 5
            #     ljm.eWriteName(handle, "DAC" + str(motorEnablePin), motorEnable)  # 0V high to disable

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

    def checkProx(self):
        global hoseStop, RPMprox1, RPMprox2
        global sessionActive, motorEnabled
        toolStatus = ljm.eReadName(handle, hoseStop)  #Tool status should read high if prox sensor is flagged
        RPM1Status = ljm.eReadName(handle, RPMprox1)
        RPM2Status = ljm.eReadName(handle, RPMprox2)
        load = ljm.eReadName(handle, loadVoltage)
        pressure = ljm.eReadName(handle, pressureVoltage)

        loadmA = (8.475*load)
        pressurePSI = 5556.3*pressure-2579.2

        self.ui.load1LCD.display(str(int(loadmA)))
        self.ui.pressureLCD1.display(str(int(pressurePSI)))

        # Check tool stop
        if toolStatus > 3 and sessionActive:
            ljm.eWriteName(handle, "DIO" + str(baseMax), 1)  # prox detected, ramp down to stop
            sessionActive = False

            self.ui.proxRadio1.setStyleSheet(redProxStyle)
            self.ui.proxRadio2.setStyleSheet(redProxStyle)
            self.ui.proxRadio3.setStyleSheet(redProxStyle)

            self.ui.startStopBTN.setChecked(False)


            prompt = QMessageBox.warning(self, 'TOOL STOP TRIPPED',
                                         'TOOL STOP TRIPPED',
                                         QMessageBox.Ok | QMessageBox.Cancel)
            if prompt == QMessageBox.Ok:
                print("Ok")
                self.ui.startStopBTN.setChecked(False)
                self.ui.startStopBTN.setText("START")
                self.ui.revDirRadioBTN.setChecked(True)
                self.ui.sensorBTN.setText("START")
                self.ui.sensorBTN.setChecked(False)

                motorEnabled = False
                ljm.eWriteName(handle, "DAC" + str(motorEnablePin), 5)  # 5V high to disable motor
                self.ui.enableBTN.setText("ENABLE")  # Reset label
                self.ui.enableBTN.setChecked(False)  # Reset label
                self.ui.startStopBTN.setChecked(False)
                self.ui.startStopBTN.setText("START")

                self.runSensorSession()
            else:
                sys.exit(app.exec_())


        elif toolStatus < 3 and sessionActive:
            self.ui.proxRadio1.setStyleSheet(greenProxStyle)
            #print("Tool Stop Low: " + str(toolStatus))

            if RPM1Status > 3:
                #print("Prox flagged, motor stopped)")
                self.ui.proxRadio2.setStyleSheet(yellowProxStyle)
            elif RPM1Status < 3:
                self.ui.proxRadio2.setStyleSheet(greenProxStyle)

            if RPM2Status > 3:
                self.ui.proxRadio3.setStyleSheet(yellowProxStyle)
            elif RPM2Status < 3:
                self.ui.proxRadio3.setStyleSheet(greenProxStyle)


    def flipflop(self):
        time = 0
        direction = 1
        while lifeTestActive:
            time = 0
            timeout = 60
            if time < timeout:
                time.sleep(1)
                time +=1
            else:
                self.lifeCycleToggle()

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