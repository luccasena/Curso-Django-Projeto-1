from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,'recipe/pages/home.html',
                  context={'name': 'Lucca'})

def contatos(request):
    return HttpResponse('Contato')

def sobre(request):
    return HttpResponse('Sobre')