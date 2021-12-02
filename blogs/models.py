from django.db import models

# Create your models here.
class Blog(models.Model):
    
    title=models.TextField()
    description=models.TextField()