# Generated by Django 3.1.7 on 2021-05-12 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20210512_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='city',
        ),
    ]
