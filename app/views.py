from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.timezone import now
from django.views.generic.edit import CreateView, FormView
from .forms import AddArticleForm
from .models import Articulo

# Create your views here.
def index(request):
  context = {}
  print(now())
  return render(request, 'app/list.html', context)

def new(request):
  form = AddArticleForm()

  if request.method == 'POST':
    form = AddArticleForm(request.POST)

    # Validacion
    if form.is_valid():
      form.save()
      return redirect('/blog/')

  context = {'form': form}
  return render(request, 'app/new.html', context)

# Creacion de un formulario basado en un modelo
# class NuevoArticulo(CreateView):
#   model = Articulo
#   form_class = AddArticleForm
#   template_name = 'app/new.html'
#   success_url = '/blog/'

#   def post(self, request, *args, **kwargs):
#     form = AddArticleForm(request.POST)
#     print(request.POST)
#     if form.is_valid():
#       form.save()
#       return HttpResponseRedirect(self.success_url)
#     print(form.errors)

# Creacion de un formulario usando la vista basada en clase FormView
# class NuevoArticulo(FormView):
#   template_name = 'app/new.html'
#   form_class = AddArticleForm
#   success_url = '/blog/'

  # def post(self, request, *args, **kwargs):
  #   form = AddArticleForm(request.POST)
  #   print(request.POST)

  #   if form.is_valid():
  #     print(form)
  #     form.save()
  #     return HttpResponseRedirect(self.success_url)
  #   return render(request, self.template_name, {'form': form})
  
def NuevoArticulo(request):
  form = AddArticleForm()

  if request.method == 'POST':
    form = AddArticleForm(request.POST)

    if form.is_valid():
      form.save()
      # titulo = form.cleaned_data['titulo']
      # descripcion = form.cleaned_data['descripcion']

      # articulo = Articulo(titulo, descripcion)
      # articulo.save()

      return HttpResponseRedirect('blog')

  return render(request, 'app/new.html', {'form': form})
  