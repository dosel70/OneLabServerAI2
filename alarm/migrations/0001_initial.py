# Generated by Django 5.0.2 on 2024-05-22 13:44

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("member", "0001_initial"),
        ("onelab", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Alarm",
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
                    "alarm_status",
                    models.SmallIntegerField(
                        choices=[(0, "승인"), (1, "거절"), (-1, "탈퇴"), (2, "대기")], default=2
                    ),
                ),
                ("alarm_message", models.CharField(max_length=100)),
                ("alarm_receiver", models.CharField(max_length=100)),
                ("alarm_sender", models.CharField(max_length=100)),
                ("status", models.BooleanField(default=1)),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="member.member"
                    ),
                ),
                (
                    "onelab",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="onelab.onelab"
                    ),
                ),
            ],
            options={
                "db_table": "tbl_alarm",
                "ordering": ["-id"],
            },
        ),
    ]
