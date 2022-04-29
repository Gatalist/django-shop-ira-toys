# Generated by Django 3.1.7 on 2021-05-14 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20210514_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sale',
        ),
        migrations.RemoveField(
            model_name='product',
            name='wholesale',
        ),
        migrations.AlterField(
            model_name='product',
            name='retail',
            field=models.IntegerField(default=1, help_text='грн.', null=True, verbose_name='Розница'),
        ),
    ]
