from django.db import models
from datetime import date



class Usd(models.Model):
    name = models.FloatField("usd")
    date = models.DateField("Добавлен", auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'USD'
        verbose_name_plural = 'USD'


class Eur(models.Model):
    name = models.FloatField("eur")
    date = models.DateField("Добавлен", auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'EUR'
        verbose_name_plural = 'EUR'


class Uah(models.Model):
    name = models.FloatField("грн")
    date = models.DateField("Добавлен", auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'ГРН'
        verbose_name_plural = 'ГРН'

