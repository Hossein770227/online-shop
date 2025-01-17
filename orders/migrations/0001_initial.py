# Generated by Django 5.0.7 on 2024-07-21 18:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0005_alter_product_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='full name')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('address', models.CharField(max_length=700, verbose_name='address')),
                ('order_notes', models.CharField(max_length=500, verbose_name='order notes')),
                ('is_paid', models.BooleanField(default=False, verbose_name='is paid')),
                ('date_time_created', models.DateTimeField(auto_now_add=True, verbose_name='date time created')),
                ('date_time_modified', models.DateTimeField(auto_now=True, verbose_name='date time modified')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='quantity')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order', verbose_name='order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='products.product', verbose_name='product')),
            ],
        ),
    ]
