# Generated by Django 3.0.8 on 2020-07-03 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0005_remove_memo_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='memo',
            name='time',
            field=models.TimeField(),
        ),
    ]
