from django.contrib import admin
from .models import User, Book, Tracker, Note


# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Tracker)
admin.site.register(Note)