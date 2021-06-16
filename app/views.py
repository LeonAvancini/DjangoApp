from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import now

# Create your views here.
def index(request):
  context = {}
  print(now())
  return render(request, 'app/list.html', context)

def new(request):
  context = {}
  return render(request, 'app/new.html', context)