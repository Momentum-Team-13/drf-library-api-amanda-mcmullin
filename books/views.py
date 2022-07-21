from django.shortcuts import render, redirect
from .models import Book, Tracker

# Create your views here.
def BookListView(request):
    books = Book.objects.all()
    return ({"books": books})