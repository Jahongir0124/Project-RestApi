from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import *
from .serializers import *
import json
class UserViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
class CategoryViewset(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializers
class ProductViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
class ProductByCategoryViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    def retrieve(self, request, *args, **kwargs):
        cat_id=kwargs['pk']
        products=self.queryset.filter(category_id=cat_id)
        seriallizer=self.get_serializer(products,many=True)
        return Response(seriallizer.data)
class OrderViewset(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializers
class OrderDetaisViewset(viewsets.ModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderSerializers
class OrderDetaisActionViewset(viewsets.ModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrederDetailsSerializers
    def update(self, request, *args, **kwargs):
        ord_id=kwargs['pk']
        data=json.loads(request.body)
        order_det=self.queryset.get(id=ord_id)
        order_det.actions(data)
        return Response({"quantity":order_det.quantity})


