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
    path('student/new_cart', new_cart_item),
    path('student/delete_cart', delete_cart_item),
    path('student/change_cart', change_cart_cnt),
    path('student/identity', query_student_identity),
    path('student/identity_change', change_student_identity),
    path('student/get_merchants', get_merchants),
    # Rider
    path('Rider/register', rider_register),
    path('Rider/login', rider_login),
    path('Rider/order_get', order_get_rider),
    path('Rider/order_complete', order_complete_rider),
    path('Rider/history', query_rider_history),
    # Merchant
    path('Merchant/register', merchant_register),
    path('Merchant/login', merchant_login),
    path('Merchant/order_get', order_get_merchant),
    path('Merchant/add_food', add_food),
    path('Merchant/get_foods', get_foods),
    path('Merchant/change_food', change_food),
    path('Merchant/get_types', get_type),
    path('Merchant/add_type', add_type),
    path('Merchant/change_type', change_type_name),
    path('Merchant/delete_type', delete_type),
    path('Merchant/history', query_merchant_history),
    # Food
    path('Food/comment_history', query_food_comments)
]
