# Generated by Django 5.0.7 on 2024-07-18 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=True, upload_to='cover/', verbose_name='image'),
        ),
    ]
