from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    qualification = models.CharField(max_length=30,null=True,blank=True)
    contact = models.CharField(max_length=30,null=True,blank=True)
    email = models.EmailField()
    def __str__(self):
        return str(self.pk)
    class Meta:
        verbose_name_plural = "employees"
