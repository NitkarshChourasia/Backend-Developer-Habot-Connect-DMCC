# models.py
from django.db import models

class Employee(models.Model):
    # name: Required field, maximum length 100 characters
    name = models.CharField(max_length=100)

    # email: Required and unique email field, ensures no duplicate emails in the system
    email = models.EmailField(unique=True)

    # department: Optional, specifies the employee's department, e.g., "HR", "Engineering"
    department = models.CharField(max_length=50, blank=True, null=True)

    # role: Optional, specifies the employee's role, e.g., "Manager", "Developer"
    role = models.CharField(max_length=50, blank=True, null=True)

    # date_joined: Automatically stores the date an employee was created in the system
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
