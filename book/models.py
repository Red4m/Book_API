from django.db import models
from django.contrib.auth.models import User
# User = get_user_model()


# class User(models.Model):
#     user = get_user_model()


class Book(models.Model):
    title = models.CharField(verbose_name='title', max_length=255)
    author_name = models.CharField(verbose_name='author', max_length=255)
    description = models.CharField(verbose_name='description', max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

