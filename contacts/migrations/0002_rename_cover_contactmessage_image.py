# Generated by Django 4.0.10 on 2023-09-27 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmessage',
            old_name='cover',
            new_name='image',
        ),
    ]
