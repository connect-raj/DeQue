# Generated by Django 5.0.2 on 2024-04-06 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_Main', '0007_cuisine_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='tables_data',
            name='table_layout',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
