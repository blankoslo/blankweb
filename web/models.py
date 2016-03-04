from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    image = models.ImageField(upload_to='employees')

    def __str__(self):
        return self.name
