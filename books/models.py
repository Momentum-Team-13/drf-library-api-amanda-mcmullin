from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint
# from pygments import highlight
# from pygments.formatters.html import HtmlFormatter
# from pygments.lexers import get_all_lexers, get_lexer_by_name
# from pygments.styles import get_all_styles

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

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
    # language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    # style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    # highlighted = models.TextField()

    # def save(self, *args, **kwargs):
    #     """
    #     Use the `pygments` library to create a highlighted HTML
    #     representation of the code snippet.
    #     """
    #     lexer = get_lexer_by_name(self.language)
    #     options = {'title': self.title} if self.title else {}
    #     formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
    #     self.highlighted = highlight(self.code, lexer, formatter)
    #     super(Book, self).save(*args, **kwargs)

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
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='notes') 
    note = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField()
    page_number = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.note
