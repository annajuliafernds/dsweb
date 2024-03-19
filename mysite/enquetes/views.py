from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Aplicação de enquetes - DsWeb 2024.1 <br> Nome: Anna Júlia Fernandes Barbosa <br> Matrícula:20172014040018 <br> Semestre:2024.1' )