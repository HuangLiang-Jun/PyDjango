

from trips.models import FX
from django.http import HttpResponse
import json
import logging

def GetFX(request):
    logging.info('getFX start')
    if request.method == "GET":
        print('GET Method..')
        fx_objs = FX.objects.all()

        fx_List = []
        for i in fx_objs:
            dic = {'cn': i.currency_cn,
                'en': i.currency_en,
                'cash_buying': i.cash_buying,
                'cash_selling': i.cash_selling,
                'spot_buying': i.spot_buying,
                'spot_selling': i.spot_selling,
                'update_date': i.update_date
                }

            # print(dic)
            fx_List.append(dic)
            # print("\n")
        
        jsonStr = json.dumps(fx_List)
        logging.info('getFX end:', jsonStr)
        return HttpResponse(jsonStr, content_type="application/json; charset=utf-8")
    else:
        print(request.header)
        account = request.POST.get('account', 'NONE')
        pwd = request.POST.get('pwd', 'NONE')
        print('account: {0}, pwd: {1}'.format(account, pwd))
        return HttpResponse('use get')