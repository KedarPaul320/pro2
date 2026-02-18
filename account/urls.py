from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('product/',views.Prod,name='product'),
    path('customer/',views.customer,name='customer'),
    path('customer/<str:pk_test>/',views.customer,name='customer_detail'),
    path('tag/',views.tag,name='tag'),
]