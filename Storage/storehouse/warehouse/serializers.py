from rest_framework import serializers

from .models import Book, Author, Category, Order, OrderItem


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'category', 'price', 'rating', 'image', 'description', 'status', 'publication_year')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('phone', 'first_name', 'status', 'email')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('order', 'total_price', 'book', 'quantity')

