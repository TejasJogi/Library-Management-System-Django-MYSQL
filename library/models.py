from django.db import models

# Create your models here.


class Book(models.Model):
    catchoice = [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('novel', 'Novel'),
        ('fantasy', 'Fantasy'),
        ('thriller', 'Thriller'),
        ('romance', 'Romance'),
        ('scifi', 'Sci-Fi'),
    ]
    name = models.CharField(max_length=30)
    isbn = models.PositiveIntegerField()
    author = models.CharField(max_length=40)
    genere = models.CharField(max_length=30, choices=catchoice, default='education')

    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'
