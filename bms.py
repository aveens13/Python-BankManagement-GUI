from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QStackedWidget, QWidget
import sys
import mysql.connector
import time
import random
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="***",
    database="bankmanagement"
)
my_cursor = db.cursor()
# my_cursor.execute("CREATE TABLE Details1(name VARCHAR(50)NOT NULL,username VARCHAR(12)NOT NULL,password VARCHAR(12)NOT NULL,account_num int UNSIGNED NOT NULL ,balance int UNSIGNED NOT NULL)")
# my_cursor.execute("INSERT INTO Details1(name,username,password,account_num,balance) VALUES(%s,%s,%s,%s,%s)",("Testname","Testusernam","Testpw",random.randint(1000,9999),'24000'))
# db.commit()

class Account:
    '''A very simple individual bank management system.Here you can deposit money in your account,withdraw money from
    your account and know your account information and many more.
    Best of luck!!!'''

    def __init__(self, name, account_num, balance):
        self.name = name
        self.account_num = account_num
        self.balance = balance

    def deposit(self,other):
        self.balance = self.balance+other
    def withdraw(self,other):
        self.balance = self.balance-other
    def accinterest(self):
        '''Interest rate is 6%'''
        return self.balance*0.06

    # @staticmethod
    # def register(NAME,USERNAME,PASSWORD,ACCOUNTNO,BALANCE):
    #     my_cursor.execute("INSERT INTO Details1(name,username,password,account_num,balance) VALUES(%s,%s,%s,%s,%s)",(NAME,USERNAME,PASSWORD,ACCOUNTNO,BALANCE))
    #     db.commit()


class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi('welcome.ui', self)
        self.button1.clicked.connect(self.search)
        self.button2.clicked.connect(self.register)


    def search(self):
        my_cursor.execute("SELECT * FROM Details1")
        values = my_cursor.fetchall()
        name = self.lineEdit.text()
        acc_num = self.lineEdit_2.text()
        for x in values:
            if name == x[0] and acc_num == str(x[3]):
                global a,bal
                bal = x[4]
                a = Account(name,acc_num,bal)
                # print(a.name)
                login = LoginScreen()
                widget.addWidget(login)
                widget.setCurrentIndex(widget.currentIndex()+1)
                print(widget.currentIndex())

            elif len(name) == 0 or len(acc_num)==0:
                self.log.setText("Please enter some details")

            else:
                self.log.setText("Not such name and account number")
                self.log.adjustSize()

    def register(self):
        register = RegisterScreen()
        widget.addWidget(register)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        print(widget.currentIndex())



class LoginScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("login.ui",self)
        self.button2.clicked.connect(self.back)
        self.button1.clicked.connect(self.login)

    def back(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex()+1)
        print(widget.currentIndex())
        # widget.show()


    def login(self):
        my_cursor.execute("SELECT * FROM Details1")
        values = my_cursor.fetchall()
        username= self.line1.text()
        password = self.line2.text()
        for x in values:
            if username == x[1] and password == x[2]:
                main = MainScreen()
                widget.addWidget(main)
                widget.setCurrentIndex(widget.currentIndex()+1)
                print(widget.currentIndex())
                main.name.setText(a.name)
                main.balance.setText("$"+str(a.balance))
                main.account_num.setText(str(a.account_num))
                main.interest.setText("$"+str(a.accinterest()))
            elif len(username) == 0 or len(password)==0:
                self.log.setText("Please enter some details")
            else:
                self.log.setText("Invalid Credentials")
                self.log.adjustSize()


class RegisterScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("register.ui",self)
        self.button2.clicked.connect(self.back)
        self.button1.clicked.connect(self.register)

    def register(self):
        name = self.line1.text()
        username = self.line2.text()
        password = self.line3.text()
        accno = random.randint(1000,10000)
        print(accno)
        print(password)
        if len(name) == 0 or len(password)==0 or len(username)==0:
            self.log.setText("Please Provide required details")
            self.log.adjustSize()
        else:
            self.log.setText(f"Your account number is {accno}")
            self.log.adjustSize()
            my_cursor.execute("INSERT INTO Details1(name,username,password,account_num,balance) VALUES(%s,%s,%s,%s,%s)",(name, username, password, accno, 0))
            db.commit()

    def back(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        print(widget.currentIndex())


class MainScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("mainscreen.ui",self)
        self.button1.clicked.connect(self.logout)
        self.button2.clicked.connect(self.deposit)
        self.button3.clicked.connect(self.withdraw)


    def logout(self):
        welcome =WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex()+1)
        print(widget.currentIndex())
        welcome.log.setText("Logged Out Successfully")

    def deposit(self):
        dep = int(self.line1.text())
        global up_bal
        up_bal = bal + dep
        update = "UPDATE Details1 SET balance=%s WHERE name =%s"
        val = (up_bal,a.name)
        my_cursor.execute(update,val)
        print(up_bal)
        print(bal)
        db.commit()
        self.log.setText("Deposited Successfully!")
        self.balance.setText("$"+str(up_bal))
        self.interest.setText("$"+str(up_bal*0.06))

    def withdraw(self):
        wd = int(self.line2.text())
        wd_bal = up_bal - wd
        update = "UPDATE Details1 SET balance=%s WHERE name =%s"
        val = (wd_bal,a.name)
        my_cursor.execute(update,val)
        print(wd_bal)
        db.commit()
        self.log.setText("Withdrawn Successfully!")
        self.balance.setText("$"+str(wd_bal))
        self.interest.setText("$"+str(wd_bal*0.06))



# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
print(widget.currentIndex())
widget.setFixedHeight(574)
widget.setFixedWidth(800)
widget.show()
sys.exit(app.exec_())
