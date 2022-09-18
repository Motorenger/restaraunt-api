# Generated by Django 4.1.1 on 2022-09-18 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_alter_votemenus_options_alter_votemenus_votes'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='restaurant_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='restaurants.restaurant'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
