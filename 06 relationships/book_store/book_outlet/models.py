from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    # def full_name(self):
    #     return f'{self.first_name} {self.last_name}'

    # def __str__(self):  # second step (general full name utility method)
    #     return self.full_name()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'  # first step


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    # author = models.CharField(null=True, max_length=100)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name='books')  # to connect Author model to Book model (one to many relation)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default='', blank=True, null=False, db_index=True)

    def get_abolute_url(self):
        return reverse('book-detail', args=[self.slug])

    def __str__(self):
        return f'{self.title} ({self.rating})'
