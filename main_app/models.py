from django.db import models

# Create your models here.
class Entry(models.Model):
    date = models.DateField('Entry Date')
    entry = models.TextField()