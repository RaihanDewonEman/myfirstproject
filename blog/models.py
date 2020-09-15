from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images/')
    post = models.TextField()
    postdate = models.DateField()


    def __str__(self):
        return self.title
