import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
import Dialog1
import Dialog2
import webbrowser
from CostomerEmail_xl import Customer_Email

form_class = uic.loadUiType('MainWindow.ui')[0]


class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.xl = Customer_Email()
        self.pushButton.clicked.connect(self.Dialog1)
        self.pushButton_2.clicked.connect(self.Costomer_List)
        self.pushButton_3.clicked.connect(self.Dialog2)
        self.pushButton_5.clicked.connect(self.makexl)
        self.pushButton_6.clicked.connect(self.Howtouse)

    def Dialog1(self):  # 버튼으로 아이디 입력창 호출
        Dialog1.Dialog1(self)


    def Costomer_List(self): # 엑셀저장파일 호출
        self.list.clear()
        rows = self.xl.Load_List()
        for row in rows:
            self.list.append(row)


    def Dialog2(self): # 쿠팡 상품검색
        try:
            Dialog2.Dialog2(self)
        except Exception as e:
            print(e)

    def makexl(self): # 이메일이 저장될 엑셀 새로만들기(엑셀 초기화)
        self.xl.CreateEmail_xl()

    def Howtouse(self):
        webbrowser.open('https://madgdbj.github.io/AI_501_4/TeamProject/send_email.html')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.show()
    sys.exit(app.exec_())