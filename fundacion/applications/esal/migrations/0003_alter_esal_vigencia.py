# Generated by Django 4.0.2 on 2022-04-04 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esal', '0002_esal_vigencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esal',
            name='vigencia',
            field=models.CharField(choices=[('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024')], max_length=4),
        ),
    ]
