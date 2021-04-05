from django.contrib import admin
from .models import Book, Author,Category, Order, OrderItem, BookInstance


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


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    fields = ['phone', 'first_name', 'status', 'email']
    list_display = ['phone', 'first_name', 'status', 'email']


@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    fields = [ 'order', 'book', 'quantity']
    list_display = ['order', 'total_price', 'book', 'quantity']


@admin.register(BookInstance)
class BookInstanceModelAdmin(admin.ModelAdmin):
    list_display = ["book", "book_status", "item_of_order"]
    list_filter = ["book", "book_status", "item_of_order"]

