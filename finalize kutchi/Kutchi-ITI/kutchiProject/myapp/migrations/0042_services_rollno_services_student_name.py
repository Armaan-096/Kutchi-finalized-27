# Generated by Django 4.2.4 on 2023-09-28 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0041_rename_service_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='rollno',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='services',
            name='student_name',
            field=models.CharField(default='student', max_length=100),
        ),
    ]
