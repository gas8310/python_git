import requests
from bs4 import BeautifulSoup


def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def getStockInfo(tr):
    tds = tr.findAll("td")
    rank = tds[0].text
    atag = tds[1].find("a")
    # 속성의 경우 배열명으로 접근.
    href = atag["href"]
    name = atag.text
    nowPrice = tds[2].text
    totalPrice = tds[6].text
    return{"rank":rank, "name":name, "href":href, "aTag":href[20:], "nowPrice":nowPrice, "totalPrice":totalPrice}

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    # objct로 부터 필요한 class를 가져온다.
    box_type_l = bsObj.find("div",{"class":"box_type_l"})
    type_2 = box_type_l.find("table", {"class":"type_2"})
    t_body = type_2.find("tbody")
    trs = t_body.findAll("tr")
    stockInfos = []
    for tr in trs:
        try:
            stockInfo = getStockInfo(tr)
            stockInfos.append(stockInfo)
        except Exception as e:
            print("error")
            pass
    return stockInfos

def getSise_market_sum(sosok, page):
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok={}&page={}".format(sosok, page)
    pageString = crawl(url)
    list = parse(pageString)
    return list


result = []
for page in range(1, 10 + 1):
    list = getSise_market_sum(0, page) #0:코스닥 1:코스피
    result += list
print(result)
print(len(result))

import json
file = open("./kosdak.json", "w+")
file.write(json.dumps(result))
