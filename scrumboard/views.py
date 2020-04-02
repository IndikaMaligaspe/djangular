from django.shortcuts import render
from .models import LIst, Card

# Create your views here.

def cardInfo(request, id):
    # id = request['id']
    print(id)
    context = {
        'cards' : Card.objects.get(id=id)
    }
    return render(request, 'caridnfor.html',context )