from django.db import models
from trainers.models import Trainer

# Create your models here.
class Course(models.Model):

    name = models.CharField(max_length=100, help_text="Nombre del curso")
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)
    brief = models.TextField(help_text="Presentación del curso")
    text = models.TextField(help_text="Detalle del curso")
    fee = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="courses")
    seats = models.IntegerField(help_text="Cantidad de plazas")
    schedule = models.CharField(max_length=100, help_text="Días y horarios \
        curso")
    trainer = models.ForeignKey(Trainer, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, help_text="Categoría de Cursos")
    description = models.TextField(help_text="Descripción de la categoría")

    class Meta:
        ordering = ["name"]
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
