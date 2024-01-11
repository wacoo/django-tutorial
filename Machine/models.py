from django.db import models

# Create your models here.
class Machine(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=100)
    speed = models.IntegerField()