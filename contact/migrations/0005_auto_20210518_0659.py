# Generated by Django 3.1.7 on 2021-05-18 06:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20210518_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='date_sending',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Дата рассылки'),
        ),
    ]
