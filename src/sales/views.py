from django.shortcuts import render
from .forms import SalesSearchForm
from .models import Sale
from .utils import get_bookname_from_id
import pandas as pd
from .utils import get_bookname_from_id, get_chart

# Create your views here.

def home(request):
  return render(request, 'sales/home.html')

def records(request):
  form = SalesSearchForm(request.POST or None)
  sales_df = None
  chart = None
  if request.method == 'POST':
    # read book_title and chart_type
    book_title = request.POST.get('book_title')
    chart_type = request.POST.get('chart_type')

    #apply filter to extract data
    qs = Sale.objects.filter(book__name__icontains=book_title)
    if qs:      #if data found
      #convert the queryset values to pandas dataframe
      sales_df = pd.DataFrame(qs.values()) 
      # convert the ID to Name of book
      sales_df['book_id'] = sales_df['book_id'].apply(get_bookname_from_id)
      chart = get_chart(chart_type, sales_df, labels=sales_df['date_created'].values)

      sales_df = sales_df.to_html()

    # display in terminal - needed for debugging during development only
    print()
    print(book_title, chart_type)

    print ('Exploring querysets:')
    print ('Case 1: Output of Sale.objects.all()')
    qs = Sale.objects.all()
    print (qs)

    print ('Case 2: Output of Sale.objects.filter(book_name__icontains=book_title)')
    qs = Sale.objects.filter(book__name__icontains=book_title)
    print (qs)

    print ('Case 3: Output of qs.values')
    print (qs.values())

    print ('Case 4: Output of qs.values_list()')
    print (qs.values_list())

    print ('Case 5: Output of Sale.objects.get(id=1)')
    obj = Sale.objects.get(id=1)
    print (obj)

  # pack up data to be sent to template in the context dictionary
  context = {
    'form': form,
    'sales_df': sales_df,
    'chart': chart,
  }

  return render(request, 'sales/records.html', context)
