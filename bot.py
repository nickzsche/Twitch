import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from designer import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QShortcut, QFileDialog
from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys
import threading
from selenium.webdriver.support.ui import Select
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMessageBox
import webbrowser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import undetected_chromedriver.v2 as uc
from numpy import dtype
import pandas as pd

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        os.chdir("Data")
        self.ui.btn_TakipEttir.clicked.connect(self.TakipEtCalistir)
        self.ui.btn_IslemBasla.clicked.connect(self.TarayiciAcCalistir)
    def TakipEtCalistir(self):
        hesap = self.ui.ln_TakipEttir.text()
        dosyamiz = self.ui.ln_DosyaAdi.text()
        
        
        def TakipEt():
            if dosyamiz == "":
                veri = pd.read_csv("Users.csv")
            elif dosyamiz != "":
                veri = pd.read_csv(dosyamiz+".csv")
            df = pd.DataFrame(veri)
            sayi = 0
            userAdd = df["USER"]
            passwordAdd = df["PASS"]
            print(df.USER.isna().sum())
            print(df.PASS.isna().sum())    
            leng = len(userAdd)
            for i in range(0,leng):
                    sayi = 0
                    driver = webdriver.Chrome("chromedriver.exe")
                    driver.get(hesap)
                    login = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button/div/div")
                    login.click()
                    time.sleep(2)
                    user = driver.find_element_by_id("login-username")
                    user.send_keys(userAdd[sayi])           
                    password = driver.find_element_by_id("password-input")
                    password.send_keys(passwordAdd[sayi])
                    loginButton = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/button/div/div")
                    loginButton.click()
                    time.sleep(10)
                    FollowButton = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/div/div/div/button/div/div/div")
                    FollowButton.click()
                    time.sleep(5)
                    sayi = sayi+1
                    driver.close()
        TakipEtCalistirThread = threading.Thread(
            target=TakipEt)
        TakipEtCalistirThread.start()
    def TarayiciAcCalistir(self):
        def TarayiciAc():
            driver = webdriver.Chrome("chromedriver.exe")
            driver2 = webdriver.Chrome("chromedriver.exe")
            driver3 = webdriver.Chrome("chromedriver.exe")
            driver4 = webdriver.Chrome("chromedriver.exe")
            driver5 = webdriver.Chrome("chromedriver.exe")
            time.sleep(12000)
        TarayiciAcCalistirThread = threading.Thread(
            target=TarayiciAc)
        TarayiciAcCalistirThread.start()
            
def app():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    win = MyApp()
    win.show()
    sys.exit(app.exec_())


app()