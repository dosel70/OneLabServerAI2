# Generated by Django 5.0.2 on 2024-05-22 13:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="File",
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
                ("created_date", models.DateTimeField(auto_now_add=True)),
                (
                    "updated_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("file_size", models.FloatField()),
            ],
            options={
                "db_table": "tbl_file",
                "ordering": ["-id"],
            },
        ),
    ]
