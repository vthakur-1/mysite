# Generated by Django 2.2.9 on 2020-02-17 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fotogram', '0003_auto_20200213_0806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='Name',
            new_name='name',
        ),
    ]
