import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
django.setup()


import urllib.request
from bs4 import BeautifulSoup #爬蟲
import re
from trips.models import Bank, Currency, ExchangeRate, ExchangeRateUpdateTime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
logging.info('shell info')

import time
from datetime import datetime, timedelta, timezone



url = 'https://ibank.tcbbank.com.tw/PIB/cb5/cb501005/CB501005_01.faces'
bank: Bank = Bank.objects.filter(id = 4)[0]
page = urllib.request.urlopen(url)
html = page.read()#s.decode('utf8')
soup = BeautifulSoup(html, 'html.parser')
# update or create
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
dt = utc_dt.astimezone(timezone(timedelta(hours=8))).strftime('%Y/%m/%d %H:%M')

obj, create = ExchangeRateUpdateTime.objects.update_or_create(
    bank = bank,
    defaults = {'update_date': dt})

if not create:
    obj.update_date = dt
    obj.save()



### FX
trList = soup.body.find('table', class_="tb2 m10").find_all('tr')
for i in range(len(trList)):
    if i == 0 : continue
    tdList = trList[i].find_all('td')
    currency_cn = tdList[0].text.split(' ')[0].strip()
    currency_en = tdList[0].text.split(' ')[1].strip()
    cur_list = Currency.objects.filter(currency_en = currency_en) 
    if not cur_list.exists():
        cur = Currency(currency_cn = currency_cn,
                       currency_en = currency_en)
        cur.save()
    else:
        
        cur = cur_list[0]
    
 
    cash_buying = tdList[1].string if float(tdList[1].string) != 0  else '-'
    cash_selling = tdList[2].string if float(tdList[2].string) != 0  else '-'
    spot_buying = tdList[3].string if float(tdList[3].string) != 0  else '-'
    spot_selling = tdList[4].string if float(tdList[4].string) != 0  else '-'
    # 檢查此銀行跟貨幣的匯率是否存在
    obj, create = ExchangeRate.objects.update_or_create(
    bank = bank,
    currency = cur,
    defaults = {'cash_buying': cash_buying,
                'cash_selling': cash_selling,
                'spot_buying': spot_buying,
                'spot_selling': spot_selling})

    if not create:
        obj.cash_buying = cash_buying
        obj.cash_selling = cash_selling
        obj.spot_buying = spot_buying
        obj.spot_selling =spot_selling
        obj.save()