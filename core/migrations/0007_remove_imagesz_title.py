# Generated by Django 3.0.6 on 2020-06-21 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200621_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagesz',
            name='title',
        ),
    ]
