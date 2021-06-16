from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  context = {}
  return render(request, 'app/list.html', context)

def new(request):
  context = {}
  return render(request, 'app/new.html', context)