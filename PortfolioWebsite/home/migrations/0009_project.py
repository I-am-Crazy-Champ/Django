# Generated by Django 3.2.18 on 2023-04-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('location', models.TextField()),
                ('desc', models.TextField()),
                ('link', models.TextField()),
                ('tech', models.TextField()),
            ],
        ),
    ]