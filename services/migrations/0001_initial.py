# Generated by Django 3.2.4 on 2021-11-03 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('is_published', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('is_published', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_en', models.CharField(max_length=50, null=True)),
                ('title_az', models.CharField(max_length=50, null=True)),
                ('title_ru', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(max_length=1000)),
                ('description_en', models.TextField(max_length=1000, null=True)),
                ('description_az', models.TextField(max_length=1000, null=True)),
                ('description_ru', models.TextField(max_length=1000, null=True)),
                ('cover_image', models.ImageField(upload_to='service_img')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services_category', to='services.categoryservice')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_en', models.CharField(max_length=50, null=True)),
                ('title_az', models.CharField(max_length=50, null=True)),
                ('title_ru', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(max_length=1000)),
                ('description_en', models.TextField(max_length=1000, null=True)),
                ('description_az', models.TextField(max_length=1000, null=True)),
                ('description_ru', models.TextField(max_length=1000, null=True)),
                ('image', models.ImageField(upload_to='project_img')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects_category', to='services.categoryproject')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='service_image')),
                ('projects', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects_image', to='services.project')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_image', to='services.service')),
            ],
        ),
    ]
