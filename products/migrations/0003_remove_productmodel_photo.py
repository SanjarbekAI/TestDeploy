# Generated by Django 4.2.8 on 2023-12-12 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productimagemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='photo',
        ),
    ]