# Generated by Django 3.2.4 on 2021-06-17 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
