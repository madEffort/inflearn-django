# Generated by Django 5.1.3 on 2024-11-24 13:26
import random
import string

from django.db import migrations


def generate_code():
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=8))


def insert_data(apps, schema_editor):
    ShortURL = apps.get_model("shortener", "ShortURL")

    objects = []
    for original_url in ["https://chat.com/", "https://stackoverflow.com/", "https://github.com/"]:
        objects.append(
            ShortURL(code=generate_code(), original_url=original_url)
        )

    ShortURL.objects.bulk_create(objs=objects, ignore_conflicts=True)


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_data, reverse_code=migrations.RunPython.noop),
    ]

