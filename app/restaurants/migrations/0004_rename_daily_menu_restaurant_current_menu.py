# Generated by Django 4.1.1 on 2022-09-19 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_alter_votemenus_options_alter_votemenus_votes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='daily_menu',
            new_name='current_menu',
        ),
    ]