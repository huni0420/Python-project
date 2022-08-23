# from PyQt5 import QtWidgets
import sys
import requests
import re
from PyQt5 import uic
from bs4 import BeautifulSoup
import math
from PyQt5.QtWidgets import *
from Main_Gui import Excelseat


class Dialog2(QDialog):
    def __init__(self, parent):
        super(Dialog2, self).__init__(parent)
        product_ui = './dialog2.ui'
        uic.loadUi(product_ui, self)
        self.search = None
        self.Lpricecut = None
        self.Upricecut = None
        self.Co = Excelseat()
        self.rowIndex = 0
        self.pushButton.clicked.connect(self.Search)
        self.pushButton_2.clicked.connect(self.connect)
        self.show()

    def alret1(self):
        QMessageBox.about(self, '오류!', '이름을 확인해 주세요')
        QMessageBox.styleSheet(self, { "QPushButton{ background-color: yellow }"})

    def alret2(self):
        QMessageBox.about(self, '오류!', '가격설정을 확인해 주세요')

    def Search(self):
        try:
            self.search = self.lineEdit.text()
            if (self.search == ''):
                self.alret1()
            self.Lpricecut = int(self.lineEdit_2.text())
            self.Upricecut = int(self.lineEdit_3.text())
            if (self.Lpricecut < 0 or self.Upricecut < self.Lpricecut):
                self.alret2()
            url = "https://www.coupang.com/np/search?component=&q=" + self.search + "&channel=user"

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
            res = requests.get(url, headers=headers)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, "lxml")
            # print(res.text)

            items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
            # price = soup.find_all("li", attrs={"class":re.compile("^search-product")})

            # 상품 불러오기
            i = 0
            information = []
            for item in items:
                # 이름 값
                name = item.find("div", attrs={"class": "name"}).get_text()
                # 가격 값
                price = item.find("strong", attrs={"class": "price-value"}).get_text()
                price = int(price.replace(',', ''))
                if (price > self.Upricecut or price < self.Lpricecut):
                    continue
                # 평점 값
                rate = item.find("em", attrs={"class": "rating"})
                if rate:
                    rate = rate.get_text()
                    rate = float(rate)
                    rate = math.ceil(int(rate))
                else:
                    rate = "평점 없음"
                # 평점 수 값
                rate_cnt = item.find("span", attrs={"class": "rating-total-count"})
                if rate_cnt:
                    rate_cnt = rate_cnt.get_text()
                else:
                    rate_cnt = "평점 없음"
                link = item.find("a", attrs={"class": "search-product-link"})['href']
                link = "https://www.coupang.com" + link
                # 정렬
                information.append([name, str(price), str(rate), rate_cnt, link])
            information.sort(key=lambda x: int(x[1]))
            self.Co.create(information)
        except Exception as e:
            print(e)

    def connect(self):
        self.tableWidget.clearContents()
        rows = self.Co.loadrow()
        self.rowIndex = 0
        for row in rows:
            self.tableWidget.setItem(self.rowIndex, 0, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(self.rowIndex, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(self.rowIndex, 2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(self.rowIndex, 3, QTableWidgetItem(row[3]))
            self.tableWidget.setItem(self.rowIndex, 4, QTableWidgetItem(row[4]))
            self.tableWidget.setItem(self.rowIndex, 5, QTableWidgetItem(row[5]))

            self.rowIndex += 1
