# Generated by Django 3.1.7 on 2021-06-30 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20210602_0720'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Под Категория')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='url')),
                ('poster', models.ImageField(upload_to='sub-category/', verbose_name='Изображение')),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Под Категория')),
            ],
            options={
                'verbose_name': 'Под Категория',
                'verbose_name_plural': 'Под Категории',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.subcategory', verbose_name='Категория'),
        ),
    ]
