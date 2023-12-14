# Generated by Django 4.2.1 on 2023-07-02 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('contact', models.IntegerField(max_length=10)),
                ('role', models.IntegerField(max_length=20)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]