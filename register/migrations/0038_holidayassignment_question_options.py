# Generated by Django 3.0.2 on 2020-02-13 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0037_auto_20200212_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='holidayassignment',
            name='question_options',
            field=models.TextField(default='options', verbose_name='Options'),
            preserve_default=False,
        ),
    ]
