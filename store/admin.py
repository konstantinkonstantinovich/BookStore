from django.contrib import admin
from .models import Book, Author, Comment, CartBook, Cart, Category


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating', 'price', 'image', 'publication_year', 'status', 'description', 'category']
    list_filter = ['title', 'author', 'price', 'category']
    fields = ['title', 'author', 'rating', 'price', 'image', 'publication_year', 'status', 'description', 'category']
# Register your models here.


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_filter = ['name']
    fields = ['name']


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_filter = ['name']
    fields = ['name']


@admin.register(CartBook)
class CardBookModelAdmin(admin.ModelAdmin):
    list_display = ['book', 'quantity', 'total_price', 'card']
    fields = ['book', 'quantity', 'customer', 'total_price', 'card']


@admin.register(Cart)
class CardModelAdmin(admin.ModelAdmin):
    list_display = ['owner', 'total_books', 'total_price']
    fields = ['books', 'owner', 'total_books', 'total_price']


