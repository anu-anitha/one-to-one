from django.shortcuts import render
from .models import Place

# Create your views here.

def page(request):
    dynamicdata = Place.objects.all()
    #var1 = Honeybadger.objects.all()
    context={'dynamic': dynamicdata}
    return render(request, 'page.html',context)

