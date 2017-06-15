from django.db import models

# Create your models here.
class Photos(models.Model):
    image_id = models.CharField(max_length=100)
    image_one = models.ImageField(upload_to='photos', max_length=500)
    image_two = models.ImageField(upload_to='photos', max_length=500)