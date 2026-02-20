from django.urls import path
from . import views

urlpatterns = [
    # Dashboard and Product
    path('',views.home,name='home'),
    path('product/',views.Prod,name='product'),
    path('customer/',views.customer,name='customer'),
    path('customer/<str:pk_test>/',views.customer,name='customer_detail'),
    # Order Operations
    path('create_order/',views.createOrder,name='create_order'),
    path('update_order/<str:pk>/',views.updateOrder,name='update_order'),   
    path('delete_order/<str:pk>/',views.deleteOrder,name='delete_order'),
    # Customer Operations
    path('create_customer/',views.create_customer,name='create_customer'),
    path('customer_list/',views.Customer_list,name='customer_list'),
    path('update_customer/<str:pk>/',views.update_customer,name='update_customer'),
    path('delete_customer/<str:pk>/',views.delete_customer,name='delete_customer'),
    path('place_order/<str:pk>/',views.placeOrder,name='place_order'),

    # Product Operations
    path('add_product/',views.add_product,name='add_product'),

    # Tag Operations
    path('tag/',views.tag,name='tag'),
]