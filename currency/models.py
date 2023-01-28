from django.db import models


class Usd(models.Model):
    name = models.FloatField("usd")
    date = models.DateField("Добавлен", auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'ГРН/USD'
        verbose_name_plural = 'ГРН/USD'


class Eur(models.Model):
    name = models.FloatField("eur")
    date = models.DateField("Добавлен", auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'ГРН/EUR'
        verbose_name_plural = 'ГРН/EUR'


class Uah(models.Model):
    name = models.FloatField("грн")
    date = models.DateField("Добавлен", auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'ГРН'
        verbose_name_plural = 'ГРН'
