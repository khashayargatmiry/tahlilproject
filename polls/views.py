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
    return render(request, 'polls/index.html' , {'id' : id})

def financial(request , id , type):
    return render(request, 'polls/financial.html', {'type' : type , 'id': id})

def reservation(request , id , reserve):
    return render(request, 'polls/reservation.html' , {'hasreserve' : reserve , 'id' : id})

def neighbors(request , id):
    return render(request , 'polls/neighbors.html' , {'id': id})

def guest(request , id , guest_id):
    return render(request , 'polls/guest.html' , {'my_id' : id , 'guest_id' : guest_id})

def validation(request , id):
    return render(request , 'polls/validation.html' , {'id' : id})

def owner(request , id):
    return render(request, 'polls/owner.html', {'id': id})
