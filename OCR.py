import pytesseract
from PIL import Image
from tkinter import filedialog
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
import aspose.words as aw

from Ui.Ui_OCR import Ui_OCR

class OCR(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_OCR()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        
        pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

        def chooseFile():
            file_path = filedialog.askopenfilename(title="Open Image File", filetypes=[("Image files", "*.png *.jpg *.jpeg")])
            if file_path:
                lang = radiobtncheck()                
                convert(file_path,lang)
                
                
                
        def radiobtncheck():
            
            if self.ui.english_rdbtn.isChecked():
               
                return "english"
            elif self.ui.persian_rdbtn.isChecked():
                
                return "persian" 
            

        def convert(file_path, lang):
            try:
                image = Image.open(file_path)
                #image_rgb = cv.imread(r"D:\Project\Toolbox Program\Images\ww.jpg")
                if lang=="english":
                    text = pytesseract.image_to_string(image)                
                else:
                    pytesseract.get_languages()
                    text = pytesseract.image_to_string(image, lang='fas')
                #image = cv.imread(r"D:\Project\Toolbox Program\Images\ww.jpg", 0)
                #img_blur = cv.medianBlur(image, 1)
                #_,img_thresh = cv.threshold(img_blur, 50, 255, cv.THRESH_BINARY)
                #plt.imshow(image, cmap = 'gray')
                self.ui.textEdit.setVisible(True)
                self.ui.textEdit.setPlainText(text)
                self.ui.createtxt_btn.setVisible(True)
                
                
            except:
                print("error")
           
        def save():
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save file", "", ("*.txt;;*.doc;;*.docx"))            
            if filename:
                if _.format() == "*.docx":
                    doc = aw.Document()
                    builder = aw.DocumentBuilder(doc)
                    builder.write(self.ui.textEdit.toPlainText())                                    
                    doc.save(filename)
                else: 
                    with open(filename, "w") as f:
                        f.write(self.ui.textEdit.toPlainText())
                    
                self.ui.label.setVisible(True)
                QtCore.QTimer.singleShot(5000, lambda:self.ui.label.setVisible(False))
        
        def close():                 
            sys.exit(app.exec())
            
        self.ui.textEdit.setAlignment(Qt.AlignLeft)      
        self.ui.createtxt_btn.setVisible(False)
        self.ui.ExitButton.clicked.connect(close)        
        self.ui.textEdit.setVisible(False)        
        self.ui.chooseimage_btn.clicked.connect(chooseFile)
        self.ui.persian_rdbtn.setChecked(True)
        self.ui.createtxt_btn.clicked.connect(save)
        self.ui.label.setVisible(False)
        self.show()
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OCR()
    sys.exit(app.exec())



