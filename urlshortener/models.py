from django.db import models


class Url(models.Model):
    link = models.CharField(max_length=200)
    new_link = models.CharField(max_length=100,default='')