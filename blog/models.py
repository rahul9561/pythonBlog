from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Post(models.Model):
    featured_image = models.ImageField(upload_to='images/')
    title=models.CharField(max_length=150)
    desc=models.TextField()


    def __str__(self):
        return self.title
    
    



