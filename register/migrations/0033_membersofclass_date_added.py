# Generated by Django 3.0.2 on 2020-02-08 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0032_membersofclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='membersofclass',
            name='date_added',
            field=models.DateTimeField(null=True, verbose_name='Last Updated'),
        ),
    ]
