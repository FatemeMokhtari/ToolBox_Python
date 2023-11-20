import sys
import os
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *

import logging
import requests
from translate import Translator
import datetime
from tkinter.messagebox import showerror

## ==> SPLASH SCREEN
from Ui.Ui_Weather import Ui_MainWindow

class Weather(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        global wheather_type 
        
        
        def second_to_clock(seconds):
            m , s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            return h, m, s

        def time_calculate(seconds):
            sunsetdate = datetime.datetime.fromtimestamp(seconds)
            now = datetime.datetime.now()
            if now >  sunsetdate:
                result = now - sunsetdate
                second = result.seconds
                h,m,s = second_to_clock(second)
                self.ui.SunsetLBL.setText(str(h)+"ساعت و"+str(m)+ "دقیقه و"+str(s)+" ثانیه پیش")
                
            else:
                result = sunsetdate - now
                second = result.seconds
                h,m,s = second_to_clock(second)
                self.ui.SunsetLBL.setText(str(h)+"ساعت و"+str(m)+ "دقیقه و"+str(s)+" ثانیه دیگر")

                
        
        def search():
            city = self.ui.CityNametxt.text()
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
            app_id = "109d424b54ae460e540bad9953047757"
            try:
                result = requests.get(url.format(city, app_id)).json()
                translator= Translator(to_lang="Persian")
                status = translator.translate(result['weather'][0]['main'])
                city = translator.translate(result['name'])
                self.ui.WeatherTypeLBL.setText(status)
                self.ui.CityLBL.setText(city)
                self.ui.TempLBL.setText(str(round(result['main']['temp']-273.15,2) )+'درجه سانتی گراد')
                self.ui.WindLBL.setText(str(result['wind']['speed'])+"متر بر ثانیه")
                time_calculate(result['sys']['sunset'])
            except:
                
                logging.exception("An exception was thrown!")
                showerror("خطا!","نام شهر صحیح نمی باشد")
                self.ui.CityLBL.setText("")                
                self.ui.WeatherTypeLBL.setText("")                
                self.ui.TempLBL.setText("")
                self.ui.WindLBL.setText("")
                self.ui.SunsetLBL.setText("")
        
        
        self.ui.searchBtn.clicked.connect(search)
        self.show()
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Weather()
    sys.exit(app.exec())









