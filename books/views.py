from django.http import QueryDict
from books.serializers import BookSerializer, FeaturedBookSerializer, UserSerializer
from rest_framework import generics, permissions
from .models import Book, User
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# get all books, get featured books, all books by status?, create books, search books(author or title)
# BookList  # *get post*
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class FeaturedBookView(generics.ListAPIView):
    queryset = Book.objects.values('featured').distinct()
    serializer_class = FeaturedBookSerializer
    # ordering = ('title')

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [permissions.IsAdminUser]

class BookCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions_class = [permissions.IsAuthenticatedOrReadOnly]