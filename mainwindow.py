# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(597, 555)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setStyleSheet("QWidget\n"
"{\n"
" background-image: url(:/sa_logo_3d_003);\n"
"background-color: rgb(80,80,80);\n"
"  color: rgb(220,220,220);\n"
"  font-size: 11px;\n"
"  outline: none;\n"
"}\n"
"\n"
"/**** QWidget (disabled) ****/\n"
"QWidget:disabled\n"
"{\n"
"  color: rgb(40,40,40);\n"
"}\n"
"")
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.line_4 = QtWidgets.QFrame(self.centralWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setStyleSheet("QLabel\n"
"{\n"
"  background-color: transparent;\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"}\n"
"\n"
"/**** QLabel (disabled) ****/\n"
"QLabel\n"
"{\n"
"}")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.pressureLCD = QtWidgets.QLCDNumber(self.centralWidget)
        self.pressureLCD.setStyleSheet("QLCDNumber\n"
"{\n"
"  background-color: rgb(40,40,40);\n"
"  border: 1px solid rgb(20,20,20);\n"
"}\n"
"\n"
"/**** QLCDNumber (disabled) ****/\n"
"QLCDNumber:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border: 1px solid rgb(60,60,60);\n"
"}")
        self.pressureLCD.setObjectName("pressureLCD")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pressureLCD)
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setStyleSheet("QLabel\n"
"{\n"
"  background-color: transparent;\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"}\n"
"\n"
"/**** QLabel (disabled) ****/\n"
"QLabel\n"
"{\n"
"}")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.loadLCD = QtWidgets.QLCDNumber(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadLCD.sizePolicy().hasHeightForWidth())
        self.loadLCD.setSizePolicy(sizePolicy)
        self.loadLCD.setStyleSheet("QLCDNumber\n"
"{\n"
"  background-color: rgb(40,40,40);\n"
"  border: 1px solid rgb(20,20,20);\n"
"}\n"
"\n"
"/**** QLCDNumber (disabled) ****/\n"
"QLCDNumber:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border: 1px solid rgb(60,60,60);\n"
"}")
        self.loadLCD.setObjectName("loadLCD")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.loadLCD)
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet("QLabel\n"
"{\n"
"  background-color: transparent;\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"}\n"
"\n"
"/**** QLabel (disabled) ****/\n"
"QLabel\n"
"{\n"
"}")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.limitPosition = QtWidgets.QProgressBar(self.centralWidget)
        self.limitPosition.setMaximum(100)
        self.limitPosition.setProperty("value", 100)
        self.limitPosition.setFormat("")
        self.limitPosition.setObjectName("limitPosition")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.limitPosition)
        self.verticalLayout.addLayout(self.formLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.line_6 = QtWidgets.QFrame(self.centralWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_3.addWidget(self.line_6)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(120,120,120), stop: 1 rgb(80,80,80));\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(230,230,230);\n"
"  padding: 4px 8px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(40,150,200), stop: 1 rgb(90,200,255));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"/**** QPushButton (disabled) ****/\n"
"QPushButton:disabled\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(160,160,160), stop: 1 rgb(120,120,120));\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 3, 1, 1)
        self.MotorLayout = QtWidgets.QVBoxLayout()
        self.MotorLayout.setSpacing(6)
        self.MotorLayout.setObjectName("MotorLayout")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.MotorLayout.addWidget(self.label_2)
        self.line_3 = QtWidgets.QFrame(self.centralWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.MotorLayout.addWidget(self.line_3)
        self.motorRunBtn = QtWidgets.QPushButton(self.centralWidget)
        self.motorRunBtn.setStyleSheet("QPushButton\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(120,120,120), stop: 1 rgb(80,80,80));\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(230,230,230);\n"
"  padding: 4px 8px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(40,150,200), stop: 1 rgb(90,200,255));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"/**** QPushButton (disabled) ****/\n"
"QPushButton:disabled\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(160,160,160), stop: 1 rgb(120,120,120));\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.motorRunBtn.setCheckable(True)
        self.motorRunBtn.setAutoDefault(False)
        self.motorRunBtn.setObjectName("motorRunBtn")
        self.MotorLayout.addWidget(self.motorRunBtn)
        self.motorSpeedSlider = QtWidgets.QSlider(self.centralWidget)
        self.motorSpeedSlider.setStyleSheet("QSlider\n"
"{\n"
"  background-color: transparent;\n"
"}\n"
"\n"
"QSlider::groove\n"
"{\n"
"  border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(40,150,200), stop: 1 rgb(90,200,255));\n"
"  border-radius: 8px;\n"
"}\n"
"\n"
"/**** QSlider (horizontal) ****/\n"
"QSlider::groove:horizontal\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(160,160,160), stop: 1 rgb(80,80,80));\n"
"  height: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal\n"
"{\n"
"  margin: -6px 0;\n"
"  width: 16px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"/**** QSlider (vertical) ****/\n"
"QSlider::groove:vertical\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                    stop: 0 rgb(160,160,160), stop: 1 rgb(80,80,80));\n"
"  width: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical\n"
"{\n"
"  margin: 0 -6px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QSlider::groove:vertical:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"/**** QSlider (disabled) ****/\n"
"QSlider::handle:disabled\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(160,160,160), stop: 1 rgb(120,120,120));\n"
"}")
        self.motorSpeedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.motorSpeedSlider.setObjectName("motorSpeedSlider")
        self.MotorLayout.addWidget(self.motorSpeedSlider)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(120,120,120), stop: 1 rgb(80,80,80));\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(230,230,230);\n"
"  padding: 4px 8px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(40,150,200), stop: 1 rgb(90,200,255));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"/**** QPushButton (disabled) ****/\n"
"QPushButton:disabled\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(160,160,160), stop: 1 rgb(120,120,120));\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.line_12 = QtWidgets.QFrame(self.centralWidget)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.horizontalLayout_4.addWidget(self.line_12)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(120,120,120), stop: 1 rgb(80,80,80));\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(230,230,230);\n"
"  padding: 4px 8px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(40,150,200), stop: 1 rgb(90,200,255));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"/**** QPushButton (disabled) ****/\n"
"QPushButton:disabled\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(160,160,160), stop: 1 rgb(120,120,120));\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.MotorLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.motorSpeedLabel = QtWidgets.QLabel(self.centralWidget)
        self.motorSpeedLabel.setObjectName("motorSpeedLabel")
        self.horizontalLayout_3.addWidget(self.motorSpeedLabel)
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.motorLCD = QtWidgets.QLCDNumber(self.centralWidget)
        self.motorLCD.setStyleSheet("QLCDNumber\n"
"{\n"
"  background-color: rgb(40,40,40);\n"
"  border: 1px solid rgb(20,20,20);\n"
"}\n"
"\n"
"/**** QLCDNumber (disabled) ****/\n"
"QLCDNumber:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border: 1px solid rgb(60,60,60);\n"
"}")
        self.motorLCD.setObjectName("motorLCD")
        self.horizontalLayout_3.addWidget(self.motorLCD)
        self.MotorLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.motorRadioStop = QtWidgets.QRadioButton(self.centralWidget)
        self.motorRadioStop.setStyleSheet("")
        self.motorRadioStop.setChecked(True)
        self.motorRadioStop.setObjectName("motorRadioStop")
        self.horizontalLayout.addWidget(self.motorRadioStop)
        self.line_9 = QtWidgets.QFrame(self.centralWidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout.addWidget(self.line_9)
        self.motorRadioFWD = QtWidgets.QRadioButton(self.centralWidget)
        self.motorRadioFWD.setStyleSheet("")
        self.motorRadioFWD.setObjectName("motorRadioFWD")
        self.horizontalLayout.addWidget(self.motorRadioFWD)
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.motorRadioREV = QtWidgets.QRadioButton(self.centralWidget)
        self.motorRadioREV.setStyleSheet("")
        self.motorRadioREV.setObjectName("motorRadioREV")
        self.horizontalLayout.addWidget(self.motorRadioREV)
        self.line_8 = QtWidgets.QFrame(self.centralWidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout.addWidget(self.line_8)
        self.MotorLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.MotorLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.motorFreqLCD = QtWidgets.QLCDNumber(self.centralWidget)
        self.motorFreqLCD.setStyleSheet("QLCDNumber\n"
"{\n"
"  background-color: rgb(40,40,40);\n"
"  border: 1px solid rgb(20,20,20);\n"
"}\n"
"\n"
"/**** QLCDNumber (disabled) ****/\n"
"QLCDNumber:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border: 1px solid rgb(60,60,60);\n"
"}")
        self.motorFreqLCD.setObjectName("motorFreqLCD")
        self.horizontalLayout_2.addWidget(self.motorFreqLCD)
        self.line_7 = QtWidgets.QFrame(self.centralWidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_2.addWidget(self.line_7)
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.motorDutyLCD = QtWidgets.QLCDNumber(self.centralWidget)
        self.motorDutyLCD.setStyleSheet("QLCDNumber\n"
"{\n"
"  background-color: rgb(40,40,40);\n"
"  border: 1px solid rgb(20,20,20);\n"
"}\n"
"\n"
"/**** QLCDNumber (disabled) ****/\n"
"QLCDNumber:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border: 1px solid rgb(60,60,60);\n"
"}")
        self.motorDutyLCD.setObjectName("motorDutyLCD")
        self.horizontalLayout_2.addWidget(self.motorDutyLCD)
        self.MotorLayout.addLayout(self.horizontalLayout_2)
        self.line_10 = QtWidgets.QFrame(self.centralWidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.MotorLayout.addWidget(self.line_10)
        self.gridLayout.addLayout(self.MotorLayout, 0, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 0, 1, 1, 1)
        self.line_11 = QtWidgets.QFrame(self.centralWidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout.addWidget(self.line_11, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">SENSORS</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic;\">PRESSURE (PSI)</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic;\">LOAD (LB F)</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic;\">LIMIT A</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">AUTO RUN</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">MOTOR CONTROL</span></p></body></html>"))
        self.motorRunBtn.setText(_translate("MainWindow", "RUN"))
        self.pushButton_3.setText(_translate("MainWindow", "<- STEP"))
        self.pushButton_2.setText(_translate("MainWindow", "STEP ->"))
        self.motorSpeedLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">SPEED (RPM)</span></p></body></html>"))
        self.motorRadioStop.setText(_translate("MainWindow", "STOP"))
        self.motorRadioFWD.setText(_translate("MainWindow", "FWD"))
        self.motorRadioREV.setText(_translate("MainWindow", "REV"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Signal Parameters</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Frequency (Hz)"))
        self.label_9.setText(_translate("MainWindow", "Duty Cycle (%)"))


