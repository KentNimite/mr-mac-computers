# Generated by Django 3.0.2 on 2020-02-01 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0014_auto_20200201_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='photos'),
        ),
    ]
