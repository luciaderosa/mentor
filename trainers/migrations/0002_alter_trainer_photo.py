# Generated by Django 4.1.2 on 2022-10-29 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trainers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trainer",
            name="photo",
            field=models.ImageField(help_text="Foto", upload_to="trainers"),
        ),
    ]
