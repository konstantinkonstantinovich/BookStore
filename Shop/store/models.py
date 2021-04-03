from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
# Create your models here.

User = get_user_model()


class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):

    class LoanStatus(models.IntegerChoices):
        AVAILABLE = 1, _('available')
        NOT_AVAILABLE = 2, _('not available')

    description = models.TextField()
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(Author)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images', blank=True)
    publication_year = models.PositiveSmallIntegerField()
    status = models.PositiveSmallIntegerField(
        choices=LoanStatus.choices, default=LoanStatus.AVAILABLE, blank=True
    )
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField(max_length=10000,
                               help_text="Input your comment.")
    rating = models.PositiveSmallIntegerField(
        choices=(
            (1, "★☆☆☆☆"),
            (2, "★★☆☆☆"),
            (3, "★★★☆☆"),
            (4, "★★★★☆"),
            (5, "★★★★★"),
        )

    )


class CartBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=9, decimal_places=2)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)


class Cart(models.Model):
    class OrderStatus(models.IntegerChoices):
        WAITING = 1, _('Waiting')
        IN_PROGRESS = 2, _('In progress')
        DONE = 4, _('Done')

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    total_books = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=9, decimal_places=2)
    status_buy = models.BooleanField(blank=True, default=False)
    status = models.PositiveSmallIntegerField(
        choices=OrderStatus.choices, default=OrderStatus.IN_PROGRESS
    )




