import sys
import os
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from googletrans import Translator,LANGUAGES
import speech_recognition as sr
from translate import Translator as translatevoice
from num2words import num2words


## ==> Num to Word
from Ui.Ui_Num_To_Words import Ui_MainWindow



    
# Num to Word
class NumToWords(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        def numberclose():  
            #QApplication.quit()   
            #window.destroy()       
            sys.exit(app.exec())
            
            
        def timertxt():
            QtCore.QTimer.singleShot(2500,convertNum)  
            
            
              
        self.ui.ExitButton.clicked.connect(numberclose)
        def convertNum():  
            try:         
                text = self.ui.lineEdit.text()
                text_int = int(text)
                s = num2words(text_int, lang ='fa')
                self.ui.label.setText(s)
            except:
                print("Could not request results;")                
                self.ui.label.setText("")
        
                
        
        self.ui.lineEdit.textChanged.connect(timertxt)
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.label.setWordWrap(True)
        
        self.ui.lineEdit.setMaxLength(18)
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NumToWords()
    sys.exit(app.exec())
