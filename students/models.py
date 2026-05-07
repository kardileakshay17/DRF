from django.db import models

# Create your models here.
class studentsModel(models.Model):
    Student_id=models.CharField(max_length=10)
    Name=models.CharField(max_length= 32)
    Branch=models.CharField(max_length=32)

    def __str__(self):
        return self.Name