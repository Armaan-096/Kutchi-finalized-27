# Generated by Django 4.2.4 on 2023-08-30 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_courses_courseduration'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDFFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file_path', models.CharField(max_length=200)),
            ],
        ),
    ]
