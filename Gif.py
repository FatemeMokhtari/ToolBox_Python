from moviepy.editor import VideoFileClip

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
from Ui.Ui_Gif import Ui_RemoveBG



    
# SPLASH SCREEN
class VideoToGif(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_RemoveBG()
        self.ui.setupUi(self)
        
        def selectfile():
            global file_path
            file_path = filedialog.askopenfilename(title="Open Video File", filetypes=[("Video files", "*mp4")])
                                          
            if len(file_path) > 0:
                self.ui.selectfile_btn.setEnabled(False)
                self.ui.convert_btn.setEnabled(True)
                self.ui.label.setText(os.path.split(file_path)[1])
                self.ui.pushButton.setVisible(True)
            #if file_path:                
               # videoClip = VideoFileClip(file_path)

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
        
        def sa(filepath):
            
            videoClip = VideoFileClip(file_path)
            
            completed = 0
            while completed < 46:
                completed += 0.0001 
                self.ui.progressBar.setValue(completed)
                    
            if filepath:
                videoClip.write_gif(filepath)
            
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
                       
                       
                           
        def convert():
            
            filepathgif, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save file", "", "Image files (*.gif)")
            self.ui.frame_2.setVisible(True)
            QtCore.QTimer.singleShot(500, lambda:sa(filepathgif))
            
        
        def close():  
            #QApplication.quit()   
            #window.destroy()       
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
        
        
        
        self.ui.selectfile_btn.clicked.connect(selectfile) 
        self.ui.convert_btn.clicked.connect(convert)    
        self.show()
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoToGif()
    sys.exit(app.exec())       
        
    