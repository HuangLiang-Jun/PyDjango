from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from getFx import GetFX
import logging
import json
from trips.models import Bank, Currency, ExchangeRate, ExchangeRateUpdateTime

# def hello_world(request): 
   
#     logging.info('hello info')
#     return render(request, 'hellow_world.html', {
#         'current_time': str(datetime.now())
#         })

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
        fx_objs1 = ExchangeRate.objects.filter(bank = bank1)
        fx_objs2 = ExchangeRate.objects.filter(bank = bank2)
        tw_update_date = ExchangeRateUpdateTime.objects.filter(bank = bank1)
        ctb_update_date = ExchangeRateUpdateTime.objects.filter(bank = bank2)
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
        'ct_update_date' : ctb_update_date[1].update_date,
        })


