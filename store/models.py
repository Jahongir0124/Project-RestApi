from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    adress=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.user.__str__()
    @property
    def full_name(self):
        return self.user.first_name + '' + self.user.last_name
class Categories(models.Model):
    category_name=models.CharField(max_length=200,null=False)
    description=models.CharField(max_length=300,null=True)
    def __str__(self):
        return self.category_name
class Products(models.Model):
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=200,null=False)
    price=models.FloatField(null=False)
    image=models.ImageField(null=True)
    def __str__(self):
        return self.product_name
    @property
    def ImageURl(self):
            try:
                return self.image.url
            except:
                return ''
class Orders(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    order_date=models.DateTimeField(auto_now=True)
    status=models.CharField(default='start',max_length=30)
    delivered_date=models.DateTimeField(null=True)
    def __str__(self):
        return str(self.id) + self.status
class OrderDetails(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True)
    @property
    def get_total(self):
        return self.quantity * self.product.price
    def add(self,quantity=1):
        self.quantity+=1
        self.save()
    def sub(self,quantity=1):
        if self.quantity-1>0:
            self.quantity -= 1
        else:
            self.delete()
    def actions(self,data):
        if data['action']=='add':
            self.add(data['quantity'])
        else:
            self.sub()









