# Generated by Django 3.1.7 on 2021-04-25 12:12

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210425_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='poster',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='', verbose_name=products.models.Product),
        ),
    ]