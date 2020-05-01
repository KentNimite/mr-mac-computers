# Generated by Django 3.0.2 on 2020-02-07 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0030_auto_20200207_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='teacher',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='date_added',
            field=models.DateTimeField(verbose_name='Last Updated'),
        ),
    ]