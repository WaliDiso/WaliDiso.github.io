# Generated by Django 4.0.10 on 2023-09-15 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0005_alter_destination_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='destination',
            options={'permissions': [('special_status', 'Can read all of the destinations')]},
        ),
    ]
