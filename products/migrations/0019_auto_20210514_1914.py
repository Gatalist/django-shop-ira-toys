# Generated by Django 3.1.7 on 2021-05-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20210514_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description_free',
            field=models.TextField(blank=True, default=' ', max_length=200, null=True, verbose_name='Краткое описание'),
        ),
    ]
