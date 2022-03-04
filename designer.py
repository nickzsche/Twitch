# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(500, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        MainWindow.setStyleSheet("background-color: #9146FF")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 501, 491))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 211, 31))
        self.label_2.setStyleSheet("font-size: 32px;\n"
"color: white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(150, 40, 191, 31))
        self.label_3.setStyleSheet("font-size: 32px;\n"
"color: white;")
        self.label_3.setObjectName("label_3")
        self.btn_IslemBasla = QtWidgets.QPushButton(self.tab_3)
        self.btn_IslemBasla.setGeometry(QtCore.QRect(150, 240, 171, 31))
        self.btn_IslemBasla.setStyleSheet("border-radius: 12px;\n"
"background-color: white;")
        self.btn_IslemBasla.setObjectName("btn_IslemBasla")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(270, 120, 211, 31))
        self.label_10.setStyleSheet("font-size: 32px;\n"
"color: white;")
        self.label_10.setObjectName("label_10")
        self.ln_YorumSuresi = QtWidgets.QLineEdit(self.tab_3)
        self.ln_YorumSuresi.setGeometry(QtCore.QRect(260, 160, 211, 20))
        self.ln_YorumSuresi.setObjectName("ln_YorumSuresi")
        self.ln_YorumAdedi = QtWidgets.QComboBox(self.tab_3)
        self.ln_YorumAdedi.setGeometry(QtCore.QRect(50, 160, 191, 22))
        self.ln_YorumAdedi.setObjectName("ln_YorumAdedi")
        self.ln_YorumAdedi.addItem("")
        self.ln_YorumAdedi.addItem("")
        self.ln_YorumAdedi.addItem("")
        self.ln_YorumAdedi.addItem("")
        self.ln_YorumAdedi.addItem("")
        self.ln_YorumAdedi.addItem("")
        self.ln_YorumAdedi.addItem("")
        self.ln_YorumAdedi.addItem("")
        self.ln_YorumAdedi.addItem("")
        self.ln_YorumAdedi.addItem("")
        self.ln_YorumAdedi.addItem("")
        self.ln_YorumAdedi.addItem("")
        self.ln_YorumAdedi.addItem("")
        self.ln_YorumAdedi.addItem("")
        self.line_YorumGrubu = QtWidgets.QLineEdit(self.tab_3)
        self.line_YorumGrubu.setGeometry(QtCore.QRect(140, 80, 211, 20))
        self.line_YorumGrubu.setObjectName("line_YorumGrubu")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_3)
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 300, 401, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btn_TakipEttir = QtWidgets.QPushButton(self.tab)
        self.btn_TakipEttir.setGeometry(QtCore.QRect(150, 290, 171, 31))
        self.btn_TakipEttir.setStyleSheet("border-radius: 12px;\n"
"background-color: white;")
        self.btn_TakipEttir.setObjectName("btn_TakipEttir")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(50, 110, 411, 31))
        self.label_5.setStyleSheet("font-size: 32px;\n"
"color: white;")
        self.label_5.setObjectName("label_5")
        self.ln_TakipEttir = QtWidgets.QLineEdit(self.tab)
        self.ln_TakipEttir.setGeometry(QtCore.QRect(140, 180, 211, 20))
        self.ln_TakipEttir.setObjectName("ln_TakipEttir")
        self.ln_DosyaAdi = QtWidgets.QLineEdit(self.tab)
        self.ln_DosyaAdi.setGeometry(QtCore.QRect(140, 240, 211, 20))
        self.ln_DosyaAdi.setObjectName("ln_DosyaAdi")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(140, 220, 47, 13))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(140, 160, 61, 16))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(90, 100, 411, 31))
        self.label_7.setStyleSheet("font-size: 32px;\n"
"color: white;")
        self.label_7.setObjectName("label_7")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_4.setGeometry(QtCore.QRect(60, 150, 371, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 280, 171, 31))
        self.pushButton_3.setStyleSheet("border-radius: 12px;\n"
"background-color: white;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 240, 271, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(200, 190, 211, 31))
        self.label_9.setStyleSheet("font-size: 32px;\n"
"color: white;")
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Twitch Bot"))
        self.label_2.setText(_translate("MainWindow", "Yorum Adedi"))
        self.label_3.setText(_translate("MainWindow", "Yorum Grubu"))
        self.btn_IslemBasla.setText(_translate("MainWindow", "İşleme Başla"))
        self.label_10.setText(_translate("MainWindow", "Yorum Süresi"))
        self.ln_YorumAdedi.setItemText(0, _translate("MainWindow", "1"))
        self.ln_YorumAdedi.setItemText(1, _translate("MainWindow", "2"))
        self.ln_YorumAdedi.setItemText(2, _translate("MainWindow", "3"))
        self.ln_YorumAdedi.setItemText(3, _translate("MainWindow", "4"))
        self.ln_YorumAdedi.setItemText(4, _translate("MainWindow", "5"))
        self.ln_YorumAdedi.setItemText(5, _translate("MainWindow", "10"))
        self.ln_YorumAdedi.setItemText(6, _translate("MainWindow", "15"))
        self.ln_YorumAdedi.setItemText(7, _translate("MainWindow", "20"))
        self.ln_YorumAdedi.setItemText(8, _translate("MainWindow", "25"))
        self.ln_YorumAdedi.setItemText(9, _translate("MainWindow", "30"))
        self.ln_YorumAdedi.setItemText(10, _translate("MainWindow", "35"))
        self.ln_YorumAdedi.setItemText(11, _translate("MainWindow", "40"))
        self.ln_YorumAdedi.setItemText(12, _translate("MainWindow", "45"))
        self.ln_YorumAdedi.setItemText(13, _translate("MainWindow", "50"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Yorum grubuna yorumların olduğu text dosyasının adını yazmak gerekiyor. Ardından yorum adedi seçilecek. Userların olduğu dosya içinden userları otomatik yükleyecek. Yorum süresini de seçebilecek kullanıcı. Ardından işleme başla denilecek."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Yorum Attır"))
        self.btn_TakipEttir.setText(_translate("MainWindow", "İşleme Başla"))
        self.label_5.setText(_translate("MainWindow", "Takip Ettirelecek Kullanıcılar"))
        self.label.setText(_translate("MainWindow", "Dosya Adı"))
        self.label_4.setText(_translate("MainWindow", "Kullanıcı Adı"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Takip Ettir"))
        self.label_7.setText(_translate("MainWindow", "İzletilecek Kullanıcılar"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "1 Saat"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "2 Saat"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "3 Saat"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Tüm Yayın"))
        self.pushButton_3.setText(_translate("MainWindow", "İşleme Başla"))
        self.label_9.setText(_translate("MainWindow", "Adet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "İzlet"))
