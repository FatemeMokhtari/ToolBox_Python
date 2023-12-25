import sys
import os
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QRegularExpression as QRegExp)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QRegularExpressionValidator as QRegExpValidator)
from PySide6.QtWidgets import *

import logging
import requests
from translate import Translator
import datetime
from tkinter.messagebox import showerror


from Ui.Ui_Weather import Ui_MainWindow

class Weather(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        global wheather_type 
        
        def enbtn():
            validator = QRegExpValidator(self.regexEnglish)
            self.ui.CityNametxt.setValidator(validator)
            self.ui.label.setText("City Name")
            
        def fabtn():
            validator = QRegExpValidator(self.regexPersian)
            self.ui.CityNametxt.setValidator(validator)
            self.ui.label.setText("نام شهر")
            
        def second_to_clock(seconds):
            m , s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            return h, m, s

        def time_calculate(seconds,lang):
            sunsetdate = datetime.datetime.fromtimestamp(seconds)
            now = datetime.datetime.now()
            if now >  sunsetdate:
                result = now - sunsetdate
                second = result.seconds
                h,m,s = second_to_clock(second)
                if lang == "en":                
                    self.ui.SunsetLBL_en.setText(str(h)+" hours, "+str(m)+ " minutes, "+str(s)+" seconds ago ")
                elif lang == "fa":                    
                    self.ui.SunsetLBL.setText(str(h)+"ساعت و"+str(m)+ "دقیقه و"+str(s)+" ثانیه پیش")
                
            else:
                result = sunsetdate - now
                second = result.seconds
                h,m,s = second_to_clock(second)
                
                if lang == "en":
                    self.ui.SunsetLBL_en.setText("Another "+str(h)+" hours, "+str(m)+ " minutes, "+str(s)+" seconds. ")
                
                elif lang == "fa":
                    self.ui.SunsetLBL.setText(str(h)+"ساعت و"+str(m)+ "دقیقه و"+str(s)+" ثانیه دیگر")

        def checkradiobutton():
            if self.ui.english_rdbtn.isChecked():
                self.ui.framePersian.setVisible(False)
                self.ui.frameEnglish.setVisible(True)
                return "en"
                    
            if self.ui.persian_rdbtn.isChecked():
                self.ui.frameEnglish.setVisible(False)
                self.ui.framePersian.setVisible(True)
                return "fa"   
        def search():        
            rdb_check = checkradiobutton()
                            
            city = self.ui.CityNametxt.text()
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
            app_id = "109d424b54ae460e540bad9953047757"
            try:
                result = requests.get(url.format(city, app_id)).json()
                if rdb_check == "fa":
                    translator= Translator(to_lang="Persian")
                    status = translator.translate(result['weather'][0]['main'])
                    city = translator.translate(result['name'])
                    self.ui.WeatherTypeLBL.setText(status)
                    self.ui.CityLBL.setText(city)
                    self.ui.TempLBL.setText(str(round(result['main']['temp']-273.15,2) )+'درجه سانتی گراد')
                    self.ui.WindLBL.setText(str(result['wind']['speed'])+"متر بر ثانیه")
                    time_calculate(result['sys']['sunset'],rdb_check)
                    
                elif rdb_check == "en":
                    
                    status = result['weather'][0]['main']
                    city = result['name']
                    self.ui.WeatherTypeLBL_en.setText(status)
                    self.ui.CityLBL_en.setText(city)
                    self.ui.TempLBL_en.setText(str(round(result['main']['temp']-273.15,2) )+' °C ')
                    self.ui.WindLBL_en.setText(str(result['wind']['speed'])+" m/s ")
                    time_calculate(result['sys']['sunset'],rdb_check)
            except:
                
                logging.exception("An exception was thrown!")
                showerror("خطا!","نام شهر صحیح نمی باشد")
                self.ui.CityLBL.setText("")                
                self.ui.WeatherTypeLBL.setText("")                
                self.ui.TempLBL.setText("")
                self.ui.WindLBL.setText("")
                self.ui.SunsetLBL.setText("")
        
        def close():
            sys.exit(app.exec()) 
        
        # وارد کردن حروف فارسی    
        self.regexPersian = QRegExp("^[\u0600-\u06FF\s]+$")        
        
        # en letters
        self.regexEnglish = QRegExp("^[a-z]*$")
        
        
        validator = QRegExpValidator(self.regexPersian)
        
        
        self.ui.persian_rdbtn.setChecked(True)
        self.ui.CityNametxt.setValidator(validator)
           
        self.ui.searchBtn.clicked.connect(search)
        self.ui.ExitButton.clicked.connect(close)
        
        self.ui.english_rdbtn.toggled.connect(enbtn)
        self.ui.persian_rdbtn.toggled.connect(fabtn)
        
        self.ui.frameEnglish.setVisible(False)
        self.ui.framePersian.setVisible(False)
        self.show()
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Weather()
    sys.exit(app.exec())









