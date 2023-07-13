from django.shortcuts import render
from .models import Photo

# Create your views here.

def main(request):
    return render(request, 'photo/home.html')

def list(request):
    return render(request, 'photo/list.html')