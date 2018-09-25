from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from getFx import GetFX
import logging
import json
from trips.models import FX

# def hello_world(request): 
   
#     logging.info('hello info')
#     return render(request, 'hellow_world.html', {
#         'current_time': str(datetime.now())
#         })

def fx(request):

    fx_objs = FX.objects.all()
    update_date = fx_objs[0].update_date
    print("date:",update_date)
    return render(request, 'hellow_world.html', {
        'fx_list': fx_objs,
        'update_date': update_date,
        })


