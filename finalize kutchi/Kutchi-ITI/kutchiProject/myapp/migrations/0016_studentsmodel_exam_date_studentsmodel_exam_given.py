# Generated by Django 4.2.4 on 2023-09-01 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_remove_studentsmodel_theexam_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsmodel',
            name='exam_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentsmodel',
            name='exam_given',
            field=models.BooleanField(default=False),
        ),
    ]