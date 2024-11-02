# habot_employee_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response

class EmployeeListCreateAPIView(APIView):
    def get(self, request):
        # Implement the GET logic here
        return Response({"message": "GET request received"})

    def post(self, request):
        # Implement the POST logic here
        return Response({"message": "POST request received"})

        
