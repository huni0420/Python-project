from PyQt5 import uic
from CostomerEmail_xl import Customer_Email
from PyQt5.QtWidgets import *


class Dialog1(QDialog):
    def __init__(self, parent):  # 입력창 호출부
        super(Dialog1, self).__init__(parent)
        Email_ui = './dialog1.ui'
        uic.loadUi(Email_ui, self)
        self.xl = Customer_Email()
        self.pushButton.clicked.connect(self.EmailPush)
        self.pushButton_2.clicked.connect(self.EmailRemove)
        self.show()

    def EmailPush(self):  # 라인텍스트 안의 글자가 엑셀에서 입력
        self.email = self.lineEdit.text()
        self.xl.SaveEmail(self.email)

    def EmailRemove(self):  # 라인텍스트 안의 글자가 엑셀에서 삭제
        self.email = self.lineEdit_2.text()
        self.xl.RemoveEmail(self.email)
