import sys
import os
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
import jdatetime
from tkinter import messagebox

## ==> SPLASH SCREEN
from Ui.Ui_DateConverter import Ui_MainWindow
    
# SPLASH SCREEN
class DateConverter(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        #Remove Menubar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        def close():  
            #QApplication.quit()   
            #window.destroy()       
            sys.exit(app.exec())
            
            
        def checknumtxtbox():
            try:
                VAR1 = int(self.ui.edt_day.text())
                if VAR1 > 0 and VAR1 < 32 :
                    VAR1 = int(self.ui.edtmonth.text())
                    if VAR1 > 0 and VAR1 < 13 :
                        VAR1 = int(self.ui.edtyear.text())
                        if VAR1 > 999 and VAR1 < 10000 :
                            return True
                        else:
                            messagebox.showerror("خطا", "لطفا مقدار سال را درست وارد کنید.")
                    else:
                            messagebox.showerror("خطا", "لطفا مقدار ماه را درست وارد کنید.")
                else:
                            messagebox.showerror("خطا", "لطفا مقدار روز را درست وارد کنید.")
            except:
                print("Could not request results;")
            
        def checkemptytxtbox():
            if( self.ui.edt_day.text()):
                if( self.ui.edtmonth.text()):
                    if( self.ui.edtyear.text()):
                        res = checknumtxtbox()
                        if res:
                            return True
                    else:
                        messagebox.showerror("خطا", "لطفا سال را وارد کنید.")
                else:
                        messagebox.showerror("خطا", "لطفا ماه را وارد کنید.")
            else:
                        messagebox.showerror("خطا", "لطفا روز را وارد کنید.")
        def toShamsi():
            try:
                if(checkemptytxtbox()):
                    
                    day = int(self.ui.edt_day.text())
                    month = int(self.ui.edtmonth.text())
                    year = int(self.ui.edtyear.text())
                    result = str(jdatetime.date.fromgregorian(day =day , month = month, year= year))
                    self.ui.labeldate.setText(result)
            except:
                print("Could not request resultsmiladi;")
                
                
        def toMiladi():
            try:
                if(checkemptytxtbox()): 
                                
                    day = int(self.ui.edt_day.text())
                    month = int(self.ui.edtmonth.text())
                    year = int(self.ui.edtyear.text())
                    result = str(jdatetime.date(day = day , month = month , year= year ).togregorian())
                    self.ui.labeldate.setText(result)
            except:
                print("Could not request resultsmiladi;")
                      
        def checkRadio():
            if self.ui.radioButtonmiladi.isChecked():
                toMiladi()
            else:
                toShamsi()
        self.ui.radioButtonmiladi.setChecked(True)
        
        self.ui.convertbtn.clicked.connect(checkRadio)
        
        #Length TextBox
        self.ui.edt_day.setMaxLength(2)
        self.ui.edtmonth.setMaxLength(2)
        self.ui.edtyear.setMaxLength(4)
        
        
        self.ui.ExitButton.clicked.connect(close)
        self.show()
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DateConverter()
    sys.exit(app.exec())