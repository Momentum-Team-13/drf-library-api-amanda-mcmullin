# NEEDED VIEWS
Retrieve all private notes for a book
Retrieve all public notes for a book
Create a note for a book
Edit notes




# what view needs to accompish
View Names
*method(s) needed*
- urls
---------------------------------------------------------------------------------------
from books import views

# get all books, get featured books, all books by status?, create books, search books(author or title)
BookList
*get post*
(generics.ListCreateAPIView)
- path('books/', views.BookList.as_view(), name='book_list'),

# get book details
BookDetail
*get*
(generics.RetrieveAPIView)
- path('books/<int:pk>/detail', views.BookDetails.as_view(), name='book_detail'),

# get list of books being tracked and their statuses, update tracking status
BookTracker
*get post* 
(generics.ListCreateAPIView)
- path('books/<int:pk>/tracker', views.BookTracker.as_view(), name='book_tracker'),

# update books(admin only)
BookUpdate
*put*
(generics.UpdateAPIView)
 - path('books/<int:pk>/update', views.BookUpdate.as_view(), name='book_update'),

# delete books(admin only)
BookDelete
*delete*
(generics.DestroyAPIView)
- path('books/<int:pk>/delete', views.BookDelete.as_view(), name='book_delete'),


# user list
UserList

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serialzier_class = UserSerializer




    POSSIBLE TRASH


# get book details
# BookDetail
# *get*
# (generics.RetrieveAPIView)
# - path('books/<int:pk>/detail', views.BookDetails.as_view(), name='book_detail'),

# # get list of books being tracked and their statuses, update tracking status
# BookTracker
# *get post* 
# (generics.ListCreateAPIView)
# - path('books/<int:pk>/tracker', views.BookTracker.as_view(), name='book_tracker'),

# # update books(admin only)
# BookUpdate
# *put*
# (generics.UpdateAPIView)
#  - path('books/<int:pk>/update', views.BookUpdate.as_view(), name='book_update'),

# # delete books(admin only)
# BookDelete
# *delete*
# (generics.DestroyAPIView)
# - path('books/<int:pk>/delete', views.BookDelete.as_view(), name='book_delete'),


# # user list
# #UserList

#class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# 



POSSIBLE URL TRASH
from django.conf import settings
from books import views as books_views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('books.urls')),
]


# urlpatterns = [
#     path('books/', books_views.BookList.as_view(), name='book_list'),
#     path('books/<int:pk>/detail', books_views.BookDetails.as_view(), name='book_detail'),
#     path('books/<int:pk>/tracker', books_views.BookTracker.as_view(), name='book_tracker'),
#     path('books/<int:pk>/update', books_views.BookUpdate.as_view(), name='book_update'),
#     path('books/<int:pk>/delete', books_views.BookDelete.as_view(), name='book_delete'),
#     path('api-auth/', include('rest_framework.urls')),
# ]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]





      "id": 1,
        "title": "Unmasked",
        "author": "Paul Holes",
        "publication_date": "2022-04-26",
        "genre": "Memoir",
        "featured": false
    },
    {
        "id": 3,
        "title": "Whoever Fights Monster",
        "author": "Robert Ressler",
        "publication_date": "2015-05-19",
        "genre": "Memoir",
        "featured": false
    },
    {
        "id": 2,
        "title": "I'll Be Gone In The Dark",
        "author": "Michelle McNamara",
        "publication_date": "2019-02-26",
        "genre": "Memoir",
        "featured": true
    }