# Generated by Django 3.0.4 on 2020-04-12 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0042_gallery_name_of_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='date_added',
            field=models.DateTimeField(verbose_name='Last Updated'),
        ),
    ]
