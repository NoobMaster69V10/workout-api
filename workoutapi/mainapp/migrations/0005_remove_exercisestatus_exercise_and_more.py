# Generated by Django 5.0.3 on 2024-03-13 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_exercisestatus_remove_userplan_completed_exercises'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercisestatus',
            name='exercise',
        ),
        migrations.AddField(
            model_name='exercisestatus',
            name='exercise',
            field=models.ManyToManyField(blank=True, default=None, to='mainapp.exercises'),
        ),
    ]