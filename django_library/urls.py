"""django_library URL Configuration

The `urlpatterns` list routes URLs to books_views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function books_views
    1. Add an import:  from my_app import books_views
    2. Add a URL to urlpatterns:  path('', books_views.home, name='home')
Class-based books_views
    1. Add an import:  from other_app.books_views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include ('books.urls')),
]