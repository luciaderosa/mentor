# Generated by Django 4.1.2 on 2022-10-29 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("trainers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "name",
                    models.CharField(help_text="Categoría de Cursos", max_length=100),
                ),
                (
                    "description",
                    models.TextField(help_text="Descripción de la categoría"),
                ),
            ],
            options={
                "verbose_name_plural": "Categories",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Course",
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
                    "name",
                    models.CharField(help_text="Nombre del curso", max_length=100),
                ),
                ("brief", models.TextField(help_text="Presentación del curso")),
                ("text", models.TextField(help_text="Detalle del curso")),
                ("fee", models.DecimalField(decimal_places=2, max_digits=6)),
                ("image", models.ImageField(upload_to="projects")),
                ("seats", models.IntegerField(help_text="Cantidad de plazas")),
                (
                    "schedule",
                    models.CharField(
                        help_text="Días y horarios         curso", max_length=100
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="courses.category",
                    ),
                ),
                (
                    "trainer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="trainers.trainer",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
    ]