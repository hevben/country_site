from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
from .models import Country
from .models import Form
from .models import Continent

def index(request):
    data = {
        'title': 'Главная страница',
        'values': [1,2,'324','foo']
    }
    return render(request, 'mainapp/index.html', data   )

def about(request):
    return render(request, 'mainapp/about.html')

def test(request):
    countries = Country.objects.all()
    return render(request, 'mainapp/test_2.html', {'countries' : countries})