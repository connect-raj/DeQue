# Generated by Django 5.0.2 on 2024-04-25 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_side', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.CharField(default='incomplete', max_length=20),
        ),
    ]
