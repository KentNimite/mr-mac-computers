# Generated by Django 3.0.2 on 2020-01-31 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_auto_20200130_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciept',
            name='Amount_deposited',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reciept',
            name='Updated_balance',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
