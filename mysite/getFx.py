

from trips.models import FX, Bank, Currency, ExchangeRate, ExchangeRateUpdateTime
from django.http import HttpResponse
import json
import logging
from django.core import serializers

def GetFX(request):
    logging.info('getFX start')
    if request.method == "GET":
        fx_List = []
        for i in FX.objects.all():
            dic = {'cn': i.currency_cn,
                'en': i.currency_en,
                'cash_buying': i.cash_buying,
                'cash_selling': i.cash_selling,
                'spot_buying': i.spot_buying,
                'spot_selling': i.spot_selling,
                'update_date': i.update_date
                }

            fx_List.append(dic)
        return HttpResponse(
            json.dumps(fx_List), 
            content_type="application/json; charset=utf-8"
            )
    
    else:
        account = request.POST.get('account', 'NONE')
        pwd = request.POST.get('pwd', 'NONE')
        print('account: {0}, pwd: {1}'.format(account, pwd))
        return HttpResponse('use get')

# 新增銀行
def addBank(request):
    resultMsg = ''
    logging.info("add bank")

    if request.method != "POST":
        resultMsg = '參數錯誤！！！！'
    else:
        bank_code = None
        bank_name = None
        try:

            int(request.POST.get('bankCode'))
            bank_code = request.POST.get('bankCode')
            bank_name = request.POST.get('bankName')
        except:
            pass
        if bank_code == None or bank_name == None:
            resultMsg = '銀行代號及名稱必填'
        elif Bank.objects.filter(bank_code = bank_code).exists() or Bank.objects.filter(bank_name = bank_name).exists():
            resultMsg = '銀行資料已存在'
        else:
            bank = Bank(bank_code = bank_code,bank_name = bank_name)
            bank.save()
            resultMsg = '儲存成功'
        
        return HttpResponse(resultMsg)
def getBank(request):
    banks = Bank.objects.all()
    
    return HttpResponse(
            json.dumps(banks), 
            content_type="application/json; charset=utf-8"
            )