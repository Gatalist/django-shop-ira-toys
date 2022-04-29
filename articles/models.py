from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class UpdateStatusPrduct(models.Model):
    """Обновление Штрих-кодов"""
    title = models.CharField("Примечание", blank=True, default='', max_length=100)
    upload = models.FileField(upload_to='status_xlsx/%Y/%m/%d/')
    date = models.DateTimeField("Дата обновления", auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Обновление'
        verbose_name_plural = 'Обновление'


class UpdateStatusView(models.Model):
    """Отчет"""
    title = models.CharField("Примечание", blank=True, default='', max_length=100)
    status = models.CharField("status", blank=True, default='', max_length=100)
    date = models.DateTimeField("Дата обновления", auto_now_add=True)
    description = models.TextField("Описание", blank=True, default='',)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
