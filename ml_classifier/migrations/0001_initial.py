# Generated by Django 4.2.8 on 2023-12-07 23:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Info",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("caption", models.CharField(max_length=100)),
                (
                    "description",
                    models.TextField(blank=True, max_length=2000, null=True),
                ),
                ("image", models.ImageField(max_length=200, upload_to="")),
                (
                    "category",
                    models.CharField(
                        choices=[("ml", "Machine Learning"), ("eda", "Visualization")],
                        max_length=100,
                    ),
                ),
            ],
        ),
    ]
