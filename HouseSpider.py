#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'爬虫: 已成交二手房信息'

__author__='杨斌'

import requests, os, time, re, DBSqlite
from bs4 import BeautifulSoup
from House import House
from datetime import datetime

list_url='https://hz.lianjia.com/chengjiao/gongshu'

conn = DBSqlite.initDB()

def getListHtml(url):
    try:
        resp = requests.get(url)
        if resp.status_code == 200: 
            return resp.text
    except requests.ConnectionError:
        return None

def getList(list_html):
    soup = BeautifulSoup(list_html,'lxml')
    print(soup.title.string)
    ul = soup.find('ul', class_ = 'listContent')
    for li in ul.children :                           
        href = li.find('a',class_='img').get('href')
        yield href

def parseDetail(detailUrls):
    for url in detailUrls:
        htmltext = getListHtml(url)
        getHouseDetail(htmltext)
        time.sleep(2)

def main():
    global list_url
    global conn
    for n in range(1,101):
        detailUrls = getList(getListHtml(list_url+('/pg%d'% n)))
        parseDetail(detailUrls)   
        time.sleep(3) 
    conn.close()

def getHouseDetail(htmltext):
    global conn

    house = House()
    soup = BeautifulSoup(htmltext,'lxml')
    print(soup.title.string)
    houseinfo = soup.find('div',class_='house-title')
    houseBase = houseinfo.find('h1').string
    houseBase = re.split(r'[\s\,]',houseBase)

    housedate = houseinfo.find('span').string
    housedate = re.split(r'[\s\,]',housedate)[0]
    housedate = datetime.strptime(housedate,'%Y.%m.%d')
    house.deal_date = housedate

    house.estate_name = houseBase[0]
    house.proportion = float(houseBase[2].replace('平米',''))

    price = soup.find('div',class_='price')
    totalPrice = price.find('i').string
    house.deal_price = float(totalPrice) * 10000
    unitPrice = price.find('b').string
    house.unit_price = float(unitPrice)

    msgs = soup.find('div',class_='msg').find_all('span')
    msgs = list(msgs)
    house.sell_price = float(msgs[0].find('label').string)*10000
    house.deal_cycle = msgs[1].find('label').string   
    
    DBSqlite.insert(house,conn)
   
    pass

if __name__ == '__main__':
    main()

# filepath = os.path.join(os.path.abspath('.'),'%s.html' % 'test8')     
# with open(filepath, 'w',encoding=resp.encoding,errors='ignore') as f:
#     f.write(soup.prettify())