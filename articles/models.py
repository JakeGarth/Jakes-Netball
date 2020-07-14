from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    #comment
    '''
    def save(self, *args, **kwargs):
         super().save(*args, **kwargs)

         img = Image.open(self.image.path)

         if img.height > 300 or img.width > 300:
             output_size = (300, 300)
             img.thumbnail(output_size)
             img.save(self.image.path)
    '''
    def snippet(self):
        return self.body[:50] + '...'
