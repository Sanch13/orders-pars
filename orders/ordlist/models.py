from django.db import models


class DataIcetrade(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    deadline = models.CharField(max_length=250)
    price = models.CharField(max_length=50)


class DataGoszakupki(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    deadline = models.CharField(max_length=250)
    price = models.CharField(max_length=50)
