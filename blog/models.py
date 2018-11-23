from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=250)
    description_short = models.CharField(max_length=500)
    description_long = models.CharField(max_length=1500)
    url_assert = models.URLField()
    pub_date = models.DateTimeField()
    last_modifications = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
