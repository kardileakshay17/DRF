from rest_framework import serializers
from students .models import studentsModel
from employees .models import employeeModel


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=studentsModel
        fields='__all__'

class employeeSerializers(serializers.ModelSerializer):
    class Meta:
        model=employeeModel
        fields='__all__'