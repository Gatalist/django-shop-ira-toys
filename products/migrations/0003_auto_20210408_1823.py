# Generated by Django 3.1.7 on 2021-04-08 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210408_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale',
            field=models.PositiveIntegerField(help_text='Укажите сумму в грн.', null=True, verbose_name='Акция'),
        ),
    ]