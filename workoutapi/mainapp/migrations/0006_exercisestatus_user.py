# Generated by Django 5.0.3 on 2024-03-13 09:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_remove_exercisestatus_exercise_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercisestatus',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
