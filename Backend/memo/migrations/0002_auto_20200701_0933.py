# Generated by Django 3.0.8 on 2020-07-01 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='my_chara',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='memo.Character'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memo',
            name='result',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='memo.Result'),
            preserve_default=False,
        ),
    ]
