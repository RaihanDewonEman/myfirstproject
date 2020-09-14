from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    post = models.TextField()
    postdate = models.DateField()
