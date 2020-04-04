from django.shortcuts import render 
from .models import LIst, Card
from .forms import CardInfoForm


# Create your views here.

def card_info_view(request, id):
    my_form = CardInfoForm()
    if request.method == 'POST':
        my_form = CardInfoForm(request.POST)
        if my_form.is_valid():
            my_form.save()
    else:
        card = Card.objects.filter(id=id)
        if len(card) > 0:
            my_form = CardInfoForm(instance=card[0])
   
    context = {
        "form": my_form
    }
    return render(request, 'caridnfor.html',context )