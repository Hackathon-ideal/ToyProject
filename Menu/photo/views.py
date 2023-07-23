import random

from django.shortcuts import render
from .models import *

# Create your views here.

def main(request):
    return render(request, 'photo/home.html')

def list(request):
    return render(request, 'photo/list.html')

# def menu(request):
#     return render(request, 'photo/menu.html')

def korean(request):
    koreanfoods = random.choice(Korean.objects.all())
    # koreanfoods = Korean.objects.all()
    # ran_kfoods = random.choice(koreanfoods)
    return render(request, 'photo/menu.html', {'koreanfoods': koreanfoods})

def japanese(request):
    j_list = Japanese.objects.all()
    ran_jfood = random.choice(j_list)
    # japanesefoods = Japanese.objects.all()
    # ran_jfoods = random.choice(japanesefoods)
    return render(request, 'photo/menu.html', {'ran_jfood': ran_jfood})

def yangsig(request):
    yangsigfood = random.choice(Yangsig.objects.all())
    return render(request, 'photo/menu.html',{'yangsigfood':yangsigfood})

def fastfood(request):
    fast = random.choice(Fastfood.objects.all())
    return render(request, 'photo/menu.html',{'fast':fast})

def asian(request):
    asianfoods = random.choice(Asian.objects.all())
    # asianfoods = asian.objects.all()
    # ran_afoods = random.choice(asianfoods)
    return render(request, 'photo/menu.html', {'asianfoods': asianfoods})

def chinese(request):
    chinesefoods = random.choice(Chinese.objects.all())
    # chinesefoods = chinese.objects.all()
    # ran_cfoods = random.choice(chinesefoods)
    return render(request, 'photo/menu.html', {'chinesefoods': chinesefoods})
