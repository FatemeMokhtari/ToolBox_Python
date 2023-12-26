from PIL import Image
from pathlib import Path

from docx2pdf import convert as cvv

import sys
import os
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from PySide6.QtGui import QMovie


from Ui.Ui_PDF import Ui_PDFCreator


class PDFCreator(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_PDFCreator()
        self.ui.setupUi(self)
        
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        
        def framevisible():
            
            self.ui.frame_2.setVisible(False)
            cleartxt()
            

            
            
        def cleartxt():
            self.ui.pushButton.setVisible(False)
            self.ui.label.setText("")   
            self.ui.selectfile_btn.setEnabled(True)
            self.ui.selectTextfilebtn.setEnabled(True) 
            self.ui.convert_btn.setEnabled(False)
            
            self.ui.label_4.setVisible(False)
            self.ui.label_3.setVisible(False)
            self.ui.progressBar.setValue(0)
            self.ui.Image_rdbtn.setEnabled(True)
            self.ui.Text_rdbtn.setEnabled(True)
            
        def stopvideo():
            self.done.stop()
            
        self.done = QMovie(r"D:\Project\Final\ToolBox\Images\Done.gif")
        
        
        
        def choosefile():
            try:
                from tkinter import filedialog                 
                global textfilepath
                file_path = filedialog.askopenfilename(filetypes=[("Text files","*.txt *.doc *.docx")])                
                if file_path:
                    self.ui.pushButton.setVisible(True)
                    self.ui.Image_rdbtn.setEnabled(False)
                    r = os.path.split(file_path)[1]                    
                    self.ui.label.setText(r)
                    self.typeRadioButton = "text"
                    textfilepath = file_path                    
                self.ui.selectTextfilebtn.setEnabled(False)
                self.ui.convert_btn.setEnabled(True)                    
                self.ui.pushButton.setVisible(True)
            except Exception as e:
                print("error " + e)             
        
        
        self.typeRadioButton = ""
        ############################################################
        # SELECT IMAGE TO PDF
        ############################################################
        def select_Image_file():
            try:
                parent = None 
                filters = "Image (*.png *.jpg *.jpeg)" 
                title = "Select Files"
                open_at = "directory/"
                results = QFileDialog.getOpenFileNames(parent, title, open_at, filters)
                global images                              
                if results:                     
                    global cretett
                    global im  
                    self.ui.Text_rdbtn.setEnabled(False)          
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
                    self.typeRadioButton = "image"
            except :
                print("error")
                
        
        
        
        #######################################################
        # CONVERT IMAGE TO PDF
        #######################################################                  
        def convert_image_to_pdf(filepath):
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
            except Exception as e:
                print(e)        
                
                
                
        def convert_text_to_pdf(filepath):  
            try:            
                completed = 0
                while completed < 46:
                    completed += 0.0001 
                    self.ui.progressBar.setValue(completed)
                        
                if filepath:
                    extension = str(textfilepath.split(".")[-1])
                    if extension == "doc" or extension == "txt":   
                        print("start")
                        
                        import os
                        import pdfkit
                        options = {
                            'encoding': "UTF-8",
                            'quiet':'',
                            'page-size':'A4',
                            'dpi':300,
                            'disable-smart-shrinking':'',
                        }
                        path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
                        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)                        
                        with open(textfilepath, encoding="UTF-8") as file:
                            with open("text.html", "w",encoding="UTF-8") as output:
                                file_content = file.read()
                                file_content = file_content.replace("\n", "<br>")
                                output.write(file_content)
                            pdfkit.from_file("text.html", filepath,configuration=config,options=options)
                            
                        print("end")
                        
                    elif extension == "docx":    
                        cvv(textfilepath,filepath)
                
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
            except Exception as e:
                print(e) 
                
                     
                  
                       
        def convert_btn():
            try:                
                filepath, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save file", "", "files (*.pdf)")
                if filepath:                                           
                    self.ui.frame_2.setVisible(True)                    
                    if self.typeRadioButton == "text":
                        QtCore.QTimer.singleShot(500, lambda:convert_text_to_pdf(filepath))
                     
                    elif self.typeRadioButton == "image":                    
                        QtCore.QTimer.singleShot(500, lambda:convert_image_to_pdf(filepath))
                        
            except Exception as e:
                print(e)
                
                
        
        def TextVisible():
            self.ui.selectTextfilebtn.setVisible(True)
            self.ui.selectfile_btn.setVisible(False)
            
        def ImageVisible():
            self.ui.selectTextfilebtn.setVisible(False)
            self.ui.selectfile_btn.setVisible(True)
            
            
        def close():               
            sys.exit(app.exec())
        
        self.movie = QMovie(r"D:\Project\Final\ToolBox\Images\Arrow.gif")
        self.ui.label_2.setMovie(self.movie)
        self.movie.start()
        
        self.ui.ExitButton.clicked.connect(close)
        self.ui.convert_btn.setEnabled(False)
        
        ##   LOAD RADIOBUTTONS
        self.ui.Image_rdbtn.setChecked(True)
        self.ui.selectTextfilebtn.setVisible(False)
        self.ui.selectfile_btn.setVisible(True)
        self.ui.Text_rdbtn.clicked.connect(TextVisible)
        self.ui.Image_rdbtn.clicked.connect(ImageVisible)
        
        self.ui.frame_2.setVisible(False)
        self.ui.label_4.setVisible(False)
        self.ui.pushButton.setVisible(False)  
        self.ui.pushButton.clicked.connect(cleartxt)  
        self.ui.progressBar.setValue(0)
        
        self.ui.convert_btn.setEnabled(False)
        self.ui.selectfile_btn.clicked.connect(select_Image_file) 
        self.ui.selectTextfilebtn.clicked.connect(choosefile) 
        self.ui.convert_btn.clicked.connect(convert_btn)    
        self.show()
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFCreator()
    sys.exit(app.exec())       
        
    
