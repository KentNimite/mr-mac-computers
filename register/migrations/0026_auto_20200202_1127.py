# Generated by Django 3.0.2 on 2020-02-02 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0025_auto_20200202_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userauth',
            name='firstname',
        ),
        migrations.AlterField(
            model_name='userauth',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]