# Generated by Django 3.0.2 on 2020-02-08 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0035_auto_20200208_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='date_added',
            field=models.DateTimeField(null=True, verbose_name='Last Updated'),
        ),
    ]