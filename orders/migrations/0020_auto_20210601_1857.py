# Generated by Django 3.1.7 on 2021-06-01 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_auto_20210517_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=0, verbose_name='Сумма заказа'),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='price_per_item',
            field=models.FloatField(default=0, verbose_name='Цена за единицу'),
        ),
        migrations.AlterField(
            model_name='productinbasket',
            name='total_price',
            field=models.FloatField(default=0, verbose_name='Сумма заказа'),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='price_per_item',
            field=models.FloatField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='total_price',
            field=models.FloatField(default=0, verbose_name='Сумма'),
        ),
    ]