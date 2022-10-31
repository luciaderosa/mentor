from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=100)
    email=models.EmailField(max_length=254) #RFC 2821
    subject=models.CharField(max_length=60)
    message=models.CharField(max_length=512) #Postgres accepts VARCHAR max of 655536
    isAnswered=models.BooleanField(default=False)

    def __str__(self):
        return self.name +' - '+self.subject