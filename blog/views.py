from django.shortcuts import render
from .models import *

# Create your views here.


def page(request):

    # getting user by the aadhar no
    dynamicdata = Person.objects.get(id=1).name
    print(dynamicdata)

    # user = User.objects.get(id=1).person
    # print(user)

#  below one when we use related name--------------------

    user1 = User.objects.get(id=1).p
    print(user1)
    #var1 = Honeybadger.objects.all()
    context = {'dynamic': dynamicdata}
    return render(request, 'page.html', context)
