from django.shortcuts import render
from .models import ChaiVariety
# Create your views here.
def menu(request):
    items=ChaiVariety.objects.all()
    return render(request, "menu/menu.html",{'items':items})