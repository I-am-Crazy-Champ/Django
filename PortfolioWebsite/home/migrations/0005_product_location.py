# Generated by Django 3.2.18 on 2023-04-20 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_products_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
