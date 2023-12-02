import sys
import os
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *

## ==> SPLASH SCREEN
from Ui.Ui_SplashScreen import Ui_SplashScreen

## ==> MAIN WINDOW
from Ui.Ui_Main import Ui_MainWindow

## ==> GLOBALS
counter = 0

# YOUR APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.uimain = Ui_MainWindow()
        self.uimain.setupUi(self)

        
        pyexec = sys.executable
        ### def for Run Windows
        def translate():
            dir_path = os.path.dirname(os.path.realpath(__file__))            
            PathPy = dir_path +"\\Translate.py"
            os.system('%s %s' % (pyexec, PathPy))
        
        
        def password():
            dir_path = os.path.dirname(os.path.realpath(__file__))            
            PathPy = dir_path +"\\Password_Generator.py"
            os.system('%s %s' % (pyexec, PathPy))
            
            
        def barcode():
            dir_path = os.path.dirname(os.path.realpath(__file__))            
            PathPy = dir_path +"\\QrCode.py"
            os.system('%s %s' % (pyexec, PathPy))
            
            
        def number():
            dir_path = os.path.dirname(os.path.realpath(__file__))            
            PathPy = dir_path +"\\Num_To_Words.py"
            os.system('%s %s' % (pyexec, PathPy))
            
            
            
        def ocr():
            dir_path = os.path.dirname(os.path.realpath(__file__))            
            PathPy = dir_path +"\\OCR.py"
            os.system('%s %s' % (pyexec, PathPy))
            
            
        def gif():
            dir_path = os.path.dirname(os.path.realpath(__file__))            
            PathPy = dir_path +"\\GIF.py"
            os.system('%s %s' % (pyexec, PathPy))
            
            
            
        def remove():
            dir_path = os.path.dirname(os.path.realpath(__file__))            
            PathPy = dir_path +"\\RemoveBG.py"
            os.system('%s %s' % (pyexec, PathPy))
            
            
        def pdf():
            dir_path = os.path.dirname(os.path.realpath(__file__))            
            PathPy = dir_path +"\\PDF.py"
            os.system('%s %s' % (pyexec, PathPy))
            
            
        def date():
            dir_path = os.path.dirname(os.path.realpath(__file__))            
            PathPy = dir_path +"\\DateConverter.py"
            os.system('%s %s' % (pyexec, PathPy))
            
            
            
        def weather():
            dir_path = os.path.dirname(os.path.realpath(__file__))            
            PathPy = dir_path +"\\Weather.py"
            os.system('%s %s' % (pyexec, PathPy))
        
        
        
        def unit():
            dir_path = os.path.dirname(os.path.realpath(__file__))            
            PathPy = dir_path +"\\UnitConverter.py"
            os.system('%s %s' % (pyexec, PathPy))
            
        def About():
            dir_path = os.path.dirname(os.path.realpath(__file__))            
            PathPy = dir_path +"\\AboutApp.py"
            os.system('%s %s' % (pyexec, PathPy))   
                
        def close():
            sys.exit(app.exec())            
            
               
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
                
        ### Click Buttons
        self.uimain.Translate.clicked.connect(translate)
        self.uimain.PassBtn.clicked.connect(password)
        self.uimain.NumtowordBtn.clicked.connect(number)
        self.uimain.QrcodeBtn.clicked.connect(barcode)
        self.uimain.OCRBtn.clicked.connect(ocr)
        self.uimain.GifBtn.clicked.connect(gif)
        self.uimain.PdfBtn.clicked.connect(pdf)
        self.uimain.RemoveBtn.clicked.connect(remove)
        self.uimain.DateBtn.clicked.connect(date)
        self.uimain.WeatherBtn.clicked.connect(weather)
        self.uimain.ExitButton.clicked.connect(close)
        self.uimain.ConvertUnitBtn.clicked.connect(unit)
        self.uimain.AboutmeBtn.clicked.connect(About)
        # MAIN WINDOW LABEL
        #QtCore.QTimer.singleShot(1500, lambda: self.ui.label.setText("<strong>THANKS</strong> FOR WATCHING"))
        #QtCore.QTimer.singleShot(1500, lambda: self.setStyleSheet("background-color: #222; color: #FFF"))


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        
        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        #self.shadow = QGraphicsDropShadowEffect(self)
        #self.shadow.setBlurRadius(20)
        #self.shadow.setXOffset(0)
        #self.shadow.setYOffset(0)
        #self.shadow.setColor(QColor(0, 0, 0, 60))
        #self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        
        
        
        
        
        
        
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())
