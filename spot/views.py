from django.shortcuts import render
from datetime import datetime, timedelta
import requests
# Create your views here.


def index(request):
    today = datetime.today()
    ddby = today - timedelta(days=3)
    yesterday = today - timedelta(days=1)
    dby = today - timedelta(days=2)
    today = today.strftime('%d-%m-20%y')
    yesterday = yesterday.strftime('%d-%m-20%y')
    dby = dby.strftime('%d-%m-20%y')
    ddby = ddby.strftime('%d-%m-20%y')
    context={
        "dby": dby,
        "yesterday": yesterday,
        "today": today,
        "ddby": ddby
    }
    return render(request, 'spot/index.html',context)

def view(request):
    r=requests.get("https://api.railwayapi.com/v2/live/train/"+request.POST['trainno']+"/date/"+request.POST['date']+"/apikey/9fk8l56ysg/")
    json_object = r.json()
    context={
        "json_object": json_object
    }
    return render(request, 'spot/view.html',context)