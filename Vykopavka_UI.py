# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowkjdxkl.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys

from Vykopavka_fce import liniovka

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    QSize, Qt)
from PySide6 import (QtWidgets,QtGui)
from PySide6.QtWidgets import (QGridLayout, QLabel, QLineEdit,
    QMenuBar, QRadioButton, QStatusBar, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(387, 397)
        MainWindow.setMinimumSize(QSize(387, 397))
        MainWindow.setMaximumSize(QSize(387, 397))
        MainWindow.setWindowIcon(QtGui.QIcon('1406304.ico'))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.label = QLabel(self.tab1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 121, 16))
        self.lineEdit = QLineEdit(self.tab1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 30, 131, 30))
        self.lineEdit.setCursorPosition(6)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        #self.lineEdit.setText("0")
        self.label_2 = QLabel(self.tab1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 161, 16))
        self.lineEdit_2 = QLineEdit(self.tab1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 90, 131, 30))
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        #self.lineEdit_2.setText("0")
        self.label_3 = QLabel(self.tab1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 130, 171, 16))
        self.lineEdit_3 = QLineEdit(self.tab1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 150, 131, 30))
        self.lineEdit_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_3.setReadOnly(True)
        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 121, 16))
        self.lineEdit_4 = QLineEdit(self.tab_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(10, 90, 131, 30))
        self.lineEdit_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_5 = QLineEdit(self.tab_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(10, 30, 131, 30))
        self.lineEdit_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_6 = QLineEdit(self.tab_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(10, 150, 131, 30))
        self.lineEdit_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_6.setReadOnly(True)
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 70, 161, 16))
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 130, 171, 16))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.label_7 = QLabel(self.tab3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 121, 16))
        self.lineEdit_7 = QLineEdit(self.tab3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(10, 150, 131, 30))
        self.lineEdit_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_8 = QLineEdit(self.tab3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(10, 90, 131, 30))
        self.lineEdit_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_9 = QLineEdit(self.tab3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(10, 210, 131, 30))
        self.lineEdit_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_9.setReadOnly(True)
        self.label_8 = QLabel(self.tab3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 130, 161, 16))
        self.label_9 = QLabel(self.tab3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 190, 171, 16))
        self.radioButton = QRadioButton(self.tab3)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 30, 100, 20))
        self.radioButton.setChecked(True)
        self.radioButton_2 = QRadioButton(self.tab3)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(10, 60, 100, 20))
        self.label_10 = QLabel(self.tab3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(150, 100, 121, 16))
        self.tabWidget.addTab(self.tab3, "")
        self.tab4 = QWidget()
        self.tab4.setObjectName(u"tab4")
        self.label_11 = QLabel(self.tab4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 0, 191, 16))
        self.lineEdit_10 = QLineEdit(self.tab4)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(10, 20, 131, 30))
        self.lineEdit_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_11 = QLineEdit(self.tab4)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(10, 80, 131, 30))
        self.lineEdit_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_11.setReadOnly(True)
        self.label_12 = QLabel(self.tab4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 60, 181, 16))
        self.lineEdit_12 = QLineEdit(self.tab4)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(10, 140, 131, 30))
        self.lineEdit_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_12.setReadOnly(True)
        self.label_13 = QLabel(self.tab4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 120, 181, 16))
        self.label_14 = QLabel(self.tab4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 180, 271, 16))
        self.lineEdit_13 = QLineEdit(self.tab4)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(10, 200, 131, 30))
        self.lineEdit_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_13.setReadOnly(True)
        self.label_15 = QLabel(self.tab4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 240, 291, 16))
        self.lineEdit_14 = QLineEdit(self.tab4)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(10, 260, 131, 30))
        self.lineEdit_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_14.setReadOnly(True)
        self.tabWidget.addTab(self.tab4, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 387, 28))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        global statusbar_default_style
        statusbar_default_style = self.statusbar.styleSheet()

        self.retranslateUi(MainWindow)

        #Definice akcí
        #=============
        self.lineEdit.textChanged.connect(self.vypocet_liniovky)
        self.lineEdit_2.textChanged.connect(self.vypocet_liniovky)

        self.lineEdit_5.textChanged.connect(self.vypocet_optiky)
        self.lineEdit_4.textChanged.connect(self.vypocet_optiky)

        self.lineEdit_8.textChanged.connect(self.vypocet_plochy)
        self.lineEdit_7.textChanged.connect(self.vypocet_plochy)

        self.radioButton.clicked.connect(self.radButton_click)
        self.radioButton_2.clicked.connect(self.radButton_2_click)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Vykop\u00e1vka", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka v\u00fdkopu (km):", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Vzd\u00e1lenost (1 cesta, km):", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Celkov\u00e1 cena (K\u010d bez DPH):", None))
        self.lineEdit_3.setInputMask("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Liniovka", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"D\u00e9lka v\u00fdkopu (km):", None))
        self.lineEdit_6.setInputMask("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Vzd\u00e1lenost (1 cesta, km):", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Celkov\u00e1 cena (K\u010d bez DPH):", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Optika", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Plocha:", None))
        self.lineEdit_9.setInputMask("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Vzd\u00e1lenost (1 cesta, km):", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Celkov\u00e1 cena (K\u010d bez DPH):", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"&Do 1000 m2", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Nad &1 Ha", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"1000 m2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QCoreApplication.translate("MainWindow", u"Plocha", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Cestovn\u00e9 (cena za 1 km v K\u010d):", None))
        self.lineEdit_10.setInputMask("")
        self.lineEdit_10.setText(QCoreApplication.translate("MainWindow", u"5.80", None))
        self.lineEdit_11.setInputMask("")
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u"13000", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Liniovka (cena za 1 km v K\u010d):", None))
        self.lineEdit_12.setInputMask("")
        self.lineEdit_12.setText(QCoreApplication.translate("MainWindow", u"7000", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Optika (cena za 1 km v K\u010d):", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Plocha do 1000 m2 (cena za 1000 m2 v K\u010d):", None))
        self.lineEdit_13.setInputMask("")
        self.lineEdit_13.setText(QCoreApplication.translate("MainWindow", u"20000", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Plocha nad 1Ha v\u010detn\u011b (cena za 1Ha v K\u010d):", None))
        self.lineEdit_14.setInputMask("")
        self.lineEdit_14.setText(QCoreApplication.translate("MainWindow", u"40000", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), QCoreApplication.translate("MainWindow", u"Ceny", None))
    # retranslateUi

#Inicializace hlavního okna
#=============
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)

#Definice funkcí hlavního okna
    #===============
    def vypocet_liniovky(self):
        self.statusbar.setStyleSheet(statusbar_default_style)
        self.statusbar.showMessage("")
        self.lineEdit_3.setStyleSheet(self.lineEdit.styleSheet())
        sazba_linie = self.lineEdit_11.text()
        delka = self.lineEdit.text()
        doprava = self.lineEdit_10.text()
        vzdalenost = self.lineEdit_2.text()
        if delka != "" and vzdalenost != "":
            try:
                if float(delka) < 0.0 or float(vzdalenost) < 0.0:
                    self.statusbar.setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
                    self.statusbar.showMessage("Zadejte pouze kladné hodnoty!")
                    self.lineEdit_3.setStyleSheet("color: red;")
                    self.lineEdit_3.setText("Chyba!")
                else:
                    cena = liniovka(float(sazba_linie), float(delka), float(doprava), float(vzdalenost))
            except ValueError:
                self.statusbar.setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
                self.statusbar.showMessage("Zadejte pouze číselné hodnoty!")
                self.lineEdit_3.setStyleSheet("color: red;")
                self.lineEdit_3.setText("Chyba!")
            self.lineEdit_3.setText(str(round(cena,2)))
    
    def vypocet_optiky(self):
        self.statusbar.setStyleSheet(statusbar_default_style)
        self.statusbar.showMessage("")
        self.lineEdit_6.setStyleSheet(self.lineEdit.styleSheet())
        sazba_optika = self.lineEdit_12.text()
        delka = self.lineEdit_5.text()
        doprava = self.lineEdit_10.text()
        vzdalenost = self.lineEdit_4.text()
        if delka != "" and vzdalenost != "":
            try:
                if float(delka) < 0.0 or float(vzdalenost) < 0.0:
                    self.statusbar.setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
                    self.statusbar.showMessage("Zadejte pouze kladné hodnoty!")
                    self.lineEdit_6.setStyleSheet("color: red;")
                    self.lineEdit_6.setText("Chyba!")
                else:
                    cena = liniovka(float(sazba_optika), float(delka), float(doprava), float(vzdalenost))
            except ValueError:
                self.statusbar.setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
                self.statusbar.showMessage("Zadejte pouze číselné hodnoty!")
                self.lineEdit_6.setStyleSheet("color: red;")
                self.lineEdit_6.setText("Chyba!")
            self.lineEdit_6.setText(str(round(cena,2)))
    
    def vypocet_plochy(self):
        self.statusbar.setStyleSheet(statusbar_default_style)
        self.statusbar.showMessage("")
        self.lineEdit_9.setStyleSheet(self.lineEdit.styleSheet())
        plocha = self.lineEdit_8.text()
        doprava = self.lineEdit_10.text()
        vzdalenost = self.lineEdit_7.text()
        if self.radioButton.isChecked() == True:
            sazba_plocha = self.lineEdit_13.text()
        else:
            sazba_plocha = self.lineEdit_14.text()
        if plocha != "" and vzdalenost != "":
            try:
                if float(plocha) < 0.0 or float(vzdalenost) < 0.0:
                    self.statusbar.setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
                    self.statusbar.showMessage("Zadejte pouze kladné hodnoty!")
                    self.lineEdit_9.setStyleSheet("color: red;")
                    self.lineEdit_9.setText("Chyba!")
                else:
                    cena = liniovka(float(sazba_plocha), float(plocha), float(doprava), float(vzdalenost))
            except ValueError:
                self.statusbar.setStyleSheet("QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
                self.statusbar.showMessage("Zadejte pouze číselné hodnoty!")
                self.lineEdit_9.setStyleSheet("color: red;")
                self.lineEdit_9.setText("Chyba!")           
            self.lineEdit_9.setText(str(round(cena,2)))

    def radButton_click(self):
        self.label_10.setText("1000 m2")
        self.vypocet_plochy()

    def radButton_2_click(self):
        self.label_10.setText("Ha")
        self.vypocet_plochy()

app = QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon("1406304.ico"))
window = MainWindow()
window.show()
app.exec()