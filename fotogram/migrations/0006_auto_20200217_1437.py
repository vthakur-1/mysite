# Generated by Django 2.2.9 on 2020-02-17 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotogram', '0005_auto_20200217_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(max_length=400, null=True),
        ),
    ]
