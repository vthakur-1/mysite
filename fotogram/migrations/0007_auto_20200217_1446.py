# Generated by Django 2.2.9 on 2020-02-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotogram', '0006_auto_20200217_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
