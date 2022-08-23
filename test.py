import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from CostomerEmail_xl import Customer_Email
from PyQt5.QtWidgets import *

class Test(QDialog):
    def __init__(self,parent):
        super(Test, self).__init__(parent)
        option_ui = './mdialog.ui'
        uic.loadUi(option_ui,self)
        self.pbtn.clicked.connect(self.customer)
        self.show()

    def customer(self):#라인텍스트 안글자가 출력
        try:
            print('일로오나')
            print(self.lineEdit.text())
            print(self.lineEdit_2.text())
        except Exception as e:
            print(e)



