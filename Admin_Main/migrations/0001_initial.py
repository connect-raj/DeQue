# Generated by Django 5.0.2 on 2024-02-22 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='restaurants_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=30, unique=True)),
                ('restaurant_admin', models.CharField(max_length=30, unique=True)),
                ('restaurant_password', models.CharField(max_length=10)),
                ('restaurant_phone_number', models.CharField(max_length=12)),
                ('restaurant_address', models.CharField(max_length=1000)),
                ('restaurant_email', models.CharField(max_length=30)),
                ('restaurant_image', models.ImageField(upload_to='uploads')),
                ('restaurant_status', models.CharField(default='closed', max_length=10)),
                ('restaurant_activity', models.BooleanField(default=False, max_length=10)),
            ],
        ),
    ]
