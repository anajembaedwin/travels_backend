from django.db import models

# Create your models here.

class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add other fields as needed
