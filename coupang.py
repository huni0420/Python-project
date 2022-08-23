import math
import requests
import re
from bs4 import BeautifulSoup
# import dload

# 검색 기능
search = input("검색어를 입력하세요\n")
url = "https://www.coupang.com/np/search?component=&q="+search+"&channel=user"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
# print(res.text)

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# price = soup.find_all("li", attrs={"class":re.compile("^search-product")})

# 상품 불러오기
i = 0
information = []
for item in items:
    # 이름 값
    name = item.find("div", attrs = {"class" : "name"}).get_text()
    # 가격 값
    price = item.find("strong", attrs = {"class" : "price-value"}).get_text()
    price = int(price.replace(',',''))
    # 평점 값
    rate = item.find("em", attrs = {"class" : "rating"})
    if rate:
        rate = rate.get_text()
        rate = float(rate)
        rate = math.ceil(int(rate))
    else:
        rate = "평점 없음"
    # 평점 수 값
    rate_cnt = item.find("span", attrs = {"class" : "rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
    else:
        rate_cnt = "평점 없음"
    link = item.find("a", attrs = {"class" : "search-product-link"})['href']
    link = "https://www.coupang.com"+link
    information.append([name,price,rate,rate_cnt,link])
    # 정렬

#가격순 정렬로 출력
information.sort(key=lambda x:x[1])
    # 출력 부분
i = 0
for item in information:
    print(information[i])
    i+=1

print("끝")

#평점으로 정렬
# information.sort(key = lambda x:-x[2])
# i=0
# for item in information:
#     print(information[i])
#     i+=1
#
# print("끝")

