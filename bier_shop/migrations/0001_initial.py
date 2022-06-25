# Generated by Django 4.0.5 on 2022-06-25 13:09

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BierCompany",
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
                ("name", models.CharField(max_length=100)),
                ("logo", models.ImageField(upload_to="")),
                ("country", django_countries.fields.CountryField(max_length=2)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Bier",
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
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="")),
                (
                    "bier_type",
                    models.CharField(
                        choices=[
                            ("Pilsner", "Pilsner"),
                            ("Dark Lager", "Dark Lager"),
                            ("German Bock", "German Bock"),
                            ("Brown Ale", "Brown Ale"),
                            ("Pale Ale", "Pale Ale"),
                            ("India Pale Ale", "Indian Pale Ale"),
                            ("Porter", "Porter"),
                            ("Stout", "Stout"),
                        ],
                        max_length=100,
                    ),
                ),
                ("description", models.TextField()),
                (
                    "bier_company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bier_shop.biercompany",
                    ),
                ),
            ],
        ),
    ]