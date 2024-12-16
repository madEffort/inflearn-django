# Generated by Django 5.1.3 on 2024-11-25 12:48

import uuid
from django.db import migrations, models


def add_uuid_to_existing_users(apps, schema_editor):
    User = apps.get_model('django_orm', 'User')
    for instance in User.objects.all():
        instance.uuid = uuid.uuid4()
        instance.save()


class Migration(migrations.Migration):

    dependencies = [
        ('django_orm', '0006_remove_project_users_userprojectrelation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
        migrations.RunPython(add_uuid_to_existing_users, reverse_code=migrations.RunPython.noop)
    ]