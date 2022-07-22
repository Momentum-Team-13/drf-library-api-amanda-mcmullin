from django.conf import settings
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from books import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('snippets/<int:pk>/', views.BookDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]