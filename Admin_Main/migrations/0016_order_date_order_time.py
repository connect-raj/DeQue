# Generated by Django 5.0.2 on 2024-06-26 18:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Admin_Main", "0015_contact"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="Date",
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name="order",
            name="Time",
            field=models.CharField(default=0, max_length=50),
        ),
    ]