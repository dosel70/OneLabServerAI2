# Generated by Django 5.0.2 on 2024-05-22 13:44

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("exhibition", "0001_initial"),
        ("university", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExhibitionMember",
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
                    "exhibition_member_status",
                    models.SmallIntegerField(choices=[(0, "참가"), (1, "종료")], default=0),
                ),
                (
                    "exhibition",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="exhibition.exhibition",
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
                "db_table": "tbl_exhibition_member",
            },
        ),
    ]
