from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    image = models.ImageField(upload_to='employees')
    phone = models.DecimalField(max_digits=8, decimal_places=0)
    linkedin_username = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class JobPostingCategory(models.Model):
    team = models.CharField(max_length=256)
    hiring_manager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.team
