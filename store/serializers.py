from rest_framework import serializers
from .models import *
class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields = "__all__"
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields = "__all__"
class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields = "__all__"
class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields = "__all__"
class OrederDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model=OrderDetails
        fields = "__all__"
class OrderDetailsActionSerializer(serializers.Serializer):
    action=serializers.CharField(max_length=10)