from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class postBlog(models.Model):
    title = models.CharField(max_length=255)
    images = models.ImageField(upload_to='images')
    about_post = models.TextField()
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    update_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    