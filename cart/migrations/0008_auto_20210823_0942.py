# Generated by Django 3.2.6 on 2021-08-23 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_alter_book_image'),
        ('cart', '0007_auto_20210822_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderbook',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book.book'),
        ),
        migrations.AlterField(
            model_name='orderbook',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderbook', to='cart.order'),
        ),
    ]