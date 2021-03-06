# Generated by Django 3.0.2 on 2020-02-08 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0033_membersofclass_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membersofclass',
            name='Class',
        ),
        migrations.AddField(
            model_name='membersofclass',
            name='class_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.Class'),
        ),
        migrations.AlterField(
            model_name='membersofclass',
            name='date_added',
            field=models.DateTimeField(verbose_name='Last Updated'),
        ),
    ]
