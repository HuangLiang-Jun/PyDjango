
# 中國信託

import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
django.setup()

import urllib.request
from bs4 import BeautifulSoup #爬蟲
import re
from trips.models import Bank,Currency,ExchangeRate,ExchangeRateUpdateTime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
logging.info('shell info')
GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN')
url = 'https://www.ctbcbank.com/CTCBPortalWeb/appmanager/ebank/rb?_nfpb=true&_pageLabel=TW_RB_CM_ebank_018001&_windowLabel=T31400173241287027448950&_nffvid=%2FCTCBPortalWeb%2Fpages%2FexchangeRate%2FexchangeRate.faces&firstView=true'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = GOOGLE_CHROME_BIN
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get(url)
html = driver.page_source
driver.close()


## 以 Beautiful Soup 解析 HTML 程式碼
soup = BeautifulSoup(html, 'html.parser')
target = soup.body.find('div', class_="answer")

## 匯率更新時間
update_date: str = soup.body.find('tbody').find_all('td')[-1].string
update_date = update_date.replace('出表時間：',"")
bank: Bank = Bank.objects.filter(id = 3)[0]

# update or create
obj, create = ExchangeRateUpdateTime.objects.update_or_create(
    bank = bank,
    defaults = {'update_date': update_date})
if not create:
    obj.update_date = update_date
    obj.save()
    print('already exists:',obj.update_date)
    
## main_table
fx_list = soup.body.find('table', class_="maintable").find_all('tr')

for index in range(len(fx_list)):
    if index == 0: 
        continue

    fx = fx_list[index].find_all('td')
    currency_names = fx[0].text.split('/')
    currency_cn = currency_names[0].strip()
    currency_en = currency_names[1].strip()
    cur: Currency
    cur_list = Currency.objects.filter(currency_en = currency_en) 
    if not cur_list.exists():
        cur = Currency(currency_cn = currency_cn,
                       currency_en = currency_en)
        cur.save()
    else:
        cur = cur_list[0]

    cash_buying = fx[1].string
    cash_selling = fx[2].string
    spot_buying = fx[3].string
    spot_selling = fx[4].string
    
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