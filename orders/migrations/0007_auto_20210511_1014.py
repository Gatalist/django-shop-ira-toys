# Generated by Django 3.1.7 on 2021-05-11 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='order',
            name='lastname',
            field=models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.status'),
        ),
    ]