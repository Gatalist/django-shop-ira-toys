# Generated by Django 3.1.7 on 2021-12-12 13:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_auto_20210709_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=25, null=True, verbose_name='Имя')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
            ],
            options={
                'verbose_name': 'Наличие',
                'verbose_name_plural': 'Наличие',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='dateAdd',
            field=models.DateField(default=datetime.date.today, verbose_name='Добавлен'),
        ),
        migrations.AlterField(
            model_name='product',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Включен'),
        ),
        migrations.AlterField(
            model_name='product',
            name='retail',
            field=models.FloatField(null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.availability', verbose_name='Наличие'),
        ),
    ]
