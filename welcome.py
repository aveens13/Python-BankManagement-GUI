# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import login


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.846, y2:0.818455, stop:0 rgba(85, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(310, 380, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button1.setFont(font)
        self.button1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button1.setStyleSheet("background-color:none;\n"
"\n"
"")
        self.button1.setObjectName("button1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(220, 60, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label2.setFont(font)
        self.label2.setStyleSheet("background-color:none;")
        self.label2.setObjectName("label2")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(320, 10, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label1.setFont(font)
        self.label1.setStyleSheet("background-color:none;")
        self.label1.setObjectName("label1")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 190, 221, 41))
        self.lineEdit.setStyleSheet("background-color:none;\n"
"border-radius:15px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 290, 221, 41))
        self.lineEdit_2.setStyleSheet("background-color:none;\n"
"border-radius:15px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(270, 140, 191, 51))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label3.setFont(font)
        self.label3.setStyleSheet("background-color:none;\n"
"font: 10pt \"SansSerif\";")
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(270, 240, 191, 51))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label4.setFont(font)
        self.label4.setStyleSheet("background-color:none;\n"
"font: 10pt \"SansSerif\";")
        self.label4.setObjectName("label4")
        self.log = QtWidgets.QLabel(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(290, 350, 191, 21))
        self.log.setStyleSheet("background-color:none;\n"
"color:red;")
        self.log.setObjectName("log")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button1.setText(_translate("MainWindow", "Search"))
        self.label2.setText(_translate("MainWindow", "Bank Management Software"))
        self.label1.setText(_translate("MainWindow", "Welcome"))
        self.label3.setText(_translate("MainWindow", "Full Name"))
        self.label4.setText(_translate("MainWindow", "Account Number"))
        self.log.setText(_translate("MainWindow", ""))
        self.button1.clicked.connect(self.search)

    def search(self):
        name = self.lineEdit.text()
        acc_num = self.lineEdit_2.text()
        if name == "Avinav Bhattarai" and acc_num == "2443":
            self.log.setText("Logged In successfully")
            login.run()
            widget login.Ui_MainWindow()

        else:
            self.log.setText("Invalid")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

