from django.db import models

class Sports(models.Model):
    name = models.CharField(max_length=50, default=None)

# Create your models here.
