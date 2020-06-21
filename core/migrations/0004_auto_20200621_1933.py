# Generated by Django 3.0.6 on 2020-06-21 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200621_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='ASU_IMGS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asu_images', models.ImageField(blank=True, null=True, upload_to='covers/%Y/%m/%D/')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
