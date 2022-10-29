from django.db import models

# Create your models here.

class Trainer(models.Model):

    first_name = models.CharField(max_length=100, help_text="Nombre")
    last_name = models.CharField(max_length=100, help_text="Apellido")
    title = models.CharField(max_length=100, help_text="Título")
    brief = models.TextField(help_text="Resumen curricular")
    photo = models.ImageField(upload_to="trainers", help_text="Foto")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta ():
        ordering = ['last_name', 'first_name']

    def __str__(self):
        # Cadena para representar el objeto MyModelName
        # (en el sitio de Admin, etc.)
        return self.last_name + ", " + self.first_name

