from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Neighbor
from .models import Apartment
from django.forms import modelformset_factory

from django.template import loader
# Create your views here.


def mainpage(request , id):
   # ApartmentFormSet = modelformset_factory(Apartment , fields=('number' , 'floor_num'))
   # formset = ApartmentFormSet()
    return render(request, 'polls/index.html' , {})

def financial(request , id , type):
    return render(request, 'polls/financial.html', {})
