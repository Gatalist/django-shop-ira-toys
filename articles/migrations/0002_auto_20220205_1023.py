# Generated by Django 3.1.7 on 2022-02-05 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='updatestatusprduct',
            options={'verbose_name': 'Обновление', 'verbose_name_plural': 'Обновление'},
        ),
        migrations.AlterModelOptions(
            name='updatestatusview',
            options={'verbose_name': 'Результат', 'verbose_name_plural': 'Результаты'},
        ),
    ]
