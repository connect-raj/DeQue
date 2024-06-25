# Generated by Django 5.0.2 on 2024-06-19 17:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Admin_Main", "0010_alter_tables_data_table_layout"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("User", models.CharField(max_length=50)),
                ("PhoneNumber", models.CharField(max_length=15)),
                ("NumberOfGuests", models.IntegerField()),
                ("SelectedTableID", models.IntegerField()),
                ("ExtraInstruction", models.TextField(blank=True)),
                ("CreatedAt", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
