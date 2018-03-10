from django.shortcuts import render
import requests
import json

# Create your views here.


def pnr(request):
    return render(request, 'pnr/index.html')


def detail(request):
    a = requests.get('https://api.railwayapi.com/v2/route/train/'+request.POST['pnr']+'/apikey/9fk8l56ysg/')
    json_object =a.json()
    dep = json_object.route[0].schdep
    context = {
        'json_object': json_object,
        'departure': dep
    }
    return render(request, 'status/status.html', context)


def home(request):
    return render(request, 'status/homepage.html')