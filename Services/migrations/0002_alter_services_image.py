# Generated by Django 4.0.5 on 2022-08-27 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(upload_to='Services'),
        ),
    ]
