# Generated by Django 5.0.3 on 2024-03-13 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_exercisestatus_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userplan',
            name='exercises_status',
            field=models.ManyToManyField(blank=True, default=None, to='mainapp.exercisestatus'),
        ),
    ]
