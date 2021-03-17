from django.contrib import admin
from .models import Book, Author, Comment


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating', 'price', 'image', 'publication_year', 'status']
    list_filter = ['title', 'author', 'price']
    fields = ['title', 'author', 'rating', 'price', 'image', 'publication_year', 'status', 'customer']
# Register your models here.


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_filter = ['name']
    fields = ['name']
