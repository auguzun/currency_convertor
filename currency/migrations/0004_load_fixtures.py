from django.core.management import call_command
from django.db import migrations

fixture = 'currency/fixtures/fixtures.json'


def load_fixture(apps, schema_editor):
    call_command('loaddata', fixture, app_label='currency')


def unload_fixture(apps, schema_editor):
    Currency = apps.get_model("currency", "Currency")
    Currency.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('currency', '0003_auto_20181014_1416'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]
