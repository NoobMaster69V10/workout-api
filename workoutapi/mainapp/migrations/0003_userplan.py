# Generated by Django 5.0.3 on 2024-03-13 08:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_exercises'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.SmallIntegerField()),
                ('goals', models.CharField(max_length=255)),
                ('exercise_type', models.CharField(blank=True, max_length=255, null=True)),
                ('daily_duration', models.SmallIntegerField()),
                ('completed_exercises', models.JSONField(null=True)),
                ('exercises', models.ManyToManyField(blank=True, default=None, to='mainapp.exercises')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User plan',
                'verbose_name_plural': 'User plans',
            },
        ),
    ]
