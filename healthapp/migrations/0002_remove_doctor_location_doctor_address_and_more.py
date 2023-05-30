# Generated by Django 4.0.3 on 2023-05-29 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='location',
        ),
        migrations.AddField(
            model_name='doctor',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='doctor',
            name='description',
            field=models.TextField(default=''),
        ),
    ]