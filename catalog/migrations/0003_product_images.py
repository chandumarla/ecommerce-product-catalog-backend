# Generated by Django 5.2.1 on 2025-05-17 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, upload_to='products/'),
        ),
    ]
