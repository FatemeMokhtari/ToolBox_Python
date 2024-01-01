import sys
from PySide6 import QtCore
from PySide6.QtWidgets import *


from Ui.Ui_AboutApp import Ui_MainWindow


class About(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        def close():              
            sys.exit(app.exec())
        
        self.ui.ExitButton.clicked.connect(close)
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = About()
    sys.exit(app.exec())