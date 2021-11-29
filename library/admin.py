from django.contrib import admin
from .models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)
