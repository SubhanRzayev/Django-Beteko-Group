# Generated by Django 3.2.4 on 2021-12-20 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20211220_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('işçilər', models.IntegerField(blank=True, null=True)),
                ('musteriler', models.IntegerField(blank=True, null=True)),
                ('bitmis_layiheler', models.IntegerField(blank=True, null=True)),
                ('islenen_proyektler', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Employees',
                'verbose_name_plural': 'İsciler',
            },
        ),
    ]
