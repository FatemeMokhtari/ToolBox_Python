import qrcode
import sys
from tkinter import filedialog
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from tkinter import messagebox


from Ui.Ui_QrCode import Ui_MainWindow


class QrCode(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ## REMOVE TITLE BAR        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        
        def checktxt():
            if self.ui.txtUrl.text():
                return True
            else:
                messagebox.showerror("خطا", "متن را وارد کنید")
             
        def location():
            if checktxt():            
                filepathgif, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save file", "", "Image files (*.png)")
                if len(filepathgif) > 0:                
                    generate(pathh=filepathgif)
            
        def generate(pathh):
            try:
                img = qrcode.make(self.ui.txtUrl.text())
                type(img)
                img.save(pathh)
                
                QtCore.QTimer.singleShot(1000, lambda:self.ui.label_2.setVisible(True))
                QtCore.QTimer.singleShot(4000, lambda:self.ui.label_2.setVisible(False))
            except:
                print("error")

        def show():
            if checktxt(): 
                img = qrcode.make(self.ui.txtUrl.text())
                type(img)
                img.show() 
        
        def close():  
                  
            sys.exit(app.exec())
            
        def clear():
            self.ui.txtUrl.setText("")
            self.ui.label_2.setVisible(False)
            
                
        self.ui.ExitButton.clicked.connect(close)    
        self.ui.btnshow.clicked.connect(show)  
        self.ui.savebtn.clicked.connect(location) 
         
        self.ui.label_2.setVisible(False)
        
        self.ui.clearbtn.clicked.connect(clear)
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QrCode()
    sys.exit(app.exec())