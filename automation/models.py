from django.db import models

# Create your models here.
class Emails(models.Model):
    name = models.CharField(max_length)
    email = models.EmailField()
    