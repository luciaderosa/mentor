from django.db import models
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    # Campos y atributos
    # max_length= 20 — Establece que la longitud máxima del valor
    # de este campo es 20 caracteres.
    # help_text="texto..." — proporciona una etiqueta de texto
    # para mostrar que ayuda.

    title = models.CharField(max_length=100, help_text="Título del evento")
    # Cadena para representar el objeto MyModelName
    # (en el sitio de Admin, etc.)
    text = models.TextField(help_text="Resumen del evento")
    date = models.DateTimeField(help_text="Fecha y hora del evento")
    image = models.ImageField(upload_to="events")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta:
        # para que el evento más nuevo quedo primero
        ordering = ["-date"]

    # Métodos

    def get_absolute_url(self):
        return reverse("events")
    

    def __str__(self):
        # Cadena para representar el objeto MyModelName
        # (en el sitio de Admin, etc.)
        return self.title
