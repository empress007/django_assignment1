from django.shortcuts import render

# Create your views here.
# def home(request):
#     return render(request,"cards.html")

from . models import Card
# Create your views here.
# def home(request):
#     cards = Card.objects.all()
#     return render(request, 'cards.html', {'cards':cards})
def home(request):
    cards = Card.objects.all()
    context ={"cards":cards }
    return render(request, 'cards.html',context)

