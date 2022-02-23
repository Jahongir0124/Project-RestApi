from rest_framework import routers
from store import views
from employee.views import *
from moderator.views import *
router=routers.DefaultRouter()
router.register(r'customer',views.UserViewset,basename='customer')
router.register(r'category',views.CategoryViewset,basename='category')
router.register(r'product',views.ProductViewset,basename='product')
router.register(r'product_by',views.ProductByCategoryViewset,basename='product_by')
router.register(r'order',views.OrderViewset,basename='order')
router.register(r'ord_detail',views.OrderDetaisViewset,basename='ord_detail')
router.register(r'ord_detail_update',views.OrderDetaisActionViewset,basename='ord_detail_update')
router.register(r'employee',EmployeeViewsets,basename='employee')
router.register(r'moderator',ModeratorViewsets,basename='moderator')
