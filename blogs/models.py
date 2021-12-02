from django.db import models

# Create your models here.
class Blog(models.Model):

    id=models.BigIntegerField
    title=models.TextField(max_length = 200)
    description=models.TextField()

