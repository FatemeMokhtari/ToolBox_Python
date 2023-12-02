import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QRegularExpression as QRegExp)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QRegularExpressionValidator as QRegExpValidator)
from PySide6.QtWidgets import *
import jdatetime
from tkinter import messagebox


from Ui.Ui_DateConverter import Ui_MainWindow
    

class DateConverter(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        #Remove Menubar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        def close():                   
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
                
        def srv():
            if self.ui.radioButtonmiladi.isChecked():
                if int(self.ui.edt_day.text()) <= 31 and int(self.ui.edtmonth.text()) <=6:
                    return True
                elif int(self.ui.edt_day.text()) <= 30 and int(self.ui.edtmonth.text()) >=7:
                    return True
                else:    
                    messagebox.showerror("خطا", "لطفا مقدار ماه/روز را درست وارد کنید.")
                
                     
        def toMiladi():
            try:
                if(checkemptytxtbox()): 
                    if srv():            
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
        
        regex = QRegExp("^[ 0-9]+$")
        validator = QRegExpValidator(regex)       
        
        self.ui.edt_day.setValidator(validator)
        self.ui.edtmonth.setValidator(validator)
        self.ui.edtyear.setValidator(validator)
        
        
        self.ui.ExitButton.clicked.connect(close)
        self.show()
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DateConverter()
    sys.exit(app.exec())