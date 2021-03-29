import datetime

from django.db.models import Count
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin

from .models import Book, Cart, CartBook, Comment


def index(request):
    cart_total_price = Cart.objects.aggregate(Sum('total_price'))
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(
        request,
        'index.html',
        context={
            'cart_total_price': cart_total_price,
            'num_visits': num_visits,
        }
    )


def success(request):
    return HttpResponse("SUCCESS!!!")


class LoginForm(LoginView):
    model = User
    template_name = "registration/login.html"
    success_url = '/store/'

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        login(self.request, form.get_user())
        messages.add_message(self.request, messages.SUCCESS, 'Authorization success!')
        return HttpResponseRedirect(self.get_success_url())


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/store/login/')


class RegistrationForm(CreateView):
    model = User
    template_name = "registration/registration.html"
    fields = ['username', 'email', 'password', 'first_name', 'last_name']
    success_url = '/store/login/'

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        user = form.cleaned_data['username']
        fake_email = form.cleaned_data['email']
        passw = form.cleaned_data['password']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        User.objects.create_user(
            username=user,
            email=fake_email,
            password=passw,
            first_name=first_name,
            last_name=last_name,
        )
        messages.add_message(self.request, messages.SUCCESS, 'Registration success!')
        return redirect(self.success_url)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('shop:login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change_form.html', {
        'form': form
    })


class BookListView(ListView):
    model = Book
    template_name = 'store/book_list.html'


class BookDetailView(DetailView, MultipleObjectMixin):
    model = Book
    template_name = 'store/book_detail.html'

    def get_context_data(self, **kwargs):
        object_lists = Comment.objects.filter(book=self.get_object())
        context = super(BookDetailView, self).get_context_data(object_list=object_lists, **kwargs)
        context['myDate'] = datetime.datetime.now()
        return context


class UserProfile(DetailView):
    model = User
    template_name = 'store/user_detail.html'

    def get_object(self, queryset=None):
        user = self.request.user
        return user


class CartListView(ListView, LoginRequiredMixin):
    model = Cart
    template_name = 'store/card_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_total_price = Cart.objects.aggregate(Sum('total_price'))
        if cart_total_price['total_price__sum'] is None:
            cart_total_price['total_price__sum'] = 0
        context['cart_total'] = cart_total_price['total_price__sum']
        return context


def add_to_cart(request, pk):
    count = 1
    user = request.user
    cart_item = CartBook(
        customer=user,
        book=Book.objects.get(pk=pk),
        quantity=count
    )
    cart_item.save()
    cart = Cart(
        product=cart_item,
        total_books=cart_item.quantity,
        total_price=cart_item.book.price,
        owner=user
    )

    cart.save()
    return redirect('store:cart-list')


class CommentCreateView(CreateView):
    model = Comment
    fields = ['comment', 'rating']
    template_name = 'store/comment_form.html'
    success_url = '/store/books/'

    def form_valid(self, form):
        form.instance.book = get_object_or_404(Book, pk=self.kwargs['pk'])
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        else:
            if User.objects.filter(username='anon').exists():
                form.instance.author = User.objects.get(username='anon')
            else:
                User.objects.create(username='anon')
                form.instance.author = User.objects.get(username='anon')
        return super(CommentCreateView, self).form_valid(form)


def buy_book_now(request):
    messages.add_message(request, messages.SUCCESS, 'Buying success!')
    return redirect('store:book-list')


def buy_book_in_cart(request):
    Cart.objects.all().delete()
    CartBook.objects.all().delete()
    messages.add_message(request, messages.SUCCESS, 'Buying success!')
    return redirect('store:book-list')


def delete_item_from_cart(request):
    cart_item = Cart.objects.get()