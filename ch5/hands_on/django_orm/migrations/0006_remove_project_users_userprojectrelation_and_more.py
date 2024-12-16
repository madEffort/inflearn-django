# Generated by Django 5.1.3 on 2024-11-25 12:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_orm', '0005_projectuser_alter_project_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='users',
        ),
        migrations.CreateModel(
            name='UserProjectRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_orm.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='ProjectUser',
        ),
    ]
