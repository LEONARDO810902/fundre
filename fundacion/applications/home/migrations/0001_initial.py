# Generated by Django 4.0.2 on 2022-02-14 05:30

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('full_name', models.CharField(max_length=60, verbose_name='Nombres Apellidos')),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=30, verbose_name='Nombre')),
                ('description', models.TextField()),
                ('about_title', models.CharField(max_length=50, verbose_name='Titulo Nosotros')),
                ('about_text', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email de contacto')),
                ('phone', models.CharField(max_length=15, verbose_name='Telefono')),
            ],
            options={
                'verbose_name': 'Pagina Principal',
                'verbose_name_plural': 'Pagina Principal',
            },
        ),
        migrations.CreateModel(
            name='Suscribirse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Suscritor',
                'verbose_name_plural': 'Suscritores',
            },
        ),
    ]
