# Generated by Django 3.1.7 on 2021-06-01 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20210601_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='retail',
            field=models.FloatField(default=1, help_text='грн.', null=True, verbose_name='Цена'),
        ),
    ]
