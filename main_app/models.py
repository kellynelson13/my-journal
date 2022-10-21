from django.db import models
from django.urls import reverse

# Create your models here.
class Entry(models.Model):
    date = models.DateField('Entry Date')
    entry = models.TextField()

    def __str__(self):
        return self.date    

    def get_absolute_url(self):
        return reverse('detail', kwargs={'entry_id': self.id})