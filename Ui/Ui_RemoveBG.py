# Form implementation generated from reading ui file 'RemoveBG.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *


class Ui_RemoveBG(object):
    def setupUi(self, RemoveBG):
        RemoveBG.setObjectName("RemoveBG")
        RemoveBG.resize(500, 400)
        RemoveBG.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=RemoveBG)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color:#14213d;\n"
"    border:6px solid #FFDB70;\n"
"border-radius:15px;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.btn_digits_2 = QtWidgets.QPushButton(parent=self.frame)
        self.btn_digits_2.setEnabled(True)
        self.btn_digits_2.setGeometry(QtCore.QRect(340, 180, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        font.setPointSize(10)
        self.btn_digits_2.setFont(font)
        self.btn_digits_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_digits_2.setStyleSheet("QPushButton{\n"
"border: 2px solid qlineargradient(spread:pad, x1:0.006, y1:0.585, x2:1, y2:0, stop:0.369318 rgba(246, 176, 66, 255), stop:1 rgba(249, 237, 78, 255));\n"
"border-radius:20px;\n"
"background-color:qlineargradient(spread:pad, x1:0.006, y1:0.585, x2:1, y2:0, stop:0.369318 rgba(246, 176, 66, 255), stop:1 rgba(249, 237, 78, 255));\n"
"color: black;   \n"
"}\n"
"QPushButton:disabled{\n"
"background-color: rgb(167, 167, 167);\n"
"border:none;\n"
"    color:#14213d;\n"
"}\n"
"")
        self.btn_digits_2.setCheckable(True)
        self.btn_digits_2.setChecked(False)
        self.btn_digits_2.setObjectName("btn_digits_2")
        self.btn_upload = QtWidgets.QPushButton(parent=self.frame)
        self.btn_upload.setEnabled(True)
        self.btn_upload.setGeometry(QtCore.QRect(70, 180, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        font.setPointSize(13)
        self.btn_upload.setFont(font)
        self.btn_upload.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_upload.setStyleSheet("QPushButton{\n"
"\n"
"border: 2px solid qlineargradient(spread:pad, x1:0.006, y1:0.585, x2:1, y2:0, stop:0.369318 rgba(246, 176, 66, 255), stop:1 rgba(249, 237, 78, 255));\n"
"border-radius:20px;\n"
"background-color:qlineargradient(spread:pad, x1:0.006, y1:0.585, x2:1, y2:0, stop:0.369318 rgba(246, 176, 66, 255), stop:1 rgba(249, 237, 78, 255));\n"
"color: black;   \n"
"}\n"
"QPushButton:disabled{\n"
"background-color: rgb(167, 167, 167);\n"
"border:none;\n"
"    color:#14213d;\n"
"}")
        self.btn_upload.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"D:\Project\Final\ToolBox\Images\chooseImage.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_upload.setIcon(icon)
        self.btn_upload.setIconSize(QtCore.QSize(35, 35))
        self.btn_upload.setCheckable(True)
        self.btn_upload.setChecked(False)
        self.btn_upload.setObjectName("btn_upload")
        self.Title = QtWidgets.QLabel(parent=self.frame)
        self.Title.setGeometry(QtCore.QRect(32, 18, 231, 31))
        font = QtGui.QFont()
        font.setFamily("A Salamat")
        font.setPointSize(10)
        font.setBold(False)
        font.setKerning(True)
        self.Title.setFont(font)
        self.Title.setStyleSheet("\n"
"color: #a7a7a7;\n"
"border:none;")
        self.Title.setScaledContents(False)
        self.Title.setObjectName("Title")
        self.ExitButton = QtWidgets.QPushButton(parent=self.frame)
        self.ExitButton.setGeometry(QtCore.QRect(455, 20, 25, 25))
        self.ExitButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExitButton.setStyleSheet("")
        self.ExitButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(r"D:\Project\Final\ToolBox\Images\Exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ExitButton.setIcon(icon1)
        self.ExitButton.setIconSize(QtCore.QSize(20, 20))
        self.ExitButton.setFlat(True)
        self.ExitButton.setObjectName("ExitButton")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(150, 160, 141, 35))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("border:none;\n"
"color: white;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setGeometry(QtCore.QRect(290, 165, 20, 20))
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(r"D:\Project\Final\ToolBox\Images\clear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(158, 195, 135, 36))
        self.label_2.setStyleSheet("border:none;")
        self.label_2.setText("")
        
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.btn_digits_2.raise_()
        self.btn_upload.raise_()
        self.Title.raise_()
        self.ExitButton.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 80, 461, 291))
        self.frame_2.setStyleSheet("border:none;\n"
"background-color: rgb(20, 33, 61);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.progressBar = QtWidgets.QProgressBar(parent=self.frame_2)
        self.progressBar.setGeometry(QtCore.QRect(30, 240, 400, 23))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    \n"
"    background-color: rgb(98, 114, 164);\n"
"    color: rgb(200, 200, 200);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setProperty("value", 100)
        self.progressBar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.Direction.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(-8, -100, 455, 350))
        self.label_3.setStyleSheet("background-color: rgb(20, 33, 61);")
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(185, 170, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_3.raise_()
        self.label_4.raise_()
        self.progressBar.raise_()
        RemoveBG.setCentralWidget(self.centralwidget)

        self.retranslateUi(RemoveBG)
        QtCore.QMetaObject.connectSlotsByName(RemoveBG)

    def retranslateUi(self, RemoveBG):
        _translate = QtCore.QCoreApplication.translate
        RemoveBG.setWindowTitle(_translate("RemoveBG", "MainWindow"))
        self.btn_digits_2.setText(_translate("RemoveBG", "حذف پس زمینه"))
        self.Title.setText(_translate("RemoveBG", "Toolbox <span style=\" font-size:11pt; font-weight:600;\">-</span> Remove Background"))        
        self.label_4.setText(_translate("RemoveBG", "انجام شد"))