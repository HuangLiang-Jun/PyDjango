

# html_doc = """
# <html><head><title>Hello World</title></head>
# <body><h2>Test Header</h2>
# <p>This is a test.</p>
# <a id="link1" href="/my_link1">Link 1</a>
# <a id="link2" href="/my_link2">Link 2</a>
# <p>Hello, <b class="boldtext">Bold Text</b></p>
# </body></html>
# """



import urllib.request
from bs4 import BeautifulSoup #爬蟲
import re
import json #JSON
from trips.models import FX
from django.http import HttpResponse
# import mysql.connector



# mydb = mysql.connector.connect(
#     host = 'localhost',
#     user = 'host',
#     passwd = '123456',
#     database = 'testdb'
# )
# print('mydb = {0}',mydb)

# cursor = mydb.cursor()

def start_crawler(request):

    # 台灣銀行
    page = urllib.request.urlopen('https://rate.bot.com.tw/xrt?Lang=zh-TW')
    html = page.read()#.decode('utf8')
    # # 以 Beautiful Soup 解析 HTML 程式碼
    soup = BeautifulSoup(html, 'html.parser')
    update_date: str = soup.body.find('span', class_="time").string
   
    all_tr = soup.body.find_all('tr')
    # print(all_tr)
    # fx_list = []
    for t in all_tr:
        # print('******************************')
        # print(t)
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
        # print('gogogo')
        # print('datetime: ', update_date)
        item = FX(currency_cn = currency_cn, 
                currency_en = currency_en, 
                cash_buying = cash_buying, 
                cash_selling = cash_selling,
                spot_buying = spot_buying,
                spot_selling = spot_selling,
                update_date = update_date
                )
        print('save')
        item.save()
        print('save2')
    return HttpResponse('OK')

    # item = {'currency_cn': currency_cn,
    #         'currency_en': currency_en,
    #         'cash_buying': cash_buying,
    #         'cash_selling': cash_selling,
    #         'spot_buying': spot_buying,
    #         'spot_selling': spot_selling}
    
    # sql = """
    #       INSERT INTO
    #       testdb.FX
    #       (currency_cn, currency_en, cash_buying, cash_selling, spot_buying, spot_selling) 
    #       VALUES ('%s', '%s', '%s', '%s', '%s', '%s')
    #       """ % (currency_cn, currency_en, cash_buying, cash_selling, spot_buying, spot_selling)
    # sql = """
    #       INSERT INTO
    #       testdb.FX
    #       (currency_cn, currency_en, cash_buying, cash_selling, spot_buying, spot_selling) 
    #       VALUES ('%s', '%s', '%s', '%s', '%s', '%s')
    #       ON DUPLICATE KEY UPDATE cash_buying = cash_buying, cash_selling = cash_selling, spot_buying = spot_buying, spot_selling = spot_selling
    #       """ % (currency_cn, currency_en, cash_buying, cash_selling, spot_buying, spot_selling)
    
    # val = (currency_cn, currency_en, cash_buying, cash_selling, spot_buying, spot_selling)
    # print('val: ', val)
    # cursor.execute(sql)
    # mydb.commit()
   
    #fx_list.append(item)    
    # print('幣別:{0}-{1}'.format(currency_cn, currency_en))
    # print('現金買入: {0}, 現金賣出: {1}'.format(cash_buying, cash_selling))
    # print('即期買入: {0}, 即期賣出: {1}'.format(spot_buying, spot_selling))
    # print('******************************\n')

# jsonStr = json.dumps(fx_list)
#print(jsonStr)

# d = json.loads(jsonStr)
# print(d)



# sql = """CREATE TABLE FX (
#          id INT NOT NULL,
#          PRIMARY KEY (id),
#          currency_cn  CHAR(20) NOT NULL,
#          currency_en  CHAR(20),
#          cash_buying CHAR(20),
#          cash_selling CHAR(20),
#          spot_buying CHAR(20),
#          spot_selling CHAR(20))"""

# cursor.execute(sql)
