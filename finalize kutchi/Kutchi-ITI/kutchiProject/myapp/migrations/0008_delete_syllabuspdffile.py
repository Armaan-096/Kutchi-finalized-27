# Generated by Django 4.2.4 on 2023-08-30 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_courses_file_path'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SyllabusPDFFile',
        ),
    ]