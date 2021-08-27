# Generated by Django 3.2.6 on 2021-08-26 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('discounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'دسته\u200cبندی',
                'verbose_name_plural': 'دسته\u200cبندی\u200cها',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('time_add', models.DateTimeField(auto_now_add=True)),
                ('price', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='covers/')),
                ('storage', models.PositiveIntegerField(default=1)),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ManyToManyField(related_name='book', to='book.Category')),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='discount', to='discounts.discount')),
            ],
            options={
                'verbose_name': 'کتاب',
                'verbose_name_plural': 'کتاب\u200cها',
            },
        ),
    ]
