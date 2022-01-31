from django.db import models
from django.db.models.functions import datetime
from django.urls import reverse


class Card(models.Model):
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(primary_key=True, max_length=250, unique=True)

    def get_absolute_url(self):
        return reverse('cards:card_detail', args=[str(self.slug)])

    def __str__(self):
        return f'{self.name}'


class Master(models.Model):
    name = models.CharField(max_length=64)
    body = models.TextField()

    def __str__(self):
        return self.name, self.body
