import sys

from PySide6 import QtCore
from PySide6.QtCore import (QRegularExpression as QRegExp)
from PySide6.QtGui import (QRegularExpressionValidator as QRegExpValidator)
from PySide6.QtWidgets import *

from num2words import num2words

from Ui.Ui_Num_To_Words import Ui_MainWindow

# Num to Word
class NumToWords(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        
        def numberclose():        
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
        
        self.ui.label.setWordWrap(True)
       
        regex = QRegExp("^[ 0-9]+$")
        validator = QRegExpValidator(regex, self.ui.lineEdit)        
        self.ui.lineEdit.setValidator(validator)
        self.ui.lineEdit.setMaxLength(18)
        
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NumToWords()
    sys.exit(app.exec())
