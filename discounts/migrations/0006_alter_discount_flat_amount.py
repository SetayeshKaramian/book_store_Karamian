# Generated by Django 3.2.6 on 2021-08-21 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0005_auto_20210821_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='flat_amount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
