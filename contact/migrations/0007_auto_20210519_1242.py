# Generated by Django 3.1.7 on 2021-05-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20210518_0702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='date_sending',
        ),
        migrations.RemoveField(
            model_name='mailing',
            name='time_sending',
        ),
        migrations.AlterField(
            model_name='mailing',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Подтвердить рассылку'),
        ),
    ]
