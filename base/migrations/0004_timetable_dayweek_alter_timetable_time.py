# Generated by Django 4.2 on 2023-05-19 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_timetable_group_account_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='dayWeek',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='time',
            field=models.TimeField(default=None),
        ),
    ]
