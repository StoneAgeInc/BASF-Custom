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
"background-color: rgb(80,80,80);\n"
"background-image:  url(\"C:/Users/chris.antle/Documents/BASF/backgroundDark.jpg\");\n"
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
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 2, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.W1)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 5, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 6, 1, 1)
        self.controlWidget = QtWidgets.QWidget(self.W1)
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
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.controlLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.controlWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.execStepsEdit = QtWidgets.QLineEdit(self.controlWidget)
        self.execStepsEdit.setStyleSheet("QLineEdit\n"
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
        self.execStepsEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.execStepsEdit.setObjectName("execStepsEdit")
        self.horizontalLayout_6.addWidget(self.execStepsEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.controlLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stepRevBTN = QtWidgets.QPushButton(self.controlWidget)
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
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
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
        self.label_12 = QtWidgets.QLabel(self.controlWidget)
        self.label_12.setObjectName("label_12")
        self.controlLayout.addWidget(self.label_12)
        self.line_13 = QtWidgets.QFrame(self.controlWidget)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.controlLayout.addWidget(self.line_13)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.newSessionBTN = QtWidgets.QPushButton(self.controlWidget)
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
        self.saveSessionBTN = QtWidgets.QPushButton(self.controlWidget)
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
        self.controlLayout.addLayout(self.horizontalLayout_4)
        self.filePathLayout = QtWidgets.QHBoxLayout()
        self.filePathLayout.setSpacing(6)
        self.filePathLayout.setObjectName("filePathLayout")
        self.label_14 = QtWidgets.QLabel(self.controlWidget)
        self.label_14.setObjectName("label_14")
        self.filePathLayout.addWidget(self.label_14)
        self.fileNameEdit = QtWidgets.QLineEdit(self.controlWidget)
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
        self.controlLayout.addLayout(self.filePathLayout)
        self.gridLayout.addWidget(self.controlWidget, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.W1)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 7)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 5, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 5, 4, 1, 1)
        self.sensorWidget = QtWidgets.QWidget(self.W1)
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
        self.label_15 = QtWidgets.QLabel(self.sensorWidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.pressureLayout = QtWidgets.QHBoxLayout()
        self.pressureLayout.setSpacing(6)
        self.pressureLayout.setObjectName("pressureLayout")
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
        self.pressureLayout.addWidget(self.label_6)
        self.pressureLCD1 = QtWidgets.QLCDNumber(self.sensorWidget)
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
        self.pressureLCD1.setDigitCount(2)
        self.pressureLCD1.setObjectName("pressureLCD1")
        self.pressureLayout.addWidget(self.pressureLCD1)
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
        self.pressureLayout.addWidget(self.label_3)
        self.pressureLCD2 = QtWidgets.QLCDNumber(self.sensorWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pressureLCD2.setFont(font)
        self.pressureLCD2.setStyleSheet("QLCDNumber\n"
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
        self.pressureLCD2.setDigitCount(2)
        self.pressureLCD2.setObjectName("pressureLCD2")
        self.pressureLayout.addWidget(self.pressureLCD2)
        self.verticalLayout.addLayout(self.pressureLayout)
        self.label_19 = QtWidgets.QLabel(self.sensorWidget)
        self.label_19.setObjectName("label_19")
        self.verticalLayout.addWidget(self.label_19)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_18 = QtWidgets.QLabel(self.sensorWidget)
        self.label_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_8.addWidget(self.label_18)
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
        self.load1LCD.setDigitCount(2)
        self.load1LCD.setMode(QtWidgets.QLCDNumber.Dec)
        self.load1LCD.setProperty("value", 0.0)
        self.load1LCD.setObjectName("load1LCD")
        self.horizontalLayout_8.addWidget(self.load1LCD)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.label_16 = QtWidgets.QLabel(self.sensorWidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.s1MSLabel = QtWidgets.QLabel(self.sensorWidget)
        self.s1MSLabel.setObjectName("s1MSLabel")
        self.horizontalLayout_7.addWidget(self.s1MSLabel)
        self.proxRadio1 = QtWidgets.QRadioButton(self.sensorWidget)
        self.proxRadio1.setStyleSheet("QRadioButton::indicator {width: 15px; height: 15px; border-radius: 7px;} QRadioButton::indicator:unchecked {\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(0, 242, 0), stop: 1 rgb(0, 170, 0));\n"
"border: 2px solid gray;}")
        self.proxRadio1.setText("")
        self.proxRadio1.setCheckable(False)
        self.proxRadio1.setObjectName("proxRadio1")
        self.horizontalLayout_7.addWidget(self.proxRadio1)
        self.line = QtWidgets.QFrame(self.sensorWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_7.addWidget(self.line)
        self.label_10 = QtWidgets.QLabel(self.sensorWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.proxRadio2 = QtWidgets.QRadioButton(self.sensorWidget)
        self.proxRadio2.setStyleSheet("QRadioButton::indicator {width: 15px; height: 15px; border-radius: 7px;} QRadioButton::indicator:unchecked { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
"\n"
"border: 2px solid gray;}")
        self.proxRadio2.setText("")
        self.proxRadio2.setCheckable(False)
        self.proxRadio2.setObjectName("proxRadio2")
        self.horizontalLayout_7.addWidget(self.proxRadio2)
        self.label_17 = QtWidgets.QLabel(self.sensorWidget)
        self.label_17.setEnabled(False)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_7.addWidget(self.label_17)
        self.proxRadio5 = QtWidgets.QRadioButton(self.sensorWidget)
        self.proxRadio5.setStyleSheet("QRadioButton::indicator {width: 15px; height: 15px; border-radius: 7px;} QRadioButton::indicator:unchecked { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(200,50,50), stop: 1 rgb(145,5,5));\n"
"\n"
"border: 2px solid gray;}")
        self.proxRadio5.setText("")
        self.proxRadio5.setCheckable(False)
        self.proxRadio5.setObjectName("proxRadio5")
        self.horizontalLayout_7.addWidget(self.proxRadio5)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.s1MSLineEdit = QtWidgets.QLineEdit(self.sensorWidget)
        self.s1MSLineEdit.setEnabled(True)
        self.s1MSLineEdit.setStyleSheet("/**** QLineEdit (enabled) ****/\n"
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
"  background-color: rgb(200, 200, 200);\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(200, 200, 200);\n"
"}")
        self.s1MSLineEdit.setObjectName("s1MSLineEdit")
        self.verticalLayout.addWidget(self.s1MSLineEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.sensorWidget)
        self.buttonBox.setEnabled(False)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.line_11 = QtWidgets.QFrame(self.sensorWidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout.addWidget(self.line_11)
        self.gridLayout.addWidget(self.sensorWidget, 5, 5, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.plotWidget = PlotWidget(self.W1)
        self.plotWidget.setStyleSheet("QWidget#plotWidget\n"
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
        self.plotWidget.setObjectName("plotWidget")
        self.verticalLayout_4.addWidget(self.plotWidget)
        self.gridLayout.addLayout(self.verticalLayout_4, 7, 1, 1, 5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 5)
        MainWindow.setCentralWidget(self.W1)
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
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#bfbfbf;\">MOTOR CONTROL</span></p></body></html>"))
        self.startStopBTN.setText(_translate("MainWindow", "START"))
        self.revDirRadioBTN.setText(_translate("MainWindow", "REV"))
        self.fwdDirRadioBTN.setText(_translate("MainWindow", "FWD"))
        self.enableBTN.setText(_translate("MainWindow", "ENABLE"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#bfbfbf;\">Execution Steps:</span></p></body></html>"))
        self.execStepsEdit.setPlaceholderText(_translate("MainWindow", "(Total Steps)"))
        self.stepRevBTN.setText(_translate("MainWindow", "<< STEP REV"))
        self.stepFwdBTN.setText(_translate("MainWindow", "STEP FWD >>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">STEP SIZE</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#bfbfbf;\">SIGNAL PARAMETERS</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#bfbfbf;\">PWM Freq (Hz)</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#bfbfbf;\">Motor RPM:</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#bfbfbf;\">FILE</span></p></body></html>"))
        self.newSessionBTN.setText(_translate("MainWindow", "NEW"))
        self.saveSessionBTN.setText(_translate("MainWindow", "SAVE SESSION"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Output File:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#bfbfbf;\">BASF CUSTOM</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#bfbfbf;\">SENSORS</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#bfbfbf;\">PRESSURE</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">P1 (PSI)</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">P2 (PSI)</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#bfbfbf;\">LOAD</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-style:italic; color:#ffffff;\">L1 (lbf)</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#bfbfbf;\">PROXIMITY</span></p></body></html>"))
        self.s1MSLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">PX1</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#bfbfbf;\">PX2</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">PX3</span></p></body></html>"))


from pyqtgraph import PlotWidget
