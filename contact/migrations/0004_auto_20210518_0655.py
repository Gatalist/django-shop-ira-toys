# Generated by Django 3.1.7 on 2021-05-18 06:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_mailing'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='date_sending',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активировать рассылку?'),
        ),
    ]
