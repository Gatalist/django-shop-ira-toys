# Generated by Django 3.1.7 on 2021-04-25 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinbasket',
            name='nmb',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='price_per_item',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]
