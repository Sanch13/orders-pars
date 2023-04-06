from django.db import models


class DataIcetrade(models.Model):
    date = models.DateField(auto_created=True)
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=250, unique=True)
    deadline = models.CharField(max_length=250)
    price = models.CharField(max_length=50)
