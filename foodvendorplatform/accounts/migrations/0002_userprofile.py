# Generated by Django 4.2.2 on 2023-06-09 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                (
                    "profile_pic",
                    models.ImageField(
                        blank=True, null=True, upload_to="user/profile_pics"
                    ),
                ),
                (
                    "cover_pic",
                    models.ImageField(
                        blank=True, null=True, upload_to="user/cover_pics"
                    ),
                ),
                ("address_1", models.CharField(blank=True, max_length=100, null=True)),
                ("address_2", models.CharField(blank=True, max_length=100, null=True)),
                ("country", models.CharField(blank=True, max_length=50, null=True)),
                ("state", models.CharField(blank=True, max_length=50, null=True)),
                ("city", models.CharField(blank=True, max_length=50, null=True)),
                ("zip_code", models.CharField(blank=True, max_length=50, null=True)),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
