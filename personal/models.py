from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='personal/images')
    url = models.URLField(blank=True)
