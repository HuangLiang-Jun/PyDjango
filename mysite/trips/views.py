from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from getFx import GetFX
import logging
import json
from trips.models import Bank, Currency, ExchangeRate, ExchangeRateUpdateTime

logging.info(__name__)

def getFxOfBank(request):
    
    if request.method == "GET":
        bankObjs = Bank.objects.filter(id=request.GET.get('bank_id'))
        if len(bankObjs) != 0:
            fxObjs = ExchangeRate.objects.filter(bank_id=bankObjs[0].id)
            refreshTime = ExchangeRateUpdateTime.objects.filter(bank_id=bankObjs[0].id)
            tmp_list = []
            for fx in fxObjs:
                dic = {'cn': fx.currency.currency_cn,
                    'en': fx.currency.currency_en,
                    'cash_buying': fx.cash_buying,
                    'cash_selling': fx.cash_selling,
                    'spot_buying': fx.spot_buying,
                    'spot_selling': fx.spot_selling
                    }
                
                tmp_list.append(dic)
            test = json.dumps({'fx': tmp_list, 'updateTime': refreshTime[0].update_date})
    return HttpResponse(test, content_type="application/json")

def bankFx(request):
    fx_dict = []
        
    bankObjs = Bank.objects.all()
    if len(bankObjs) == 0:
        fx_dict = {'message': 'No data.'}
    else:

        for i in bankObjs:
            rateObjs = ExchangeRate.objects.filter(bank_id=i.id)
            if len(rateObjs) == 0:
                print('zero data',i.id)
                continue
                
            tmp_list = []
            for fx in rateObjs:
                dic = {'cn': fx.currency.currency_cn,
                       'en': fx.currency.currency_en,
                       'cash_buying': fx.cash_buying,
                       'cash_selling': fx.cash_selling,
                       'spot_buying': fx.spot_buying,
                       'spot_selling': fx.spot_selling
                       }
                
                tmp_list.append(dic)
                
            code = i.bank_code
            try:
                update_at = ExchangeRateUpdateTime.objects.get(bank_id=i.id).update_date
            except :
                update_at = '---'

            fx_dict.append({'bank_id': i.id,
                            'bank_name' : i.bank_name, 
                            'bank_code': code,
                            'update_at': update_at,
                            'data': tmp_list
                            })
    # print(fx_dict) 
    return render(request, 'bank_fx.html', {
        'fx': fx_dict
    })




def fx(request):
    bank1 = None
    bank2 = None
    fx_objs1 = None
    fx_objs2 = None
    tw_update_date = None
    ctb_update_date = None
    try:
        bank1 = Bank.objects.filter(id = 2)[0] #台銀
        bank2 = Bank.objects.filter(id = 3)[0] #中信
        bank3 = Bank.objects.filter(id = 4)[0] #台中商銀
        fx_objs1 = ExchangeRate.objects.filter(bank = bank1)
        fx_objs2 = ExchangeRate.objects.filter(bank = bank2)
        tw_update_date = ExchangeRateUpdateTime.objects.filter(bank = bank1)
        ctb_update_date = ExchangeRateUpdateTime.objects.filter(bank = bank2)
        print(ctb_update_date[0].update_date)
    
    except:
        
        bank1 = []
        bank2 = []
        fx_objs1 = []
        fx_objs2 = []
        tw_update_date = ['no']
        ctb_update_date = ['no']
    
    return render(request, 'hellow_world.html', {
        'tw_bank' : fx_objs1,
        'ctbc' : fx_objs2,
        'tw_update_date' : tw_update_date[0].update_date,
        'ct_update_date' : ctb_update_date[0].update_date,
        })


