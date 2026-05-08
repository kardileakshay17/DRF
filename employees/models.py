from django.db import models

# Create your models here.
class employeeModel(models.Model):
    emp_id=models.CharField(max_length=32)
    emp_name=models.CharField(max_length=32)
    designation=models.CharField(max_length=32)

    def __str__(self):
        return self.emp_name