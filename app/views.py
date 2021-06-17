from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import now
from django.shortcuts import render
from .models import Articulo

# Create your views here.
def index(request):
    context = {
      'articulos' : Articulo.objects.all()
    }
    return render(request, 'app/list.html', context)


def new(request):
    context = {}
    return render(request, 'app/new.html', context)


def ArticulosList(request):

    if request.method == 'POST':
        articuloUno = Articulo()
        articuloUno.titulo = request.POST["titulo"]
        articuloUno.descripcion = request.POST["descripcion"]
        articuloUno.save()

    articulos = Articulo.objects.all()
    context = {'articulos': articulos}
    return render(request, 'app/list.html', context)
