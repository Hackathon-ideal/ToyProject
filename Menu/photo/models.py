from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='menu/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title