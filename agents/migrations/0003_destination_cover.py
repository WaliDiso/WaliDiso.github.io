# Generated by Django 4.0.10 on 2023-09-14 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
