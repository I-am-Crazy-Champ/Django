# Generated by Django 3.2.18 on 2023-04-20 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_phone_contactdata_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]