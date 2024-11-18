# Generated by Django 5.1.3 on 2024-11-16 02:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 16, 2, 15, 1, 673729, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 16, 2, 15, 1, 673729, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='users',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=125, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='login',
            field=models.CharField(max_length=70, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='senha',
            field=models.CharField(max_length=150),
        ),
    ]