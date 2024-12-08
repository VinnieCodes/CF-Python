# you need to connect parameter from books model
from books.models import Book

def get_bookname_from_id(val):
  # this ID is used to retrieve the name from the record
  bookname = Book.objects.get(id=val)
  # and the name is returned back
  return bookname