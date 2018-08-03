# Generated by Django 2.0.5 on 2018-07-27 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Triko', '0014_auto_20180703_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='triko_model',
            name='color',
        ),
        migrations.AddField(
            model_name='color',
            name='model',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Triko.Triko_Model'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='triko_model',
            name='like',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='triko_model',
            name='price',
            field=models.PositiveSmallIntegerField(default=150),
        ),
    ]
