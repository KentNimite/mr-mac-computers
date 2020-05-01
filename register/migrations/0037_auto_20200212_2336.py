# Generated by Django 3.0.2 on 2020-02-13 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0036_auto_20200208_0744'),
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='display_pic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='HolidayAssignmentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100)),
                ('question', models.TextField()),
                ('correct_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Options')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Students')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.TermOfYear')),
            ],
        ),
        migrations.CreateModel(
            name='HolidayAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100)),
                ('question', models.TextField(verbose_name='Write your Questions here..')),
                ('class_of_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Class')),
                ('correct_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Options')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Subject')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.TermOfYear')),
            ],
        ),
    ]
