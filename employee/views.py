from django.shortcuts import render
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework import viewsets,status
class EmployeeViewsets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            user = User.objects.create(
                username=data['user']['username'],
                first_name=data['user']['first_name'],
                last_name=data['user']['last_name'],
                email=data['user']['email'],
                password=data['user']['password']
            )
            user.save()
            employee = Employee.objects.create(
                user=user,
                phone=data['phone'],
                adress=data['adress'],
                image=data['image']
            )
            employee.save()
            return Response({'status':'created'},status=status.HTTP_201_CREATED)
        return Response({"salom"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
