from django.db import models
from django.urls import reverse

# Create your models here.

class Mood(models.Model):
    mood = models.CharField(max_length=20)

    def __str__(self):
        return self.mood

    def get_absolute_url(self):
        return reverse('moods_detail', kwargs={'pk': self.id})



class Entry(models.Model):
    date = models.DateField('Entry Date')
    entry = models.TextField()
    moods = models.ManyToManyField(Mood)

    # def __str__(self):
    #     return self.date    

    def get_absolute_url(self):
        return reverse('detail', kwargs={'entry_id': self.id})

    class Meta:
        ordering = ['-date']

    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for entry_id: {self.entry_id} @{self.url}"