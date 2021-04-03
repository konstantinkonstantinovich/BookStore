
from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),
    path('login/', views.LoginForm.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.RegistrationForm.as_view(), name='registration'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('cart/list/', views.CartListView.as_view(), name='cart-list'),
    path('cart/<int:pk>', views.add_to_cart, name='cart-create'),
    path('books/buy_now/', views.buy_book_now, name='buy-book-now'),
    path('cart/list/buy_in_cart/', views.buy_book_in_cart, name='buy-in-cart'),
    path('comment_add/<int:pk>', views.CommentCreateView.as_view(), name='comment'),
    path('search/', views.SearchResultView.as_view(), name='search_results'),
    path('contact/', views.contact_form, name="store-contact"),
    path('cart/delete/<int:pk>/', views.delete_from, name="cart-delete"),
    path('cart/plus/<int:pk>', views.plus_form, name="cart-item-plus"),
    path('cart/minus/<int:pk>', views.minus_form, name="cart-item-minus"),
]
