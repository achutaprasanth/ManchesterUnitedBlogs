from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    # title
    title = models.CharField(max_length=50)
    # description
    description = models.CharField(max_length=50)
    # image
    image = models.ImageField(upload_to='blog_images', blank=True)
    date_posted = models.DateTimeField(default=datetime.datetime.now())
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title
