from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtGui import QMovie
import sys
# importing all necessary libraries
from rembg import remove
from PIL import Image
from tkinter import filedialog
from PIL import Image
import os


from Ui.Ui_RemoveBG import Ui_RemoveBG

class RemoveBG(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_RemoveBG()
        self.ui.setupUi(self)
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        
        global completed 

        def upload_file():
            global filename
            f_types = [("Image files", "*.png *.jpg *.jpeg")]
            filename = filedialog.askopenfilename(filetypes=f_types)                          
            if len(filename) > 0:
                self.ui.btn_upload.setEnabled(False)
                self.ui.btn_digits_2.setEnabled(True)
                self.ui.label.setText(os.path.split(filename)[1])
                self.ui.pushButton.setVisible(True)


        def chechtxt():
            text = self.ui.txt_filename.text()
            if text:
                Convert()
        def framevisible():
            
            self.ui.frame_2.setVisible(False)
            cleartxt()

            
            
        def cleartxt():
            self.ui.pushButton.setVisible(False)
            self.ui.label.setText("")   
            self.ui.btn_upload.setEnabled(True) 
            self.ui.btn_digits_2.setEnabled(False)
            
            self.ui.label_4.setVisible(False)
            self.ui.label_3.setVisible(False)
            self.ui.progressBar.setValue(0)
            
        def stopvideo():
            self.done.stop()
            
                
        self.done = QMovie(r"D:\Project\Final\ToolBox\Images\Done.gif")
        
        def sa(filepath):
            completed = 0
            while completed < 46:
                completed += 0.0001 
                self.ui.progressBar.setValue(completed)
                    
            input_path = filename
                
            output_path = filepath
            image_input = Image.open(input_path)
            output = remove(image_input)
            output.save(output_path)
            
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
                       
       
        def Convert():
            filepath, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save file", "", "Image files (*.png)")
            
            self.ui.frame_2.setVisible(True)
            QtCore.QTimer.singleShot(500, lambda:sa(filepath))
            
        
        def close():                  
            sys.exit(app.exec())
        
        
        self.movie = QMovie(r"D:\Project\Final\ToolBox\Images\Arrow.gif")
        self.ui.label_2.setMovie(self.movie)
        self.movie.start()
        
        self.ui.ExitButton.clicked.connect(close)
        self.ui.btn_digits_2.setEnabled(False)
        
            
        self.ui.frame_2.setVisible(False)
        self.ui.label_4.setVisible(False)
        self.ui.pushButton.setVisible(False)  
        self.ui.pushButton.clicked.connect(cleartxt)  
        self.ui.progressBar.setValue(0)
        self.ui.btn_upload.clicked.connect(upload_file)
        self.ui.btn_digits_2.clicked.connect(Convert)
        self.show()
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RemoveBG()
    sys.exit(app.exec())    
    
