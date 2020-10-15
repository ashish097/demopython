from django.shortcuts import render

from django.http.response import JsonResponse # for json response
from django.http import HttpResponse  #for Http response, for forms 

from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response #for resonse having a UI generated response includes json

from employee.models import Employee
from employee.serializers import EmployeeSerializer

from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def employee_list(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            employee = employee.filter(name__icontains=name)
        
        employee_serializer = EmployeeSerializer(employee, many=True)
        return Response(employee_serializer.data)

    elif request.method == 'POST':
       #employee_data = JSONParser().parse(request)
       #employee_serializer = EmployeeSerializer(data=employee_data)
       employee_serializer = EmployeeSerializer(data=request.data)
       if employee_serializer.is_valid():
           employee_serializer.save()
           return Response(employee_serializer.data) 
       return JsonResponse(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    # find tutorial by pk (id)
    employee = Employee.objects.get(pk=pk)
    if request.method == 'GET': 
        employee_serializer = EmployeeSerializer(employee) 
        return Response(employee_serializer.data)