# Generated by Django 3.2.4 on 2021-11-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='email',
            field=models.EmailField(blank=True, default='office@beteko.az', max_length=254),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.IntegerField(default='012-570-00-04'),
        ),
    ]
