# Generated by Django 2.1.2 on 2018-10-12 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('type', models.CharField(max_length=50, unique=True, verbose_name='Currency type')),
                ('exchange_rate', models.DecimalField(decimal_places=4, max_digits=6, verbose_name='Exchange rate to base currency')),
            ],
            options={
                'db_table': 'currency',
            },
        ),
    ]