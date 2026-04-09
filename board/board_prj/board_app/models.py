from django.db import models

class Guest(models.Model):
    username = models.CharField(max_length=50)
    stdnum = models.CharField(max_length=20)
    message = models.TextField()