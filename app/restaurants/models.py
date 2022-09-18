from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    daily_menu = models.ImageField()
    