# Generated by Django 3.2.6 on 2021-08-22 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_alter_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
    ]