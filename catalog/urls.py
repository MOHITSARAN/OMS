from django.conf.urls import url
from catalog.views import *
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('create_order/', login_required(order), name='order'),
    path('view_order/', login_required(view_order), name='order'),
    path('create_product/', login_required(product), name='product'),
    path('view_product/', login_required(view_product), name='product'),
    path('create_customer/', login_required(customer), name='customer'),
    path('view_customer/', login_required(view_customer), name='customer')
]
