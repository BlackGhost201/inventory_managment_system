from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import TuModelo

def mi_vista(request):
    # Lógica para manejar la solicitud
    contexto = {'datos': TuModelo.objects.all()}
    return render(request, 'mi_template.html', contexto)