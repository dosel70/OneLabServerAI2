# Generated by Django 5.0.2 on 2024-05-22 13:42

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("place", "0001_initial"),
        ("university", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="PlaceMember",
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
                (
                    "place_member_status",
                    models.SmallIntegerField(choices=[(0, "결제"), (1, "환불")], default=0),
                ),
                (
                    "place",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="place.place"
                    ),
                ),
                (
                    "university",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="university.university",
                    ),
                ),
            ],
            options={
                "db_table": "tbl_place_member",
            },
        ),
    ]
