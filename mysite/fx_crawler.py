
#外部腳本調用django
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
django.setup()

import urllib.request
from bs4 import BeautifulSoup #爬蟲
import re
from trips.models import FX
import logging


# 台灣銀行
page = urllib.request.urlopen('https://rate.bot.com.tw/xrt?Lang=zh-TW')
html = page.read()#.decode('utf8')
# # 以 Beautiful Soup 解析 HTML 程式碼
soup = BeautifulSoup(html, 'html.parser')
update_date: str = soup.body.find('span', class_="time").string
   
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


    # print('datetime: ', update_date)
    item = FX(currency_cn = currency_cn, 
            currency_en = currency_en, 
            cash_buying = cash_buying, 
            cash_selling = cash_selling,
            spot_buying = spot_buying,
            spot_selling = spot_selling,
            update_date = update_date
            )
    logging.info('server error')
    item.save()
        
