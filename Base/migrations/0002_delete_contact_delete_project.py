# Generated by Django 4.2.16 on 2024-11-17 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
