# Generated by Django 4.1.2 on 2022-10-29 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
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
                    "title",
                    models.CharField(help_text="Título del evento", max_length=100),
                ),
                ("text", models.TextField(help_text="Resumen del evento")),
                ("date", models.DateTimeField(help_text="Fecha y hora del evento")),
                ("image", models.ImageField(upload_to="projects")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
    ]
