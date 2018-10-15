# Generated by Django 2.1.2 on 2018-10-14 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='exchange_rate',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True, verbose_name='Exchange rate to base currency'),
        ),
    ]
