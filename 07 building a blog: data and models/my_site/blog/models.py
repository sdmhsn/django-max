from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)  # unique=True: I want to use the slug as a unique identifier for getting my posts. db_index=True: to let Django and Sequel trade an index for that field to make querying and filtering based on it a bit more effective.
    content = models.TextField(validators=[MinLengthValidator(10)])
