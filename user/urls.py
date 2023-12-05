from django.urls import path
from .views import *

urlpatterns = [
    # Student
    path('student/register', student_register),
    path('student/login', student_login),
    path('student/order_add', order_add),
    path('student/order_complete', order_complete),
    path('student/order_comment', order_comment),
    path('student/order_complaint', order_complaint),
    path('student/history', query_student_history),
    path('student/cart', query_student_cart),
    path('student/add_cart', add_cart_item),
    path('student/delete_cart', delete_cart_item),
    path('student/change_cart', change_cart_cnt)
    # Merchant
]
