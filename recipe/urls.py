from django.urls import path
from django.http import HttpResponse
from recipe.views import home, sobre, contatos

# HTTP REQUEST: Solicitação
# HTTP RESPONSE: Resposta da solicitação

urlpatterns = [
    path('', home),
    path('contatos/', contatos),
    path('sobre/', sobre),
]