# Generated by Django 4.1.3 on 2022-12-08 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='display_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='estimated_delivery_days',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
