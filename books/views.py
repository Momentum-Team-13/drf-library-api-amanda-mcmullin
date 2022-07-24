from django.http import QueryDict
from books.serializers import BookSerializer, FeaturedBookSerializer, TrackerSerializer, UserSerializer, NoteSerializer
from rest_framework import generics, permissions
from .models import Book, User, Tracker, Note
from .filters import IsOwnerFilterBackend
from .permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#WORKS
# get all books,   
# BookList  # *get post*
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#WORKS
#view book details
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#***DOES NOT WORK AS IT SHOULD***needs work
#get featured books, all books by status?,
class FeaturedBookView(generics.ListAPIView):
    queryset = Book.objects.values('featured').distinct()
    serializer_class = FeaturedBookSerializer
    # ordering = ('title')

#***delete function appears but not limited to admin only - needs work
#delete book - ADMIN SHOULD BE ONLY ACCT(S) PERMITTED TO DELETE
class BookDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [permissions.IsAdminUser]

##NEEDS WORK - TEST USER CAN ADD BOOK AS ADMIN - NO BUENO**
#create books - user will see list of books and be able to add a new book
class BookCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions_class = [permissions.IsAuthenticatedOrReadOnly]


#search books(author or title)


#list of all notes
class NoteListView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['public']

    def post(self, request, *args, **kwargs):
        book_id = self.kwargs['pk']
        request.data['book'] = book_id
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        book_id = self.kwargs['pk']
        queryset = self.filter_queryset(self.get_queryset()).filter(book=book_id)
        owner_queryset = queryset.filter(user=request.user)
        public_queryset = queryset.exclude(user=request.user).filter(public=True)
        merged_queryset = owner_queryset.union(public_queryset).order_by('-created_at')
        serializer = self.get_serializ3er(merged_queryset, many=True)
        return Response(serializer.data)


#update notes
class NoteUpdateView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_class = [permissions.IsAuthenticated, IsOwner]
    lookup_url_kwarg = 'note_pk'

    def put(self, request, *args, **kwargs):
        book_id = self.kwargs('pk')
        request.data['book'] = book_id
        return self.update(request, *args, **kwargs)
