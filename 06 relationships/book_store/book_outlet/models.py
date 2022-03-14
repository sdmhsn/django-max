from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Country Entries'

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.street}, {self.postal_code}, {self.city}'

    class Meta:  # nested class in Address class. to fix Addresss word in django admin
        verbose_name_plural = 'Address Entries'  # plural name for Address class (without this meta class, the address word has triple sss in django amin)


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

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
    published_countries = models.ManyToManyField(Country)  # many to many relation. don't set up on_delete

    def get_abolute_url(self):
        return reverse('book-detail', args=[self.slug])

    def __str__(self):
        return f'{self.title} ({self.rating})'
