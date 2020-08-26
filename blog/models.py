from django.db import models


class Entries(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    text = models.TextField()
