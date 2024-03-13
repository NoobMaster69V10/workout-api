# Generated by Django 5.0.3 on 2024-03-13 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_userplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='userplan',
            name='completed_exercises',
        ),
    ]