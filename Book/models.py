from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Book(models.Model):
    title = models.CharField(verbose_name='title', max_length=255)
    author_name = models.CharField(verbose_name='author', max_length=255)
    description = models.CharField(verbose_name='description', max_length=255)

