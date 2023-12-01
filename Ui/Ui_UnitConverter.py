# Form implementation generated from reading ui file 'UnitConverter.ui'
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
        MainWindow.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 500, 300))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color:#14213d;\n"
"    border:6px solid #FFDB70;\n"
"border-radius:15px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.Title = QtWidgets.QLabel(parent=self.frame)
        self.Title.setGeometry(QtCore.QRect(32, 18, 185, 31))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"D:\Project\Final\ToolBox/Images/Exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ExitButton.setIcon(icon)
        self.ExitButton.setIconSize(QtCore.QSize(20, 20))
        self.ExitButton.setFlat(True)
        self.ExitButton.setObjectName("ExitButton")
        self.comboBox = QtWidgets.QComboBox(parent=self.frame)
        self.comboBox.setGeometry(QtCore.QRect(150, 80, 198, 25))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox{\n"
"border:2px solid #ffdb70;\n"
"background-color: rgb(255, 255, 255);\n"
"padding-left:10px;\n"
"}\n"
"QListView{\n"
"border:none;\n"
"border-radius:5px;\n"
"background-color: rgb(255, 255, 255);\n"
"margin:5px;\n"
"}\n"
"QListView::item {\n"
"padding:3px;\n"
"padding-top:6px;\n"
"padding-left:5px;\n"
"height: 8px;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.txtUrl = QtWidgets.QLineEdit(parent=self.frame)
        self.txtUrl.setGeometry(QtCore.QRect(150, 130, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        font.setPointSize(10)
        self.txtUrl.setFont(font)
        self.txtUrl.setStyleSheet("QLineEdit {\n"
"    border-radius:5px;\n"
"    margin: 0;\n"
"padding-left:6px;\n"
"padding-right:6px;\n"
"    color: rgb(20, 33, 61);\n"
"}\n"
"")
        self.txtUrl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtUrl.setObjectName("txtUrl")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 190, 421, 81))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:none;\n"
"color: white;")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "<html><head/><body><p>Toolbox <span style=\" font-size:11pt; font-weight:600;\">-</span> Unit Converter</p></body></html>"))