# Generated by Django 5.1.3 on 2024-11-24 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_insert_data'),
    ]

    operations = [
        migrations.RunSQL(
            sql="UPDATE short_url SET access_count = access_count + 10;",
            reverse_sql="UPDATE short_url SET access_count = access_count - 10;"
        ),
    ]
