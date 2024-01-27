# Generated by Django 4.2.4 on 2023-09-07 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_remove_studentsmodel_batch_day_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batch',
            old_name='batch_and_time',
            new_name='batch_day',
        ),
        migrations.RemoveField(
            model_name='studentsmodel',
            name='batch_and_time',
        ),
        migrations.AddField(
            model_name='batch',
            name='batch_time',
            field=models.CharField(default='8:30 pm - 10:30 pm', max_length=100),
        ),
        migrations.AddField(
            model_name='studentsmodel',
            name='batch_day',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students_with_batch_day', to='myapp.batch'),
        ),
        migrations.AddField(
            model_name='studentsmodel',
            name='batch_time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students_with_batch_time', to='myapp.batch'),
        ),
    ]