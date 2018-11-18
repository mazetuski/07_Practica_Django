from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50, unique=True)


class Post(models.Model):

    title = models.CharField(max_length=250)
    description_short = models.CharField(max_length=500)
    description_long = models.CharField(max_length=1500)
    url_assert = models.URLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modifications = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
