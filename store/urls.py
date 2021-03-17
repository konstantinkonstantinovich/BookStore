
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

]
