from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render


def hello_world(request): 
   

    return render(request, 'hellow_world.html', {
        'current_time': str(datetime.now()),
        'des': '999999',
        })

# def fx(request):
#     category = Fx.objects.last()
#     return render(request, 'hellow_world.html', {
#         'current_time': str(datetime.now()),
#         'des': str('hihihi')
#         })