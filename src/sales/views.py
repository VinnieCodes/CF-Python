from django.shortcuts import render
from .forms import SalesSearchForm

# Create your views here.

def home(request):
  return render(request, 'sales/home.html')

def records(request):
  form = SalesSearchForm(request.POST or None)
  context = {
    'form': form
  }
  
  return render(request, 'sales/records.html')
