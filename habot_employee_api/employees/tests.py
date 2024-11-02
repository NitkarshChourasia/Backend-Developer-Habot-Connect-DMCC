# tests.py

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Employee  # Import your model if you want to check database entries

class EmployeeTests(APITestCase):
    def test_create_employee(self):
        """
        Test creating an employee with valid data.
        """
        # Set up the URL for employee creation
        url = reverse('employee-list')  # Adjust the name to match your `urls.py`
        
        # Define data to be posted
        data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "department": "Engineering",
            "role": "Developer"
        }
        
        # Make a POST request
        response = self.client.post(url, data, format='json')
        
        # Check for a 201 Created response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_employees(self):
        """
        Test listing all employees.
        """
        # Create an employee first (or you can use a fixture if preferred)
        Employee.objects.create(name="Jane Doe", email="jane.doe@example.com", department="HR", role="Manager")
        
        # Set up the URL for listing employees
        url = reverse('employee-list')
        
        # Make a GET request
        response = self.client.get(url, format='json')
        
        # Check if the response is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if there is at least one employee in the response data
        self.assertGreaterEqual(len(response.data), 1)
