# Generated by Django 3.0.2 on 2020-01-31 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_auto_20200130_0620'),
    ]

    operations = [
        migrations.AddField(
            model_name='reciept',
            name='New_signature',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]