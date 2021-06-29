from django.db import models

from django.db import models


class App(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField()
    last_edit = models.DateField()
    article = models.TextField()