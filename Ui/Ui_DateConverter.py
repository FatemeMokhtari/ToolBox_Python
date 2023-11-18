# Form implementation generated from reading ui file 'DateConverter.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 550)
        MainWindow.setStyleSheet("QMainWindow{\n"
"background-color: rgb(255, 255, 255);\n"
"border:2px solid #14213d;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 700, 550))
        self.frame.setStyleSheet("QFrame{\n"
"\n"
"    background-color:#14213d;\n"
"    border:6px solid #FFDB70;\n"
"\n"
"border-radius:15px;\n"
"\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.framemonth = QtWidgets.QFrame(parent=self.frame)
        self.framemonth.setGeometry(QtCore.QRect(250, 90, 200, 200))
        self.framemonth.setStyleSheet("QFrame {\n"
"    border:5px solid #a7a7a7;\n"
"    border-radius: 100px;\n"
"}\n"
"QFrame:hover {\n"
"    border: 5px solid #ffdb70;\n"
"}")
        self.framemonth.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.framemonth.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.framemonth.setObjectName("framemonth")
        self.label_5 = QtWidgets.QLabel(parent=self.framemonth)
        self.label_5.setGeometry(QtCore.QRect(19, 40, 161, 25))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: none;\n"
"color:white;\n"
"border: none;\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.edtmonth = QtWidgets.QLineEdit(parent=self.framemonth)
        self.edtmonth.setGeometry(QtCore.QRect(30, 110, 141, 30))
        self.edtmonth.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edtmonth.setFont(font)
        self.edtmonth.setStyleSheet("QLineEdit {\n"
"    border: 1px solid white;\n"
"    border-radius:10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 3px solid #ffdb70;\n"
"}")
        self.edtmonth.setInputMask("")
        self.edtmonth.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.edtmonth.setObjectName("edtmonth")
        self.label_2 = QtWidgets.QLabel(parent=self.framemonth)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:none;\n"
"color: #ffdb70;")
        self.label_2.setObjectName("label_2")
        self.radioButtonmiladi = QtWidgets.QRadioButton(parent=self.frame)
        self.radioButtonmiladi.setGeometry(QtCore.QRect(150, 320, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        font.setPointSize(12)
        self.radioButtonmiladi.setFont(font)
        self.radioButtonmiladi.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.radioButtonmiladi.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButtonmiladi.setObjectName("radioButtonmiladi")
        self.labeldate = QtWidgets.QLabel(parent=self.frame)
        self.labeldate.setGeometry(QtCore.QRect(100, 440, 501, 71))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.labeldate.setFont(font)
        self.labeldate.setStyleSheet("border:none;\n"
"color: rgb(255, 255, 255);")
        self.labeldate.setText("")
        self.labeldate.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labeldate.setObjectName("labeldate")
        self.frameyear = QtWidgets.QFrame(parent=self.frame)
        self.frameyear.setGeometry(QtCore.QRect(30, 90, 200, 200))
        self.frameyear.setStyleSheet("QFrame {\n"
"    border:5px solid #a7a7a7;\n"
"\n"
"    border-radius: 100px;\n"
"}\n"
"QFrame:hover {\n"
"    border: 5px solid #ffdb70;\n"
"}")
        self.frameyear.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameyear.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameyear.setObjectName("frameyear")
        self.label_6 = QtWidgets.QLabel(parent=self.frameyear)
        self.label_6.setGeometry(QtCore.QRect(19, 40, 161, 25))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: none;\n"
"color:white;\n"
"border: none;\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.edtyear = QtWidgets.QLineEdit(parent=self.frameyear)
        self.edtyear.setGeometry(QtCore.QRect(30, 110, 141, 30))
        self.edtyear.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edtyear.setFont(font)
        self.edtyear.setStyleSheet("QLineEdit {\n"
"    border: 1px solid white;\n"
"    border-radius:10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 3px solid #ffdb70;\n"
"}")
        self.edtyear.setInputMask("")
        self.edtyear.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.edtyear.setObjectName("edtyear")
        self.label = QtWidgets.QLabel(parent=self.frameyear)
        self.label.setGeometry(QtCore.QRect(40, 80, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        self.label.setFont(font)
        self.label.setStyleSheet("border:none;\n"
"color: #ffdb70;")
        self.label.setObjectName("label")
        self.frameday = QtWidgets.QFrame(parent=self.frame)
        self.frameday.setGeometry(QtCore.QRect(470, 90, 200, 200))
        self.frameday.setStyleSheet("QFrame {\n"
"    border:5px solid #a7a7a7;\n"
"    border-radius: 100px;\n"
"}\n"
"QFrame:hover {\n"
"    border: 5px solid #ffdb70;\n"
"}")
        self.frameday.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameday.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameday.setObjectName("frameday")
        self.label_7 = QtWidgets.QLabel(parent=self.frameday)
        self.label_7.setGeometry(QtCore.QRect(19, 40, 161, 25))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: none;\n"
"color:white;\n"
"border: none;\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.edt_day = QtWidgets.QLineEdit(parent=self.frameday)
        self.edt_day.setGeometry(QtCore.QRect(30, 110, 141, 30))
        self.edt_day.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edt_day.setFont(font)
        self.edt_day.setStyleSheet("QLineEdit {\n"
"    border: 1px solid white;\n"
"    border-radius:10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border:3px solid #ffdb70;\n"
"}")
        self.edt_day.setInputMask("")
        self.edt_day.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.edt_day.setObjectName("edt_day")
        self.label_3 = QtWidgets.QLabel(parent=self.frameday)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:none;\n"
"color: #ffdb70;")
        self.label_3.setObjectName("label_3")
        self.radioButtonshamsi = QtWidgets.QRadioButton(parent=self.frame)
        self.radioButtonshamsi.setGeometry(QtCore.QRect(340, 320, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        font.setPointSize(12)
        self.radioButtonshamsi.setFont(font)
        self.radioButtonshamsi.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.radioButtonshamsi.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButtonshamsi.setObjectName("radioButtonshamsi")
        self.convertbtn = QtWidgets.QPushButton(parent=self.frame)
        self.convertbtn.setGeometry(QtCore.QRect(300, 380, 100, 35))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        font.setPointSize(12)
        self.convertbtn.setFont(font)
        self.convertbtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.convertbtn.setStyleSheet("\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"background-color:qlineargradient(spread:pad, x1:0.006, y1:0.585, x2:1, y2:0, stop:0.369318 rgba(246, 176, 66, 255), stop:1 rgba(249, 237, 78, 255));")
        self.convertbtn.setObjectName("convertbtn")
        self.Title = QtWidgets.QLabel(parent=self.frame)
        self.Title.setGeometry(QtCore.QRect(30, 18, 231, 31))
        font = QtGui.QFont()
        font.setFamily("A Salamat")
        font.setPointSize(9)
        font.setBold(True)
        
        font.setKerning(True)
        self.Title.setFont(font)
        self.Title.setStyleSheet("\n"
"color: #a7a7a7;\n"
"border:none;")
        self.Title.setScaledContents(False)
        self.Title.setObjectName("Title")
        self.ExitButton = QtWidgets.QPushButton(parent=self.frame)
        self.ExitButton.setGeometry(QtCore.QRect(655, 20, 25, 25))
        self.ExitButton.setStyleSheet("")
        self.ExitButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\Project\Final\ToolBox\Images\Exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ExitButton.setIcon(icon)
        self.ExitButton.setIconSize(QtCore.QSize(20, 20))
        self.ExitButton.setFlat(True)
        self.ExitButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExitButton.setObjectName("ExitButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.edtyear, self.edtmonth)
        MainWindow.setTabOrder(self.edtmonth, self.edt_day)
        MainWindow.setTabOrder(self.edt_day, self.radioButtonmiladi)
        MainWindow.setTabOrder(self.radioButtonmiladi, self.radioButtonshamsi)
        MainWindow.setTabOrder(self.radioButtonshamsi, self.convertbtn)
        MainWindow.setTabOrder(self.convertbtn, self.ExitButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "ماه را وارد کنید"))
        self.label_2.setText(_translate("MainWindow", "مثال  12 - 8   "))
        self.radioButtonmiladi.setText(_translate("MainWindow", "تبدیل به میلادی"))
        self.label_6.setText(_translate("MainWindow", "سال را وارد کنید"))
        self.label.setText(_translate("MainWindow", "مثال 2020 - 1378   "))
        self.label_7.setText(_translate("MainWindow", "روز را وارد کنید"))
        self.label_3.setText(_translate("MainWindow", "مثال 21 - 5     "))
        self.radioButtonshamsi.setText(_translate("MainWindow", "تبدیل به شمسی"))
        self.convertbtn.setText(_translate("MainWindow", "تبدیل"))
        self.Title.setText(_translate("MainWindow", "Toolbox <span style=\" font-size:11pt; font-weight:600;\">-</span> Date Converter"))
