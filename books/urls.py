from django.conf import settings
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from books import views

urlpatterns = [
    path('books/', views.BookListView.as_view()),
    path('books/<int:pk>/', views.BookDetailView.as_view()),
    path('books/featured/', views.FeaturedBookView.as_view()),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view()),
    path('books/create/', views.BookCreateView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]