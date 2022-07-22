from books.serializers import BookSerializer
from rest_framework import generics
from .models import Book


# Create your views here.
# get all books, get featured books, all books by status?, create books, search books(author or title)
# BookList  # *get post*
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
