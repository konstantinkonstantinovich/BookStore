from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Book(models.Model):

    class LoanStatus(models.IntegerChoices):
        AVAILABLE = 1, _('available')
        NOT_AVAILABLE = 2, _('not available')

    title = models.CharField(max_length=250)
    author = models.ManyToManyField(Author)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='static/images', blank=True)
    publication_year = models.PositiveSmallIntegerField()
    status = models.PositiveSmallIntegerField(
        choices=LoanStatus.choices, default=LoanStatus.AVAILABLE, blank=True
    )
    customer = models.ManyToManyField(User, blank=True)
    rating = models.FloatField(default=0)


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




