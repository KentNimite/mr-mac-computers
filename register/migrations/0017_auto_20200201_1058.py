# Generated by Django 3.0.2 on 2020-02-01 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0016_auto_20200201_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='photos'),
        ),
    ]