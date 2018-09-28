# 台灣銀行
#外部腳本調用django
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
django.setup()

import urllib.request
from bs4 import BeautifulSoup #爬蟲
import re
from trips.models import Bank,Currency,ExchangeRate,ExchangeRateUpdateTime
import logging


# 台灣銀行
logging.info('crawler info')
page = urllib.request.urlopen('https://rate.bot.com.tw/xrt?Lang=zh-TW')
html = page.read()#.decode('utf8')
# # 以 Beautiful Soup 解析 HTML 程式碼
soup = BeautifulSoup(html, 'html.parser')
update_date: str = soup.body.find('span', class_="time").string
bank: Bank = Bank.objects.filter(id = 2)[0]
obj, create = ExchangeRateUpdateTime.objects.update_or_create(
    bank = bank,
    defaults = {'update_date': update_date})
if not create:
    obj.update_date = update_date
    obj.save()
    print('already exists:',obj.update_date)  

all_tr = soup.body.find_all('tr')
for t in all_tr:
    currency_cn = ''
    currency_en = ''
    try:
        # 幣別 
        currenct_list = t.find('div', class_="visible-phone print_hide").string.strip().split(" ")#删除空白符包括'\n', '\r',  '\t',  ' ')，但是只能删除頭尾的
        currency_cn = currenct_list[0]
        currency_en = re.search('(\w+)', currenct_list[1]).group(1)
        cash_buying: str = t.find('td', attrs={"data-table": "本行現金買入"}).string
        cash_selling: str = t.find('td', attrs={"data-table": "本行現金賣出"}).string
        spot_buying: str = t.find('td', attrs={"data-table": "本行即期買入"}).string
        spot_selling: str = t.find('td', attrs={"data-table": "本行即期賣出"}).string
    except Exception:
        continue
    
    cur: Currency
    cur_list = Currency.objects.filter(currency_en = currency_en)
    if not cur_list.exists():
        cur = Currency(currency_cn = currency_cn,
                       currency_en = currency_en)
        cur.save()
    else:
        cur = cur_list[0]
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
    logging.info('log info')

        
