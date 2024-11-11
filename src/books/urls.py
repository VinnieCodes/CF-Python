from django.urls import path
from .views import BookListView, BookDetailView  # Import the BookListView

app_name = 'books'

urlpatterns = [
  path('list/', BookListView.as_view(), name='list'), 
  path('list/<pk>', BookDetailView.as_view(), name='detail'), 
]