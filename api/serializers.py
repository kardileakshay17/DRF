from rest_framework import serializers
from students .models import studentsModel


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=studentsModel
        fields='__all__'