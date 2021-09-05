# Generated by Django 3.2.6 on 2021-08-28 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='کد')),
                ('percentage', models.FloatField(blank=True, default=0, verbose_name='درصد')),
                ('max_amount', models.IntegerField(blank=True, default=None, null=True, verbose_name='حداکثر تحفیف')),
                ('flat_fee', models.IntegerField(default=0, verbose_name='تخفیف ثابت')),
                ('expiration_date', models.DateTimeField(verbose_name='انقضا')),
            ],
            options={
                'verbose_name': 'کپن',
                'verbose_name_plural': 'کپن\u200cها',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('percentage', models.FloatField(default=0, verbose_name='درصد')),
                ('flat_amount', models.PositiveIntegerField(blank=True, null=True, verbose_name='مبلغ ثابت')),
            ],
            options={
                'verbose_name': 'تخفیف',
                'verbose_name_plural': 'تخفیف\u200cها',
            },
        ),
    ]