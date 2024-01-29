# Generated by Django 4.2.1 on 2024-01-29 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_dataset_useremail'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='dataset',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
    ]
