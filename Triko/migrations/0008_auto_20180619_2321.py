# Generated by Django 2.0.5 on 2018-06-19 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triko', '0007_person_buy_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person_buy_product',
            name='code',
            field=models.DecimalField(decimal_places=4, max_digits=4),
        ),
    ]
