from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    home_town = models.CharField(max_length=35)
