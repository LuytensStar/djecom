from django.shortcuts import render
from .models import Item


# Crfeate your views here.
def item_list(request):
    context = {
        'items':Item.objects.all()
    }
    return render(request, "item_list.html", context)
