# Generated by Django 5.1.3 on 2024-11-17 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_users_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='users',
            name='updated_at',
        ),
    ]