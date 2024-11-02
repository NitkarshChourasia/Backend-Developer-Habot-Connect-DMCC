# Import necessary modules
from rest_framework import serializers
from .models import Employee

# Define the serializer class
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee           # specify the model to serialize
        fields = '__all__'         # use '__all__' to include all fields in the model, or specify a list of fields
        # Example: fields = ['id', 'name', 'position', 'hire_date']