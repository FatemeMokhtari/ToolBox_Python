# Form implementation generated from reading ui file 'Translate.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *

class Ui_Translate(object):
    def setupUi(self, Translate):
        Translate.setObjectName("Translate")
        Translate.resize(650, 600)
        Translate.setWindowOpacity(1.0)
        Translate.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        Translate.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=Translate)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 650, 600))
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
        self.DestFrame = QtWidgets.QFrame(parent=self.frame)
        self.DestFrame.setGeometry(QtCore.QRect(30, 360, 581, 221))
        self.DestFrame.setStyleSheet("QFrame {\n"
"    border:4px solid #a7a7a7;\n"
"    border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"    border: 4px solid #ffdb70;\n"
"}")
        self.DestFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.DestFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.DestFrame.setObjectName("DestFrame")
        self.txtDest = QtWidgets.QPlainTextEdit(parent=self.DestFrame)
        self.txtDest.setGeometry(QtCore.QRect(20, 30, 541, 171))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        font.setPointSize(12)
        font.setBold(False)
        self.txtDest.setFont(font)
        self.txtDest.setStyleSheet("QPlainTextEdit{\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"padding:15px 1px 2px 5px;\n"
"\n"
"\n"
"}")
        self.txtDest.setObjectName("txtDest")
        self.SrcFrame = QtWidgets.QFrame(parent=self.frame)
        self.SrcFrame.setGeometry(QtCore.QRect(30, 100, 581, 221))
        self.SrcFrame.setStyleSheet("QFrame {\n"
"    border:4px solid #a7a7a7;\n"
"    border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"    border: 4px solid #ffdb70;\n"
"}")
        self.SrcFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.SrcFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.SrcFrame.setObjectName("SrcFrame")
        self.txtSrc = QtWidgets.QPlainTextEdit(parent=self.SrcFrame)
        self.txtSrc.setGeometry(QtCore.QRect(20, 20, 541, 171))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        font.setPointSize(12)
        font.setBold(False)
        self.txtSrc.setFont(font)
        self.txtSrc.setStyleSheet("QPlainTextEdit{\n"
"\n"
"color: rgb(255, 255, 255);\n"
"padding:15px 1px 2px 5px;\n"
"border:none;\n"
"    \n"
"}")
        self.txtSrc.setObjectName("txtSrc")
        self.MicButton = QtWidgets.QPushButton(parent=self.SrcFrame)
        self.MicButton.setGeometry(QtCore.QRect(545, 12, 20, 20))
        self.MicButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.MicButton.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"border-radius: 20px;\n"
"  min-height: 7px;\n"
"  min-width: 7px;\n"
"\n"
"}")
        self.MicButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\Project\Final\ToolBox\Images\mic.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.MicButton.setIcon(icon)
        self.MicButton.setIconSize(QtCore.QSize(17, 17))
        self.MicButton.setFlat(False)
        self.MicButton.setObjectName("MicButton")
        self.comboDest = QtWidgets.QComboBox(parent=self.frame)
        self.comboDest.setGeometry(QtCore.QRect(53, 350, 200, 22))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.comboDest.setFont(font)
        self.comboDest.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.comboDest.setStyleSheet("QComboBox{\n"
"border:2px solid #ffdb70;\n"
"    background-color: rgb(255, 255, 255);\n"
"padding-left:5px;\n"
"}\n"
"QFrame{\n"
"border:none;\n"
"padding-left:5px;\n"
"border-radius:3px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.comboDest.setObjectName("comboDest")
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
        self.ExitButton.setGeometry(QtCore.QRect(605, 20, 25, 25))
        self.ExitButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ExitButton.setStyleSheet("")
        self.ExitButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\Project\Final\ToolBox\Images\Exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ExitButton.setIcon(icon1)
        self.ExitButton.setIconSize(QtCore.QSize(20, 20))
        self.ExitButton.setFlat(True)
        self.ExitButton.setObjectName("ExitButton")
        self.comboSrc = QtWidgets.QComboBox(parent=self.frame)
        self.comboSrc.setGeometry(QtCore.QRect(53, 90, 200, 22))
        font = QtGui.QFont()
        font.setFamily("Gandom")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.comboSrc.setFont(font)
        self.comboSrc.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.comboSrc.setStyleSheet("QComboBox{\n"
"border:2px solid #ffdb70;\n"
"    background-color: rgb(255, 255, 255);\n"
"padding-left:5px;\n"
"}\n"
"QFrame{\n"
"border:none;\n"
"padding-left:5px;\n"
"border-radius:3px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.comboSrc.setObjectName("comboSrc")
        Translate.setCentralWidget(self.centralwidget)

        self.retranslateUi(Translate)
        QtCore.QMetaObject.connectSlotsByName(Translate)
        Translate.setTabOrder(self.txtSrc, self.comboSrc)
        Translate.setTabOrder(self.comboSrc, self.comboDest)
        Translate.setTabOrder(self.comboDest, self.MicButton)
        Translate.setTabOrder(self.MicButton, self.txtDest)
        Translate.setTabOrder(self.txtDest, self.ExitButton)

    def retranslateUi(self, Translate):
        _translate = QtCore.QCoreApplication.translate
        Translate.setWindowTitle(_translate("Translate", "Translate"))
        self.txtDest.setPlaceholderText(_translate("Translate", "ترجمه"))
        self.Title.setText(_translate("Translate", "Toolbox <span style=\" font-size:11pt; font-weight:600;\">-</span> Translate"))