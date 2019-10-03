# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BASFmainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(885, 793)
        self.W1 = QtWidgets.QWidget(MainWindow)
        self.W1.setStyleSheet("QWidget#W1{\n"
"background-color: black;\n"
"opacity: 0.5;\n"
"background-position: center;\n"
"}\n"
"\n"
"")
        self.W1.setObjectName("W1")
        self.gridLayout = QtWidgets.QGridLayout(self.W1)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.plotLayout = QtWidgets.QVBoxLayout()
        self.plotLayout.setSpacing(6)
        self.plotLayout.setObjectName("plotLayout")
        self.plotWidget = PlotWidget(self.W1)
        self.plotWidget.setStyleSheet("QWidget#plotWidget\n"
"{\n"
"  background-color: transparent;\n"
"  color: rgb(220,220,220, 10);\n"
"  font-size: 11px;\n"
"  outline: none;\n"
"opacity: 0.5;\n"
"}\n"
"\n"
"/**** QWidget (disabled) ****/\n"
"QWidget:disabled\n"
"{\n"
"  color: rgb(40,40,40);\n"
"}")
        self.plotWidget.setObjectName("plotWidget")
        self.plotLayout.addWidget(self.plotWidget)
        self.gridLayout.addLayout(self.plotLayout, 2, 0, 1, 1)
        self.T1 = QtWidgets.QTabWidget(self.W1)
        self.T1.setStyleSheet("QTabWidget#T1\n"
"{\n"
"background-color: rgb(80,80,80);\n"
"background-image:  url(\"C:/Users/chris.antle/Documents/BASF/backgroundDark.jpg\");\n"
"opacity: 0.5;\n"
"background-position: center;\n"
"}\n"
"\n"
"QTabWidget#T1::pane\n"
"{\n"
"background-color: rgb(200, 200, 200, 0);\n"
"}\n"
"\n"
"/**** QTabWidget (disabled) ****/\n"
"QTabWidget::pane:disabled\n"
"{\n"
"  border-color: rgb(60,60,60);\n"
"}")
        self.T1.setTabPosition(QtWidgets.QTabWidget.North)
        self.T1.setObjectName("T1")
        self.controlTab = QtWidgets.QWidget()
        self.controlTab.setStyleSheet("QWidget#controlTab{\n"
"background-color: rgb(80,80,80);\n"
"background-image:  url(\"C:/Users/chris.antle/Documents/BASF/backgroundDark.jpg\");\n"
"opacity: 0.5;\n"
"background-position: center;\n"
"\n"
"}")
        self.controlTab.setObjectName("controlTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.controlTab)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_5 = QtWidgets.QFrame(self.controlTab)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 0, 1, 1, 1)
        self.controlWidget = QtWidgets.QWidget(self.controlTab)
        self.controlWidget.setStyleSheet("QWidget#controlWidget\n"
"{\n"
"  background-color: rgb(0, 0, 0,80);\n"
"  color: rgb(220,220,220);\n"
"  font-size: 11px;\n"
"  outline: none;\n"
"opacity: 0.5;\n"
"}\n"
"\n"
"/**** QWidget (disabled) ****/\n"
"QWidget:disabled\n"
"{\n"
"  color: rgb(40,40,40);\n"
"}")
        self.controlWidget.setObjectName("controlWidget")
        self.controlLayout = QtWidgets.QVBoxLayout(self.controlWidget)
        self.controlLayout.setContentsMargins(11, 11, 11, 11)
        self.controlLayout.setSpacing(6)
        self.controlLayout.setObjectName("controlLayout")
        self.label_7 = QtWidgets.QLabel(self.controlWidget)
        self.label_7.setObjectName("label_7")
        self.controlLayout.addWidget(self.label_7)
        self.line_6 = QtWidgets.QFrame(self.controlWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.controlLayout.addWidget(self.line_6)
        self.startStopBTN = QtWidgets.QPushButton(self.controlWidget)
        self.startStopBTN.setStyleSheet("QPushButton\n"
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
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(0, 242, 0), stop: 1 rgb(0, 170, 0));\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(125,75,0);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
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
        self.startStopBTN.setCheckable(True)
        self.startStopBTN.setAutoDefault(False)
        self.startStopBTN.setObjectName("startStopBTN")
        self.controlLayout.addWidget(self.startStopBTN)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.revDirRadioBTN = QtWidgets.QRadioButton(self.controlWidget)
        self.revDirRadioBTN.setStyleSheet("/**** QRadioButton (enabled) ****/\n"
"QRadioButton\n"
"{\n"
"  background-color: transparent;\n"
"  color: rgb(220, 220, 220);\n"
"  padding: 4px 8px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"  border: 1px solid rgb(20,20,20);\n"
"  border-radius: 7px;\n"
"  width: 14px;\n"
"  height: 14px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(120,120,120), stop: 1 rgb(80,80,80));\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(0, 242, 0), stop: 1 rgb(0, 170, 0));\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover,\n"
"QRadioButton::indicator:checked:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed,\n"
"QRadioButton::indicator:checked:pressed\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"}\n"
"\n"
"/**** QRadioButton (disabled) ****/\n"
"QRadioButton:disabled\n"
"{\n"
"  color: rgb(40,40,40);\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled\n"
"{\n"
"  border-color: rgb(60,60,60);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled\n"
"{\n"
"  image: url(images/radiobutton_checked_disabled.png);\n"
"}\n"
"")
        self.revDirRadioBTN.setObjectName("revDirRadioBTN")
        self.horizontalLayout_5.addWidget(self.revDirRadioBTN)
        self.fwdDirRadioBTN = QtWidgets.QRadioButton(self.controlWidget)
        self.fwdDirRadioBTN.setStyleSheet("/**** QRadioButton (enabled) ****/\n"
"QRadioButton\n"
"{\n"
"  background-color: transparent;\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px 8px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"  border: 1px solid rgb(20,20,20);\n"
"  border-radius: 7px;\n"
"  width: 14px;\n"
"  height: 14px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(120,120,120), stop: 1 rgb(80,80,80));\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(0, 242, 0), stop: 1 rgb(0, 170, 0));\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover,\n"
"QRadioButton::indicator:checked:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed,\n"
"QRadioButton::indicator:checked:pressed\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"}\n"
"\n"
"/**** QRadioButton (disabled) ****/\n"
"QRadioButton:disabled\n"
"{\n"
"  color: rgb(40,40,40);\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled\n"
"{\n"
"  border-color: rgb(60,60,60);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:disabled\n"
"{\n"
"  image: url(images/radiobutton_checked_disabled.png);\n"
"}\n"
"")
        self.fwdDirRadioBTN.setChecked(True)
        self.fwdDirRadioBTN.setObjectName("fwdDirRadioBTN")
        self.horizontalLayout_5.addWidget(self.fwdDirRadioBTN)
        self.enableBTN = QtWidgets.QPushButton(self.controlWidget)
        self.enableBTN.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enableBTN.sizePolicy().hasHeightForWidth())
        self.enableBTN.setSizePolicy(sizePolicy)
        self.enableBTN.setStyleSheet("QPushButton\n"
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
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(0, 242, 0), stop: 1 rgb(0, 170, 0));\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(125,75,0);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
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
        self.enableBTN.setCheckable(True)
        self.enableBTN.setObjectName("enableBTN")
        self.horizontalLayout_5.addWidget(self.enableBTN)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.controlLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.controlWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.RPMinLineEdit = QtWidgets.QLineEdit(self.controlWidget)
        self.RPMinLineEdit.setStyleSheet("QLineEdit\n"
"{\n"
"  background-color: rgb(80,80,80);\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"  selection-background-color: rgb(70,110,130);\n"
"  selection-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"}\n"
"\n"
"/**** QLineEdit (disabled) ****/\n"
"QLineEdit:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.RPMinLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.RPMinLineEdit.setObjectName("RPMinLineEdit")
        self.horizontalLayout_6.addWidget(self.RPMinLineEdit)
        self.label_15 = QtWidgets.QLabel(self.controlWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_6.addWidget(self.label_15)
        self.RPMoutLineEdit = QtWidgets.QLineEdit(self.controlWidget)
        self.RPMoutLineEdit.setStyleSheet("QLineEdit\n"
"{\n"
"  background-color: rgb(80,80,80);\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"  selection-background-color: rgb(70,110,130);\n"
"  selection-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"}\n"
"\n"
"/**** QLineEdit (disabled) ****/\n"
"QLineEdit:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.RPMoutLineEdit.setObjectName("RPMoutLineEdit")
        self.horizontalLayout_6.addWidget(self.RPMoutLineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.controlLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stepRevBTN = QtWidgets.QPushButton(self.controlWidget)
        self.stepRevBTN.setEnabled(False)
        self.stepRevBTN.setStyleSheet("QPushButton\n"
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
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(0, 242, 0), stop: 1 rgb(0, 170, 0));\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(125,75,0);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
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
        self.stepRevBTN.setObjectName("stepRevBTN")
        self.horizontalLayout.addWidget(self.stepRevBTN)
        self.stepFwdBTN = QtWidgets.QPushButton(self.controlWidget)
        self.stepFwdBTN.setEnabled(False)
        self.stepFwdBTN.setStyleSheet("QPushButton\n"
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
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(0, 242, 0), stop: 1 rgb(0, 170, 0));\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(125,75,0);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
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
        self.stepFwdBTN.setObjectName("stepFwdBTN")
        self.horizontalLayout.addWidget(self.stepFwdBTN)
        self.label_11 = QtWidgets.QLabel(self.controlWidget)
        self.label_11.setStyleSheet("QLabel:\n"
"{\n"
"color: rgb(220, 220, 220);\n"
"}")
        self.label_11.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.spinBox = QtWidgets.QSpinBox(self.controlWidget)
        self.spinBox.setEnabled(False)
        self.spinBox.setStyleSheet("QSpinBox,\n"
"QDoubleSpinBox,\n"
"QTimeEdit,\n"
"QDateEdit,\n"
"QDateTimeEdit\n"
"{\n"
"  background-color: rgb(80,80,80);\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"  selection-background-color: rgb(70,110,130);\n"
"  selection-color: white;\n"
"}\n"
"\n"
"QSpinBox:focus,\n"
"QDoubleSpinBox:focus,\n"
"QTimeEdit:focus,\n"
"QDateEdit:focus,\n"
"QDateTimeEdit:focus\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"}\n"
"\n"
"QSpinBox::up-button,\n"
"QDoubleSpinBox::up-button,\n"
"QTimeEdit::up-button,\n"
"QDateEdit::up-button,\n"
"QDateTimeEdit::up-button\n"
"{\n"
"\n"
"  width: 16px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover,\n"
"QDoubleSpinBox::up-button:hover,\n"
"QTimeEdit::up-button:hover,\n"
"QDateEdit::up-button:hover,\n"
"QDateTimeEdit::up-button:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed,\n"
"QDoubleSpinBox::up-button:pressed,\n"
"QTimeEdit::up-button:pressed,\n"
"QDateEdit::up-button:pressed,\n"
"QDateTimeEdit::up-button:pressed\n"
"{\n"
"\n"
"}\n"
"\n"
"QSpinBox::down-button,\n"
"QDoubleSpinBox::down-button,\n"
"QTimeEdit::down-button,\n"
"QDateEdit::down-button,\n"
"QDateTimeEdit::down-button\n"
"{\n"
"\n"
"  width: 16px;\n"
"}\n"
"\n"
"QSpinBox::down-button:hover,\n"
"QDoubleSpinBox::down-button:hover,\n"
"QTimeEdit::down-button:hover,\n"
"QDateEdit::down-button:hover,\n"
"QDateTimeEdit::down-button:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed,\n"
"QDoubleSpinBox::down-button:pressed,\n"
"QTimeEdit::down-button:pressed,\n"
"QDateEdit::down-button:pressed,\n"
"QDateTimeEdit::down-button:pressed\n"
"{\n"
"\n"
"}\n"
"\n"
"/**** QSpinBox, QDoubleSpinBox, QTimeEdit, QDateEdit and QDateTimeEdit (disabled) ****/\n"
"QSpinBox:disabled,\n"
"QDoubleSpinBox:disabled,\n"
"QTimeEdit:disabled,\n"
"QDateEdit:disabled,\n"
"QDateTimeEdit:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}\n"
"\n"
"QSpinBox::up-button:disabled,\n"
"QDoubleSpinBox::up-button:disabled,\n"
"QTimeEdit::up-button:disabled,\n"
"QDateEdit::up-button:disabled,\n"
"QDateTimeEdit::up-button:disabled\n"
"{\n"
"\n"
"}\n"
"\n"
"QSpinBox::down-button:disabled,\n"
"QDoubleSpinBox::down-button:disabled,\n"
"QTimeEdit::down-button:disabled,\n"
"QDateEdit::down-button:disabled,\n"
"QDateTimeEdit::down-button:disabled\n"
"{\n"
"\n"
"}")
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.controlLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.controlLayout.addLayout(self.horizontalLayout_3)
        self.label_13 = QtWidgets.QLabel(self.controlWidget)
        self.label_13.setObjectName("label_13")
        self.controlLayout.addWidget(self.label_13)
        self.line_2 = QtWidgets.QFrame(self.controlWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.controlLayout.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.controlWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.PWMLCD = QtWidgets.QLCDNumber(self.controlWidget)
        self.PWMLCD.setStyleSheet("QLCDNumber\n"
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
        self.PWMLCD.setDigitCount(5)
        self.PWMLCD.setObjectName("PWMLCD")
        self.horizontalLayout_2.addWidget(self.PWMLCD)
        self.label_9 = QtWidgets.QLabel(self.controlWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.motorRPMLCD = QtWidgets.QLCDNumber(self.controlWidget)
        self.motorRPMLCD.setEnabled(True)
        self.motorRPMLCD.setStyleSheet("QLCDNumber\n"
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
        self.motorRPMLCD.setObjectName("motorRPMLCD")
        self.horizontalLayout_2.addWidget(self.motorRPMLCD)
        self.controlLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.controlLayout.addItem(spacerItem3)
        self.gridLayout_2.addWidget(self.controlWidget, 0, 0, 1, 1)
        self.sensorWidget = QtWidgets.QWidget(self.controlTab)
        self.sensorWidget.setStyleSheet("QWidget#sensorWidget\n"
"{\n"
"  background-color: rgb(0, 0, 0,80);\n"
"  color: rgb(220,220,220);\n"
"  font-size: 11px;\n"
"  outline: none;\n"
"opacity: 0.5;\n"
"}\n"
"\n"
"/**** QWidget (disabled) ****/\n"
"QWidget:disabled\n"
"{\n"
"  color: rgb(40,40,40);\n"
"}")
        self.sensorWidget.setObjectName("sensorWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sensorWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.sensorWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.line_4 = QtWidgets.QFrame(self.sensorWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.pressureLayout = QtWidgets.QHBoxLayout()
        self.pressureLayout.setSpacing(6)
        self.pressureLayout.setObjectName("pressureLayout")
        self.verticalLayout.addLayout(self.pressureLayout)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.proxRadio2 = QtWidgets.QRadioButton(self.sensorWidget)
        self.proxRadio2.setStyleSheet("QRadioButton::indicator {width: 15px; height: 15px; border-radius: 7px;} QRadioButton::indicator:unchecked { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
"\n"
"border: 2px solid gray;}")
        self.proxRadio2.setText("")
        self.proxRadio2.setCheckable(False)
        self.proxRadio2.setObjectName("proxRadio2")
        self.gridLayout_6.addWidget(self.proxRadio2, 2, 1, 1, 1)
        self.s1MSLabel = QtWidgets.QLabel(self.sensorWidget)
        self.s1MSLabel.setObjectName("s1MSLabel")
        self.gridLayout_6.addWidget(self.s1MSLabel, 1, 0, 1, 1)
        self.proxRadio3 = QtWidgets.QRadioButton(self.sensorWidget)
        self.proxRadio3.setStyleSheet("QRadioButton::indicator {width: 15px; height: 15px; border-radius: 7px;} QRadioButton::indicator:unchecked { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
"\n"
"border: 2px solid gray;}")
        self.proxRadio3.setText("")
        self.proxRadio3.setCheckable(False)
        self.proxRadio3.setObjectName("proxRadio3")
        self.gridLayout_6.addWidget(self.proxRadio3, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.sensorWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.sensorWidget)
        self.label_17.setEnabled(False)
        self.label_17.setObjectName("label_17")
        self.gridLayout_6.addWidget(self.label_17, 3, 0, 1, 1)
        self.proxRadio1 = QtWidgets.QRadioButton(self.sensorWidget)
        self.proxRadio1.setStyleSheet("QRadioButton::indicator {width: 15px; height: 15px; border-radius: 7px;} QRadioButton::indicator:unchecked {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(0, 242, 0), stop: 1 rgb(0, 170, 0));\n"
"border: 2px solid gray;}")
        self.proxRadio1.setText("")
        self.proxRadio1.setCheckable(False)
        self.proxRadio1.setObjectName("proxRadio1")
        self.gridLayout_6.addWidget(self.proxRadio1, 1, 1, 1, 1)
        self.load1LCD = QtWidgets.QLCDNumber(self.sensorWidget)
        self.load1LCD.setStyleSheet("QLCDNumber\n"
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
        self.load1LCD.setDigitCount(8)
        self.load1LCD.setMode(QtWidgets.QLCDNumber.Dec)
        self.load1LCD.setProperty("value", 0.0)
        self.load1LCD.setObjectName("load1LCD")
        self.gridLayout_6.addWidget(self.load1LCD, 2, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.sensorWidget)
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
        self.gridLayout_6.addWidget(self.label_6, 1, 2, 1, 1)
        self.pressureLCD1 = QtWidgets.QLCDNumber(self.sensorWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressureLCD1.sizePolicy().hasHeightForWidth())
        self.pressureLCD1.setSizePolicy(sizePolicy)
        self.pressureLCD1.setStyleSheet("QLCDNumber\n"
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
        self.pressureLCD1.setDigitCount(8)
        self.pressureLCD1.setObjectName("pressureLCD1")
        self.gridLayout_6.addWidget(self.pressureLCD1, 1, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.sensorWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("/**** QLineEdit (enabled) ****/\n"
"QLineEdit\n"
"{\n"
"  background-color: rgb(80,80,80);\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"  selection-background-color: rgb(70,110,130);\n"
"  selection-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"}\n"
"\n"
"/**** QLineEdit (disabled) ****/\n"
"QLineEdit:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_6.addWidget(self.lineEdit, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.sensorWidget)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 3, 2, 1, 1)
        self.sensorBTN = QtWidgets.QPushButton(self.sensorWidget)
        self.sensorBTN.setStyleSheet("QPushButton\n"
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
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(0, 242, 0), stop: 1 rgb(0, 170, 0));\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(125,75,0);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
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
        self.sensorBTN.setCheckable(True)
        self.sensorBTN.setObjectName("sensorBTN")
        self.gridLayout_6.addWidget(self.sensorBTN, 4, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.sensorWidget)
        self.label_3.setStyleSheet("QLabel\n"
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
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_6)
        self.label_12 = QtWidgets.QLabel(self.sensorWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.line_13 = QtWidgets.QFrame(self.sensorWidget)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.verticalLayout.addWidget(self.line_13)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.newSessionBTN = QtWidgets.QPushButton(self.sensorWidget)
        self.newSessionBTN.setEnabled(False)
        self.newSessionBTN.setStyleSheet("QPushButton\n"
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
"  background-color: rgb(150,95,15);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(125,75,0);\n"
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
        self.newSessionBTN.setObjectName("newSessionBTN")
        self.horizontalLayout_4.addWidget(self.newSessionBTN)
        self.saveSessionBTN = QtWidgets.QPushButton(self.sensorWidget)
        self.saveSessionBTN.setEnabled(False)
        self.saveSessionBTN.setStyleSheet("QPushButton\n"
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
"  background-color: rgb(150,95,15);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(125,75,0);\n"
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
        self.saveSessionBTN.setObjectName("saveSessionBTN")
        self.horizontalLayout_4.addWidget(self.saveSessionBTN)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.filePathLayout = QtWidgets.QHBoxLayout()
        self.filePathLayout.setSpacing(6)
        self.filePathLayout.setObjectName("filePathLayout")
        self.label_14 = QtWidgets.QLabel(self.sensorWidget)
        self.label_14.setObjectName("label_14")
        self.filePathLayout.addWidget(self.label_14)
        self.fileNameEdit = QtWidgets.QLineEdit(self.sensorWidget)
        self.fileNameEdit.setStyleSheet("/**** QLineEdit (enabled) ****/\n"
"QLineEdit\n"
"{\n"
"  background-color: rgb(80,80,80);\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"  selection-background-color: rgb(70,110,130);\n"
"  selection-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"}\n"
"\n"
"/**** QLineEdit (disabled) ****/\n"
"QLineEdit:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.fileNameEdit.setReadOnly(True)
        self.fileNameEdit.setObjectName("fileNameEdit")
        self.filePathLayout.addWidget(self.fileNameEdit)
        self.verticalLayout.addLayout(self.filePathLayout)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.line_11 = QtWidgets.QFrame(self.sensorWidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout.addWidget(self.line_11)
        self.gridLayout_2.addWidget(self.sensorWidget, 0, 2, 1, 1)
        self.T1.addTab(self.controlTab, "")
        self.lifeTestTab = QtWidgets.QWidget()
        self.lifeTestTab.setStyleSheet("QWidget#lifeTestTab{\n"
"background-color: rgb(80,80,80);\n"
"background-image:  url(\"C:/Users/chris.antle/Documents/BASF/backgroundDark.jpg\");\n"
"opacity: 0.5;\n"
"background-position: center;\n"
"\n"
"}")
        self.lifeTestTab.setObjectName("lifeTestTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.lifeTestTab)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.line = QtWidgets.QFrame(self.lifeTestTab)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 0, 1, 1, 1)
        self.paramWidget = QtWidgets.QWidget(self.lifeTestTab)
        self.paramWidget.setStyleSheet("QWidget#paramWidget\n"
"{\n"
"  background-color: rgb(0, 0, 0,80);\n"
"  color: rgb(220,220,220);\n"
"  font-size: 11px;\n"
"  outline: none;\n"
"opacity: 0.5;\n"
"}\n"
"\n"
"/**** QWidget (disabled) ****/\n"
"QWidget:disabled\n"
"{\n"
"  color: rgb(40,40,40);\n"
"}")
        self.paramWidget.setObjectName("paramWidget")
        self.cycleParameters = QtWidgets.QVBoxLayout(self.paramWidget)
        self.cycleParameters.setContentsMargins(11, 11, 11, 11)
        self.cycleParameters.setSpacing(6)
        self.cycleParameters.setObjectName("cycleParameters")
        self.label_20 = QtWidgets.QLabel(self.paramWidget)
        self.label_20.setObjectName("label_20")
        self.cycleParameters.addWidget(self.label_20)
        self.line_3 = QtWidgets.QFrame(self.paramWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.cycleParameters.addWidget(self.line_3)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.runTimeEdit = QtWidgets.QLineEdit(self.paramWidget)
        self.runTimeEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runTimeEdit.sizePolicy().hasHeightForWidth())
        self.runTimeEdit.setSizePolicy(sizePolicy)
        self.runTimeEdit.setStyleSheet("/**** QLineEdit (enabled) ****/\n"
"QLineEdit\n"
"{\n"
"  background-color: rgb(80,80,80);\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"  selection-background-color: rgb(70,110,130);\n"
"  selection-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"}\n"
"\n"
"/**** QLineEdit (disabled) ****/\n"
"QLineEdit:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.runTimeEdit.setObjectName("runTimeEdit")
        self.gridLayout_5.addWidget(self.runTimeEdit, 0, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.paramWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.paramWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 1, 2, 1, 1)
        self.RPMoutEdit = QtWidgets.QLineEdit(self.paramWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RPMoutEdit.sizePolicy().hasHeightForWidth())
        self.RPMoutEdit.setSizePolicy(sizePolicy)
        self.RPMoutEdit.setStyleSheet("/**** QLineEdit (enabled) ****/\n"
"QLineEdit\n"
"{\n"
"  background-color: rgb(80,80,80);\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"  selection-background-color: rgb(70,110,130);\n"
"  selection-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"}\n"
"\n"
"/**** QLineEdit (disabled) ****/\n"
"QLineEdit:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.RPMoutEdit.setObjectName("RPMoutEdit")
        self.gridLayout_5.addWidget(self.RPMoutEdit, 2, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.paramWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 0, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.paramWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 0, 0, 1, 1)
        self.forceCutOffEdit = QtWidgets.QLineEdit(self.paramWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forceCutOffEdit.sizePolicy().hasHeightForWidth())
        self.forceCutOffEdit.setSizePolicy(sizePolicy)
        self.forceCutOffEdit.setStyleSheet("/**** QLineEdit (enabled) ****/\n"
"QLineEdit\n"
"{\n"
"  background-color: rgb(80,80,80);\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"  selection-background-color: rgb(70,110,130);\n"
"  selection-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"}\n"
"\n"
"/**** QLineEdit (disabled) ****/\n"
"QLineEdit:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.forceCutOffEdit.setObjectName("forceCutOffEdit")
        self.gridLayout_5.addWidget(self.forceCutOffEdit, 0, 3, 1, 1)
        self.stepsOutEdit = QtWidgets.QLineEdit(self.paramWidget)
        self.stepsOutEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepsOutEdit.sizePolicy().hasHeightForWidth())
        self.stepsOutEdit.setSizePolicy(sizePolicy)
        self.stepsOutEdit.setStyleSheet("/**** QLineEdit (enabled) ****/\n"
"QLineEdit\n"
"{\n"
"  background-color: rgb(80,80,80);\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"  selection-background-color: rgb(70,110,130);\n"
"  selection-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"}\n"
"\n"
"/**** QLineEdit (disabled) ****/\n"
"QLineEdit:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.stepsOutEdit.setObjectName("stepsOutEdit")
        self.gridLayout_5.addWidget(self.stepsOutEdit, 1, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.paramWidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 2, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.paramWidget)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 2, 2, 1, 1)
        self.RPMinEdit = QtWidgets.QLineEdit(self.paramWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RPMinEdit.sizePolicy().hasHeightForWidth())
        self.RPMinEdit.setSizePolicy(sizePolicy)
        self.RPMinEdit.setStyleSheet("/**** QLineEdit (enabled) ****/\n"
"QLineEdit\n"
"{\n"
"  background-color: rgb(80,80,80);\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"  selection-background-color: rgb(70,110,130);\n"
"  selection-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"}\n"
"\n"
"/**** QLineEdit (disabled) ****/\n"
"QLineEdit:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.RPMinEdit.setObjectName("RPMinEdit")
        self.gridLayout_5.addWidget(self.RPMinEdit, 2, 3, 1, 1)
        self.stepsInEdit = QtWidgets.QLineEdit(self.paramWidget)
        self.stepsInEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepsInEdit.sizePolicy().hasHeightForWidth())
        self.stepsInEdit.setSizePolicy(sizePolicy)
        self.stepsInEdit.setStyleSheet("/**** QLineEdit (enabled) ****/\n"
"QLineEdit\n"
"{\n"
"  background-color: rgb(80,80,80);\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(220,220,220);\n"
"  padding: 4px;\n"
"  selection-background-color: rgb(70,110,130);\n"
"  selection-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"}\n"
"\n"
"/**** QLineEdit (disabled) ****/\n"
"QLineEdit:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.stepsInEdit.setObjectName("stepsInEdit")
        self.gridLayout_5.addWidget(self.stepsInEdit, 1, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem5, 4, 1, 1, 1)
        self.paramSaveBTN = QtWidgets.QPushButton(self.paramWidget)
        self.paramSaveBTN.setStyleSheet("QPushButton\n"
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
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(0, 242, 0), stop: 1 rgb(0, 170, 0));\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(125,75,0);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
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
        self.paramSaveBTN.setObjectName("paramSaveBTN")
        self.gridLayout_5.addWidget(self.paramSaveBTN, 3, 0, 1, 2)
        self.paramClearBTN = QtWidgets.QPushButton(self.paramWidget)
        self.paramClearBTN.setStyleSheet("QPushButton\n"
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
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(0, 242, 0), stop: 1 rgb(0, 170, 0));\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(125,75,0);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
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
        self.paramClearBTN.setObjectName("paramClearBTN")
        self.gridLayout_5.addWidget(self.paramClearBTN, 3, 2, 1, 2)
        self.cycleParameters.addLayout(self.gridLayout_5)
        self.gridLayout_3.addWidget(self.paramWidget, 0, 0, 1, 1)
        self.statusWidget = QtWidgets.QWidget(self.lifeTestTab)
        self.statusWidget.setStyleSheet("QWidget#statusWidget\n"
"{\n"
"  background-color: rgb(0, 0, 0,80);\n"
"  color: rgb(220,220,220);\n"
"  font-size: 11px;\n"
"  outline: none;\n"
"opacity: 0.5;\n"
"}\n"
"\n"
"/**** QWidget (disabled) ****/\n"
"QWidget:disabled\n"
"{\n"
"  color: rgb(40,40,40);\n"
"}")
        self.statusWidget.setObjectName("statusWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.statusWidget)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_26 = QtWidgets.QLabel(self.statusWidget)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_3.addWidget(self.label_26)
        self.line_7 = QtWidgets.QFrame(self.statusWidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_3.addWidget(self.line_7)
        self.lifeTestProgBar = QtWidgets.QProgressBar(self.statusWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lifeTestProgBar.sizePolicy().hasHeightForWidth())
        self.lifeTestProgBar.setSizePolicy(sizePolicy)
        self.lifeTestProgBar.setStyleSheet("QProgressBar\n"
"{\n"
"  background-color: rgb(40,40,40);\n"
"  background-color: rgb(140,80,10,20);\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(220,220,220);\n"
"  text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"  background-color: rgb(30,185,15);\n"
"  margin: 1px;\n"
"  width: 4px;\n"
"}\n"
"\n"
"/**** QProgressBar (disabled) ****/\n"
"QProgressBar:disabled\n"
"{\n"
"  background-color: rgb(120,120,120);\n"
"  border: 1px solid rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.lifeTestProgBar.setProperty("value", 24)
        self.lifeTestProgBar.setObjectName("lifeTestProgBar")
        self.verticalLayout_3.addWidget(self.lifeTestProgBar)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_30 = QtWidgets.QLabel(self.statusWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setObjectName("label_30")
        self.gridLayout_4.addWidget(self.label_30, 5, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.statusWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setObjectName("label_31")
        self.gridLayout_4.addWidget(self.label_31, 6, 0, 1, 1)
        self.loadLifeLCD = QtWidgets.QLCDNumber(self.statusWidget)
        self.loadLifeLCD.setObjectName("loadLifeLCD")
        self.gridLayout_4.addWidget(self.loadLifeLCD, 5, 3, 1, 1)
        self.proxLifeRadio2 = QtWidgets.QRadioButton(self.statusWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxLifeRadio2.sizePolicy().hasHeightForWidth())
        self.proxLifeRadio2.setSizePolicy(sizePolicy)
        self.proxLifeRadio2.setStyleSheet("QRadioButton::indicator {width: 15px; height: 15px; border-radius: 7px;} QRadioButton::indicator:unchecked {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(0, 242, 0), stop: 1 rgb(0, 170, 0));\n"
"border: 2px solid gray;}")
        self.proxLifeRadio2.setText("")
        self.proxLifeRadio2.setObjectName("proxLifeRadio2")
        self.gridLayout_4.addWidget(self.proxLifeRadio2, 5, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.statusWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setObjectName("label_29")
        self.gridLayout_4.addWidget(self.label_29, 4, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.statusWidget)
        self.label_28.setObjectName("label_28")
        self.gridLayout_4.addWidget(self.label_28, 5, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem6, 10, 0, 1, 1)
        self.proxLifeRadio3 = QtWidgets.QRadioButton(self.statusWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxLifeRadio3.sizePolicy().hasHeightForWidth())
        self.proxLifeRadio3.setSizePolicy(sizePolicy)
        self.proxLifeRadio3.setStyleSheet("QRadioButton::indicator {width: 15px; height: 15px; border-radius: 7px;} QRadioButton::indicator:unchecked {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(242, 242, 0), stop: 1 rgb(170, 142, 0));\n"
"border: 2px solid gray;}")
        self.proxLifeRadio3.setText("")
        self.proxLifeRadio3.setObjectName("proxLifeRadio3")
        self.gridLayout_4.addWidget(self.proxLifeRadio3, 6, 1, 1, 1)
        self.pressureLifeLCD = QtWidgets.QLCDNumber(self.statusWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressureLifeLCD.sizePolicy().hasHeightForWidth())
        self.pressureLifeLCD.setSizePolicy(sizePolicy)
        self.pressureLifeLCD.setObjectName("pressureLifeLCD")
        self.gridLayout_4.addWidget(self.pressureLifeLCD, 4, 3, 1, 1)
        self.lifeCycleStartBTN = QtWidgets.QPushButton(self.statusWidget)
        self.lifeCycleStartBTN.setStyleSheet("QPushButton\n"
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
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(0, 242, 0), stop: 1 rgb(0, 170, 0));\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(125,75,0);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
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
        self.lifeCycleStartBTN.setCheckable(True)
        self.lifeCycleStartBTN.setObjectName("lifeCycleStartBTN")
        self.gridLayout_4.addWidget(self.lifeCycleStartBTN, 6, 2, 1, 2)
        self.proxLifeRadio1 = QtWidgets.QRadioButton(self.statusWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxLifeRadio1.sizePolicy().hasHeightForWidth())
        self.proxLifeRadio1.setSizePolicy(sizePolicy)
        self.proxLifeRadio1.setStyleSheet("QRadioButton::indicator {width: 15px; height: 15px; border-radius: 7px;} QRadioButton::indicator:unchecked {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(0, 242, 0), stop: 1 rgb(0, 170, 0));\n"
"border: 2px solid gray;}")
        self.proxLifeRadio1.setText("")
        self.proxLifeRadio1.setAutoExclusive(True)
        self.proxLifeRadio1.setObjectName("proxLifeRadio1")
        self.gridLayout_4.addWidget(self.proxLifeRadio1, 4, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.statusWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setObjectName("label_27")
        self.gridLayout_4.addWidget(self.label_27, 4, 2, 1, 1)
        self.lifeCycleSuspendBTN = QtWidgets.QPushButton(self.statusWidget)
        self.lifeCycleSuspendBTN.setStyleSheet("QPushButton\n"
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
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(0, 242, 0), stop: 1 rgb(0, 170, 0));\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(125,75,0);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
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
        self.lifeCycleSuspendBTN.setCheckable(True)
        self.lifeCycleSuspendBTN.setObjectName("lifeCycleSuspendBTN")
        self.gridLayout_4.addWidget(self.lifeCycleSuspendBTN, 7, 2, 1, 2)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.gridLayout_3.addWidget(self.statusWidget, 0, 2, 1, 1)
        self.T1.addTab(self.lifeTestTab, "")
        self.gridLayout.addWidget(self.T1, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.W1)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.T1.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.startStopBTN, self.revDirRadioBTN)
        MainWindow.setTabOrder(self.revDirRadioBTN, self.fwdDirRadioBTN)
        MainWindow.setTabOrder(self.fwdDirRadioBTN, self.RPMinLineEdit)
        MainWindow.setTabOrder(self.RPMinLineEdit, self.stepRevBTN)
        MainWindow.setTabOrder(self.stepRevBTN, self.stepFwdBTN)
        MainWindow.setTabOrder(self.stepFwdBTN, self.spinBox)
        MainWindow.setTabOrder(self.spinBox, self.proxRadio2)
        MainWindow.setTabOrder(self.proxRadio2, self.proxRadio3)
        MainWindow.setTabOrder(self.proxRadio3, self.proxRadio1)
        MainWindow.setTabOrder(self.proxRadio1, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.sensorBTN)
        MainWindow.setTabOrder(self.sensorBTN, self.newSessionBTN)
        MainWindow.setTabOrder(self.newSessionBTN, self.saveSessionBTN)
        MainWindow.setTabOrder(self.saveSessionBTN, self.fileNameEdit)
        MainWindow.setTabOrder(self.fileNameEdit, self.plotWidget)
        MainWindow.setTabOrder(self.plotWidget, self.enableBTN)
        MainWindow.setTabOrder(self.enableBTN, self.paramSaveBTN)
        MainWindow.setTabOrder(self.paramSaveBTN, self.paramClearBTN)
        MainWindow.setTabOrder(self.paramClearBTN, self.runTimeEdit)
        MainWindow.setTabOrder(self.runTimeEdit, self.forceCutOffEdit)
        MainWindow.setTabOrder(self.forceCutOffEdit, self.stepsOutEdit)
        MainWindow.setTabOrder(self.stepsOutEdit, self.stepsInEdit)
        MainWindow.setTabOrder(self.stepsInEdit, self.RPMoutEdit)
        MainWindow.setTabOrder(self.RPMoutEdit, self.RPMinEdit)
        MainWindow.setTabOrder(self.RPMinEdit, self.proxLifeRadio3)
        MainWindow.setTabOrder(self.proxLifeRadio3, self.lifeCycleStartBTN)
        MainWindow.setTabOrder(self.lifeCycleStartBTN, self.proxLifeRadio1)
        MainWindow.setTabOrder(self.proxLifeRadio1, self.lifeCycleSuspendBTN)
        MainWindow.setTabOrder(self.lifeCycleSuspendBTN, self.proxLifeRadio2)
        MainWindow.setTabOrder(self.proxLifeRadio2, self.T1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BASF-Custom"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#bfbfbf;\">MOTOR</span></p></body></html>"))
        self.startStopBTN.setText(_translate("MainWindow", "START"))
        self.revDirRadioBTN.setText(_translate("MainWindow", "REV"))
        self.fwdDirRadioBTN.setText(_translate("MainWindow", "FWD"))
        self.enableBTN.setText(_translate("MainWindow", "ENABLE"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#bfbfbf;\">Target Out RPM:</span></p></body></html>"))
        self.RPMinLineEdit.setPlaceholderText(_translate("MainWindow", "(Target RPM)"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#bfbfbf;\">Target In RPM:</span></p></body></html>"))
        self.RPMoutLineEdit.setPlaceholderText(_translate("MainWindow", "(Target RPM)"))
        self.stepRevBTN.setText(_translate("MainWindow", "<< STEP REV"))
        self.stepFwdBTN.setText(_translate("MainWindow", "STEP FWD >>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">STEP SIZE</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#bfbfbf;\">SIGNAL</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#bfbfbf;\">PWM Freq (Hz)</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#bfbfbf;\">Microstep (steps/rev):</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#bfbfbf;\">SENSORS</span></p></body></html>"))
        self.s1MSLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#bfbfbf;\">PX1</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#bfbfbf;\">PX2</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#bfbfbf;\">PX3</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#bfbfbf;\">P1 (PSI)</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic; color:#bfbfbf;\">Fs (Hz):</span></p></body></html>"))
        self.sensorBTN.setText(_translate("MainWindow", "SAMPLE"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#bfbfbf;\">L1 (lbf)</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#bfbfbf;\">FILE</span></p></body></html>"))
        self.newSessionBTN.setText(_translate("MainWindow", "NEW"))
        self.saveSessionBTN.setText(_translate("MainWindow", "SAVE SESSION"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Output File:</span></p></body></html>"))
        self.T1.setTabText(self.T1.indexOf(self.controlTab), _translate("MainWindow", "CONTROL"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#bfbfbf;\">PARAMETERS</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#bfbfbf;\">Steps Out</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#bfbfbf;\">Steps In</span></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#bfbfbf;\">Cut-Off Force (lbf)</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#bfbfbf;\">Run Time (min)</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#bfbfbf;\">RPM Out</span></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#bfbfbf;\">RPM In</span></p></body></html>"))
        self.paramSaveBTN.setText(_translate("MainWindow", "SAVE"))
        self.paramClearBTN.setText(_translate("MainWindow", "CLEAR"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#bfbfbf;\">STATUS</span></p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#bfbfbf;\">PX2</span></p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#bfbfbf;\">PX3</span></p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#bfbfbf;\">PX1</span></p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#bfbfbf;\">L1 (lbf)</span></p></body></html>"))
        self.lifeCycleStartBTN.setText(_translate("MainWindow", "START"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#bfbfbf;\">P1 (PSI)</span></p></body></html>"))
        self.lifeCycleSuspendBTN.setText(_translate("MainWindow", "SUSPEND"))
        self.T1.setTabText(self.T1.indexOf(self.lifeTestTab), _translate("MainWindow", "LIFE TEST"))


from pyqtgraph import PlotWidget
