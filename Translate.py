import sys
import os
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from googletrans import Translator,LANGUAGES
import speech_recognition as sr
from translate import Translator as translatevoice

## ==> SPLASH SCREEN
from Ui.Ui_Translate import Ui_Translate



    
# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Translate()
        self.ui.setupUi(self)
        
        
        def change(text="type",src="English",dest="Hindi"):
            text1 = text
            src1= src
            dest1 = dest
            trans = Translator()
            trans1 = trans.translate(text,src=src1,dest=dest1)
            return trans1.text


        def data():
            
            s = self.ui.comboSrc.currentText()
            
            d = self.ui.comboDest.currentText()
            masg = self.ui.txtSrc.toPlainText()
            textget= change(text=masg , src=s , dest=d)
            self.ui.txtDest.clear()
            self.ui.txtDest.setPlainText(textget)
          
          
        
    
      
        r = sr.Recognizer()
        global counter
        counter = 2
        
        
        def langcode(test):
            switcher={
                'afrikaans':'af-AF',
                'albanian':'sq-SQ',
                'amharic':'am-AM',
                'arabic':'ar-AR',
                'armenian':'hy-Hy',
                'azerbaijani':'az-AZ',
                'basque':'', #fdhfh********************************
                'belarusian':'be-Be',
                'bengali':'bn-BN',
                'bosnian':'bs-BS',
                'bulgarian':'bg-BG',
                'catalan':'ca-CA',
                'cebuano':'', #************************************
                'chichewa':'ny-NY',
                'chinese (simplified)':'zh-ZH',
                'chinese (traditional)':'zh-Hant',
                'corsican':'co-CO',
                'croatian':'hr-HR',
                'czech':'cs-CS',
                'danish':'da-DA',
                'dutch':'nl-NL',
                'english':'en-EN',
                'esperanto':'eo-EO',
                'estonian':'et-ET',
                'filipino':'', #*************************************
                'finnish':'fi-FI',
                'french':'fr-FR',
                'frisian':'', #****************************************
                'galician':'gl-GL',
                'georgian':'ka-KA',
                'german':'de-DE',
                'greek':'el-EL',
                'gujarati':'gu-GU',
                'haitian creole':'ht-HT',
                'hausa':'ha-HA',
                'hawaiian':'',#*************************************
                'hebrew':'he=HE',                
                'hindi':'hi-HI',
                'hmong':'',#***************************************
                'hungarian':'hu-HU',
                'icelandic':'is-IS',
                'igbo':'ig-IG',
                'indonesian':'id-ID',
                'irish':'ga-GA',
                'italian':'it-IT',
                'japanese':'ja-JA',
                'javanese':'ja-JV',
                'kannada':'kn-KN',
                'kazakh':'kk-KK',
                'khmer':'km-KM',
                'korean':'ko-KO',
                'kurdish (kurmanji)':'ko-KO',
                'kyrgyz':'ky-KY',
                'lao':'lo-LO',
                'latin':'la-LA',
                'latvian':'lv-LV',
                'lithuanian':'lt-LT',
                'luxembourgish':'lb-LB',
                'macedonian':'mk-MK',
                'malagasy':'mg-MG',
                'malay':'ms-MS',
                'malayalam':'ml-ML',
                'maltese':'mt-MT',
                'maori':'mi-MI',
                'marathi':'mr-MR',
                'mongolian':'mn-MN',
                'myanmar (burmese)':'my-MY',
                'nepali':'ne-NE', 
                'norwegian':'nn-NN',
                'odia':'or-OR',
                'pashto':'ps-PS',
                'persian':'fa-FA',
                'polish':'pl-PL',
                'portuguese':'pt-PT',
                'punjabi':'pa-PA',
                'romanian':'ro-RO',
                'russian':'ru-RU',
                'samoan':'sm-SM',
                'scots gaelic':'gd-GD',
                'serbian':'sr-SR',
                'sesotho':'st-ST',
                'shona':'sn-SN',
                'sindhi':'sd-SD',
                'sinhala':'si-SI',
                'slovak':'sk-SK',
                'slovenian':'sl-SL',
                'somali':'so-SO',
                'spanish':'es-ES',
                'sundanese':'su-SU',
                'swahili':'sw-SW',
                'swedish':'sv-SV',
                'tajik':'tg-TG',
                'tamil':'ta-TA',
                'telugu':'te-TE',
                'thai':'th-TH',
                'turkish':'tr-TR',
                'ukrainian':'uk-UK',
                'urdu':'ur-UR',
                'uyghur':'ug-UG',
                'uzbek':'uz-UZ',
                'vietnamese':'vi-VI',
                'welsh':'cy-CY',
                'xhosa':'xh-XH',
                'yiddish':'yi-YI',
                'yoruba':'yo-YO',
                'zulu':'zo-ZO'
            }
            return switcher.get(test, "nothing")
                  
        def Translateclose():  
            #QApplication.quit()   
            #window.destroy()       
            sys.exit(app.exec())
            
        def get_voice():
            try:
                with sr.Microphone() as src:
                    r.adjust_for_ambient_noise(src, duration=0.2)
                    audio = r.listen(src)
                    s = self.ui.comboSrc.currentText()
                    er=langcode(s)
                    #print(er)
                    text = r.recognize_google(audio, language=er)
                    text = text.lower()
                    self.ui.txtSrc.setPlainText(text)                    
                    QtCore.QTimer.singleShot(2500, lambda: self.ui.txtSrc.textChanged.connect(data))
                    #self.ui.txtDest.
                    
                    
                    #d = self.ui.combodest.currentText()
                    #translator = translatevoice(to_lang='tr')
                    #translation = translator.translate(text)
                    #QtCore.QTimer.singleShot(2500, lambda: self.ui.txtdest.setPlainText(translation))
                    
        
                    #show_text(translation)
                    

            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                
            except sr.UnknownValueError:
                self.ui.txtDest.setPlainText("درست تشخیص داده نشد")
        
        def timertxt():
            QtCore.QTimer.singleShot(2500,data)  
               
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)        
        list_text = list(LANGUAGES.values())        
        
        #self.ui.combosrc.setHidden(True)
        self.ui.comboSrc.addItems(list_text)
        self.ui.comboSrc.setCurrentText("english")
        
        self.ui.comboDest.addItems(list_text)
        self.ui.comboDest.setCurrentText("persian")
        
        
            
        self.ui.txtSrc.textChanged.connect(timertxt)     

        self.ui.comboDest.editTextChanged.connect(data)
        
        self.ui.txtDest.setReadOnly(True);
        
        self.ui.MicButton.clicked.connect(get_voice)       
        
        
        #self.ui.btntext.setText("Translate")
        #self.ui.btntext.clicked.connect(get_voice)
        
        self.ui.ExitButton.clicked.connect(Translateclose)
        self.show()
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    
    sys.exit(app.exec())
