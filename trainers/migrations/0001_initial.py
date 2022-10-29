# Generated by Django 4.1.2 on 2022-10-29 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Trainer",
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
                ("first_name", models.CharField(help_text="Nombre", max_length=100)),
                ("last_name", models.CharField(help_text="Apellido", max_length=100)),
                ("title", models.CharField(help_text="Título", max_length=100)),
                ("brief", models.TextField(help_text="Resumen curricular")),
                ("photo", models.ImageField(help_text="Foto", upload_to="projects")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["last_name", "first_name"],
            },
        ),
    ]
