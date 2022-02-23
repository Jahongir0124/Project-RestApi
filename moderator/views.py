from django.shortcuts import render
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework import viewsets,status
class ModeratorViewsets(viewsets.ModelViewSet):
    queryset = Moderator.objects.all()
    serializer_class = MOderatorSerializer
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
            moderator = Moderator.objects.create(
                user=user,
                phone=data['phone'],
                image=data['image']
            )
            moderator.save()
            return Response({'status':'created'},status=status.HTTP_201_CREATED)
        return Response({"salom"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
