# Generated by Django 2.0.5 on 2018-07-27 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triko', '0015_auto_20180727_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='model',
        ),
        migrations.AddField(
            model_name='color',
            name='model',
            field=models.ManyToManyField(to='Triko.Triko_Model'),
        ),
    ]