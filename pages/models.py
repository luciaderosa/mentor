from django.db import models

# Create your models here.

class Testimonial(models.Model):

    name = models.CharField(max_length=100, help_text="Nombre")
    title = models.CharField(max_length=100, help_text="Título")
    text = models.TextField(help_text="Texto del testimonio")
    image = models.ImageField(upload_to="testimonials")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # el orden de ingreso? la fecha de creación?
        # del más viejo al más nuevo?
        ordering = ["created"]

    def __str__(self):
        return self.name