from django.urls import path
from .views import *

urlpatterns = [
    path('register', register),
    path('login', login),
    path("order_add", order_add)
]
