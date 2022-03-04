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
import sqlite3
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
        self.ui.btn_TakipEttir.clicked.connect(self.TakipEt)
    def TakipEt(self):
        hesap = self.ui.ln_TakipEttir.text()
        os.chdir("Data")
        dosyamiz = self.ui.ln_DosyaAdi.text()
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
        sayi = 0
        for i in range(0,leng):
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
    def Yazdir(self):
        print("Deneme")
def app():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    win = MyApp()
    win.show()
    sys.exit(app.exec_())


app()