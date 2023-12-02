import sys
import os
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QRegularExpression as QRegExp)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QRegularExpressionValidator as QRegExpValidator)
from PySide6.QtWidgets import *

## ==> SPLASH SCREEN
from Ui.Ui_UnitConverter import Ui_MainWindow



    
# SPLASH SCREEN
class OCR(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        
             
        
        def tst():
            if self.ui.txtUrl.text():
                num = int(self.ui.txtUrl.text())
                
                if self.ui.comboBox.currentText() == 'Centimeter to Meter':
                    self.ui.label_2.setText("{} سانتی متر برابر است با {} متر.".format(num, num / 100))
                elif self.ui.comboBox.currentText() == 'Meter to Centimeter':
                    self.ui.label_2.setText("{} متر برابر است با {} سانتی متر.".format(num, num * 100))
                elif self.ui.comboBox.currentText() == 'Centimeter to INCH':
                    self.ui.label_2.setText("{} سانتی متر برابر است با {} اینچ.".format(num, num / 2.54))
                elif self.ui.comboBox.currentText() == 'INCH to Centimeter':
                    self.ui.label_2.setText("{} اینچ برابر است با {} سانتی متر.".format(num, num * 2.54))
                elif self.ui.comboBox.currentText() == 'Centimeter to KiloMetre':
                    self.ui.label_2.setText("{} سانتی متر برابر است با {} کیلومتر.".format(num, num / 100000))
                elif self.ui.comboBox.currentText() == 'KiloMetre to Centimeter':
                    self.ui.label_2.setText("{} کیلومتر برابر است با {} سانتی متر.".format(num, num * 100000))
                elif self.ui.comboBox.currentText() == 'Centimeter to FOOT':
                    self.ui.label_2.setText("{} سانتی متر برابر است با {} فوت.".format(num, num / 30.48))
                elif self.ui.comboBox.currentText() == 'FOOT to Centimeter':
                    self.ui.label_2.setText("{} فوت برابر است با {} سانتی متر.".format(num, num * 30.48))
                elif self.ui.comboBox.currentText() == 'Kilometre to Mile':
                    self.ui.label_2.setText("{} کیلومتر برابر است با {} مایل".format(num, num / 1.609))
                elif self.ui.comboBox.currentText() == 'Mile to Kilometre':
                    self.ui.label_2.setText("{} مایل برابر است با {} کیلومتر".format(num, num * 1.609))
                
                
                elif self.ui.comboBox.currentText()== 'Gram to Kilogram':
                    self.ui.label_2.setText("{} گرم برابر است با {} کیلوگرم".format(num, num / 1000))
                elif self.ui.comboBox.currentText() == 'Kilogram to Gram':
                    self.ui.label_2.setText("{} کیلوگرم برابر است با {} گرم".format(num, num * 1000))
                elif self.ui.comboBox.currentText() == 'Kilogram to Tonne':
                    self.ui.label_2.setText("{} کیلوگرم برابر است با {} تن".format(num, num / 1000))
                elif self.ui.comboBox.currentText() == 'Tonne to Kilogram':
                    self.ui.label_2.setText("{} تن برابر است با {} کیلوگرم".format(num, num * 1000))
                elif self.ui.comboBox.currentText() == 'Milligram to Kilogram':
                    self.ui.label_2.setText("{} میلی گرم برابر است با {} کیلوگرم".format(num, num / 1000000))
                elif self.ui.comboBox.currentText() == 'Kilogram to Milligram':
                    self.ui.label_2.setText("{} کیلوگرم برابر است با {} میلی گرم".format(num, num * 1000000))
                elif self.ui.comboBox.currentText() == 'Milligram to Gram':
                    self.ui.label_2.setText("{} میلی گرم برابر است با {} گرم".format(num, num / 1000))
                elif self.ui.comboBox.currentText() == 'Gram to Milligram':
                    self.ui.label_2.setText("{} گرم برابر است با {} میلی گرم".format(num, num * 1000))
                elif self.ui.comboBox.currentText() == 'kilogram to pound (lb)':
                    self.ui.label_2.setText("{} کیلوگرم برابر است با {} پوند".format(num, num * 2.20462))
                elif self.ui.comboBox.currentText() == 'pound (lb) to Kilogram':
                    self.ui.label_2.setText("{} پوند برابر است با {} کیلوگرم".format(num, num / 2.20462))
                elif self.ui.comboBox.currentText() == 'Micrograms to gram':
                    self.ui.label_2.setText("{} میکروگرم برابر است با {} گرم".format(num, num / 1e+6))
                elif self.ui.comboBox.currentText() == 'Micrograms to Kilogram':
                    self.ui.label_2.setText("{} میکروگرم برابر است با {} کیلوگرم".format(num, num / 1e+9))
                    
                    
                elif self.ui.comboBox.currentText() == 'Celsius to Fahrenheit':
                    self.ui.label_2.setText("{} سلسیوس برابر است با {} فارنهایت".format(num, (num * 9.5) + 32))
                elif self.ui.comboBox.currentText() == 'Celsius to Kelvin':
                    self.ui.label_2.setText("{} سلسیوس برابر است با {} کلوین".format(num, num + 273.15))
                elif self.ui.comboBox.currentText() == 'Fahrenheit to Celsius':
                    self.ui.label_2.setText("{} فارنهایت برابر است با {} سلسیوس".format(num, (num - 32) * 5.9))
                elif self.ui.comboBox.currentText() == 'Fahrenheit to Kelvin':
                    self.ui.label_2.setText("{} فارنهایت برابر است با {} کلوین".format(num, (num - 32) * 5.9 + 273.15))
                elif self.ui.comboBox.currentText() == 'Kelvin to Celsius':
                    self.ui.label_2.setText("{} کلوین برابر است با {} سلسیوس".format(num, num - 273.15))
                elif self.ui.comboBox.currentText() == 'Kelvin to Fahrenheit':
                    self.ui.label_2.setText("{} کلوین برابر است با {} فارنهایت".format(num, (num - 273.15) * 9.5 + 32))
                    
                elif self.ui.comboBox.currentText() == 'Second to Minute':
                    self.ui.label_2.setText("{} ثانیه برابر است با {} دقیقه".format(num, num / 60))
                elif self.ui.comboBox.currentText() == 'Minute to Second':
                    self.ui.label_2.setText("{} دقیقه برابر است با {} ثانیه".format(num, num * 60))
                elif self.ui.comboBox.currentText() == 'Second to Hour':
                    self.ui.label_2.setText("{} ثانیه برابر است با {} ساعت".format(num, num / 3600))
                elif self.ui.comboBox.currentText() == 'Minute to Hour':
                    self.ui.label_2.setText("{} دقیقه برابر است با {} ساعت".format(num, num / 60))
                elif self.ui.comboBox.currentText() == 'Hour to Minute':
                    self.ui.label_2.setText("{} ساعت برابر است با {} دقیقه".format(num, num * 60))
                elif self.ui.comboBox.currentText() == 'Day to Hour':
                    self.ui.label_2.setText("{} روز برابر با {} ساعت".format(num, num * 24))
                elif self.ui.comboBox.currentText() == 'Hour to Day':
                    self.ui.label_2.setText("{} ساعت برابر است با {} روز".format(num, num / 24))
            else:
                print("enter number")
                  
        list_text = ['Centimeter to Meter', 'Meter to Centimeter', 'Centimeter to INCH', 'INCH to Centimeter', 'Centimeter to KiloMetre'
                     ,'KiloMetre to Centimeter', 'Centimeter to FOOT', 'FOOT to Centimeter', 'Kilometre to Mile', 'Mile to Kilometre'
                     ,'Gram to Kilogram', 'Kilogram to Gram', 'Kilogram to Tonne', 'Tonne to Kilogram' ,'Milligram to Kilogram', 'Kilogram to Milligram'
                     ,'Milligram to Gram', 'Gram to Milligram', 'kilogram to pound (lb)','pound (lb) to Kilogram','Micrograms to gram','Micrograms to Kilogram'
                     ,'Celsius to Fahrenheit','Celsius to Kelvin','Fahrenheit to Celsius','Fahrenheit to Kelvin','Kelvin to Celsius','Kelvin to Fahrenheit'
                     ,'Second to Minute','Minute to Second','Second to Hour','Minute to Hour','Hour to Minute','Day to Hour','Hour to Day']
        
        def close():
            sys.exit(app.exec())
            
        
        self.ui.ExitButton.clicked.connect(close)    
        self.ui.comboBox.addItems(list_text)
        self.ui.txtUrl.textChanged.connect(tst)
        self.ui.comboBox.currentTextChanged.connect(tst)
        self.ui.label_2.setWordWrap(True)
        
        regex = QRegExp("^[ 0-9]+$")
        validator = QRegExpValidator(regex)        
        self.ui.txtUrl.setValidator(validator)
        
        self.show()
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OCR()
    sys.exit(app.exec())



