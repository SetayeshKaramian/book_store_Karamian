# Generated by Django 3.2.6 on 2021-08-30 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='covers/blank.jpg', null=True, upload_to='profile_pics/', verbose_name='عکس'),
        ),
    ]