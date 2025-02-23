# Generated by Django 5.0.2 on 2024-05-22 13:42

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("member", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="School",
            fields=[
                ("created_date", models.DateTimeField(auto_now_add=True)),
                (
                    "updated_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "school_member_address",
                    models.CharField(default="서울시 강남구", max_length=500),
                ),
                ("school_name", models.CharField(max_length=100)),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        primary_key=True,
                        serialize=False,
                        to="member.member",
                    ),
                ),
                ("school_member_status", models.BooleanField(default=False)),
            ],
            options={
                "db_table": "tbl_school",
                "ordering": ["-created_date"],
            },
        ),
    ]
