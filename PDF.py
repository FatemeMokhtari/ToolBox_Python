from PIL import Image
from pathlib import Path



from tkinter import filedialog , messagebox
import sys
import os
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from PySide6.QtGui import QMovie

## ==> SPLASH SCREEN
from Ui.Ui_PDF import Ui_PDFCreator



    
# SPLASH SCREEN
class PDFCreator(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_PDFCreator()
        self.ui.setupUi(self)
        
        
        
        def framevisible():
            
            self.ui.frame_2.setVisible(False)
            cleartxt()

            
            
        def cleartxt():
            self.ui.pushButton.setVisible(False)
            self.ui.label.setText("")   
            self.ui.selectfile_btn.setEnabled(True) 
            self.ui.convert_btn.setEnabled(False)
            
            self.ui.label_4.setVisible(False)
            self.ui.label_3.setVisible(False)
            self.ui.progressBar.setValue(0)
            
        def stopvideo():
            self.done.stop()
            
        self.done = QMovie(r"D:\Project\Final\ToolBox\Images\Done.gif")
        
        
        
        def selectfile():
            try:
                parent = None 
                filters = "Image (*.png *.jpg *.jpeg)" 
                title = "Select Files"
                open_at = "directory/"
                results = QFileDialog.getOpenFileNames(parent, title, open_at, filters)
                                
                if results:          
                    
                    global cretett
                    global im            
                    i=0
                    cretett =[None] * len(results[0]) 
                    im = [None] * len(results[0])         
                    for d in results[0]:
                        r = os.path.split(d)[1]
                        self.ui.label.setText(self.ui.label.text()+"<br>"+r)                            
                        print(d)
                        image= Image.open(d)
                        im[i]= image.convert('RGB')
                        cretett[i] = im[i]
                        i = i+1 
                    self.ui.selectfile_btn.setEnabled(False)
                    self.ui.convert_btn.setEnabled(True)                    
                    self.ui.pushButton.setVisible(True)
            except :
                print("error")
                    
        def sa(filepath):
            try:            
                completed = 0
                while completed < 46:
                    completed += 0.0001 
                    self.ui.progressBar.setValue(completed)
                        
                if filepath:
                    im[0].save(filepath,save_all=True, append_images=cretett[1:len(cretett)])
                
                while completed < 90:
                    completed += 0.0001 
                    self.ui.progressBar.setValue(completed)
                self.done.start()    
                self.ui.label_3.setVisible(True)            
                    
                self.ui.label_3.setMovie(self.done)
                self.ui.label_4.setVisible(True)
                QtCore.QTimer.singleShot(1000, lambda:(stopvideo))
                while completed < 100:
                    completed += 0.0001 
                    self.ui.progressBar.setValue(completed)
                                    
                QtCore.QTimer.singleShot(4500, lambda:framevisible())
            except:
                print("error")          
                       
        def convert():
            try:
                filepath, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save file", "", "files (*.pdf)")
                if filepath:
                    
                    self.ui.frame_2.setVisible(True)
                    QtCore.QTimer.singleShot(500, lambda:sa(filepath))
            except:
                print("error")
        
        
        def close():               
            sys.exit(app.exec())
        
        self.movie = QMovie(r"D:\Project\Final\ToolBox\Images\Arrow.gif")
        self.ui.label_2.setMovie(self.movie)
        self.movie.start()
        
        self.ui.ExitButton.clicked.connect(close)
        self.ui.convert_btn.setEnabled(False)
        
            
        self.ui.frame_2.setVisible(False)
        self.ui.label_4.setVisible(False)
        self.ui.pushButton.setVisible(False)  
        self.ui.pushButton.clicked.connect(cleartxt)  
        self.ui.progressBar.setValue(0)
        
        self.ui.convert_btn.setEnabled(False)
        self.ui.selectfile_btn.clicked.connect(selectfile) 
        self.ui.convert_btn.clicked.connect(convert)    
        self.show()
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFCreator()
    sys.exit(app.exec())       
        
    
