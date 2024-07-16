# Generated by Django 5.0.7 on 2024-07-16 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('short_description', models.CharField(max_length=200, verbose_name='short description')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('price_with_discount', models.PositiveIntegerField(blank=True, null=True, verbose_name='price with discount')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('date_time_created', models.DateTimeField(auto_now_add=True, verbose_name='date time created')),
            ],
            options={
                'verbose_name': 'products',
                'verbose_name_plural': 'products',
            },
        ),
    ]
