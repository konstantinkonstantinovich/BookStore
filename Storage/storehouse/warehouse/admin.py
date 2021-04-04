from django.contrib import admin
from .models import Book, Author,Category, Order, OrderItem, BookInstance


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'rating', 'price', 'image', 'publication_year', 'status', 'description', 'category']
    list_filter = ['title', 'author', 'price', 'category']
    fields = ['id','title', 'author', 'rating', 'price', 'image', 'publication_year', 'status', 'description', 'category']
# Register your models here.


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_filter = ['id','name']
    fields = ['id','name']


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_filter = ['name']
    fields = ['name']


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    fields = ['id','phone', 'first_name', 'status', 'email']
    list_display = ['id','phone', 'first_name', 'status', 'email']


@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    fields = ['id', 'order', 'book', 'quantity', 'customer']
    list_display = ['id', 'order', 'total_price', 'book', 'quantity', 'customer']


@admin.register(BookInstance)
class BookInstanceModelAdmin(admin.ModelAdmin):
    list_display = ["id", "book", "book_status", "item_of_order"]
    list_filter = ["id", "book", "book_status", "item_of_order"]

