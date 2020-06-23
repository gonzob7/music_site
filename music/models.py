# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Musician(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    birth_city = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
