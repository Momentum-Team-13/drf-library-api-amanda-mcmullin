from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint


class User(AbstractUser):
    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"


class Book(models.Model):
    title = models.CharField(max_length=255)
    author_first_name = models.CharField(max_length=100)
    author_last_name = models.CharField(max_length=100)
    publication_date = models.DateField()
    genre = models.CharField(max_length=100)
    featured = models.BooleanField()
    reader = models.ForeignKey("User", on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title, self.author_first_name, self.author_last_name, self.publication_date, self.genre, self.featured

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'author_first_name', 'author_last_name'],
            name='unique_book')
        ]


class Tracker(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='trackers')
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='books')


class Note(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='notes')
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='notes') 
    note = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField()
    page_number = models.CharField(max_length=100, null=True, blank=True)
