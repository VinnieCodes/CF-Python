from django.shortcuts import render
from .forms import SalesSearchForm

# Create your views here.

def home(request):
  return render(request, 'sales/home.html')

def records(request):
  form = SalesSearchForm(request.POST or None)
  if request.method == 'POST':
    # read book_title and chart_type
    book_title = request.POST.get('book_title')
    chart_type = request.POST.get('chart_type')
    # display in terminal - needed for debugging during development only
    print(book_title, chart_type)

  # pack up data to be sent to template in the context dictionary
  context = {
    'form': form,
  }

  return render(request, 'sales/records.html', context)
