from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint


class User(AbstractUser):
    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"


class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', null=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=125, default="unknown")
    publication_date = models.DateField()
    genre = models.CharField(max_length=100)
    featured = models.BooleanField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'], name='unique_book')
        ]


class Tracker(models.Model):
    WANT_TO_READ = 'Want to read'
    READING = 'Reading'
    READ = 'Read'
    STATUS_CHOICES = [
        (WANT_TO_READ, 'Want to read'),
        (READING, 'Reading'),
        (READ, 'Read'),
    ]
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=WANT_TO_READ)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trackers')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.book}  -  {self.status}"


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, related_name='notes', null=True) 
    note = models.TextField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField()
    page_number = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.note
