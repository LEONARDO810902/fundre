# Generated by Django 4.0.2 on 2022-04-07 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='carousel',
            field=models.BooleanField(default=False),
        ),
    ]
