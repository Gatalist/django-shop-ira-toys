from django.db import models
from datetime import date, time
# Create your models here.

class Contact(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Все поддписки'


class Mailing(models.Model):
    is_active = models.BooleanField("Подтверждение рассылки", default=True)
    title = models.CharField("Тема", blank=True, default='', max_length=100)
    text = models.TextField("Текст", blank=True, default='', max_length=100)
    date = models.DateTimeField("Дата расслылки",auto_now_add=True)

    def __str__(self):
        return f"{self.date}"
    
    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Все рассылки'

