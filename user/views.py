from django import forms
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from order.models import *

import re
import datetime
from utils.token import create_token
from user.models import *


# Student

class StudentRegisterForm(forms.Form):
    user_name = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput())
    password1 = forms.CharField(label="密码", max_length=128, widget=forms.PasswordInput())
    password2 = forms.CharField(label="确认密码", max_length=128, widget=forms.PasswordInput())
    telephone = forms.CharField(label="联系电话", max_length=128, widget=forms.TextInput())
    student_id = forms.CharField(label="学号", max_length=128, widget=forms.TextInput())


@csrf_exempt
def student_register(request):
    if request.method == 'POST':
        register_form = StudentRegisterForm(request.POST)
        # if register_form.is_valid():
        print(register_form)
        user_name = register_form.cleaned_data.get('user_name')
        password1 = register_form.cleaned_data.get('password1')
        password2 = register_form.cleaned_data.get('password2')
        telephone = register_form.cleaned_data.get('telephone')
        student_id = register_form.cleaned_data.get('student_id')

        repeated_name = Student.objects.filter(user_name=user_name)
        if repeated_name.exists():
            return JsonResponse({'error': 4001, 'msg': '用户名已存在'})

        repeated_student_id = Student.objects.filter(student_id=student_id)
        if repeated_student_id.exists():
            return JsonResponse({'error': 4002, 'msg': '学号已存在'})
        # 检测两次密码是否一致
        if password1 != password2:
            return JsonResponse({'error': 4003, 'msg': '两次输入的密码不一致'})
        # 检测密码不符合规范：8-18，英文字母+数字
        if not re.match('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,18}$', password1):
            return JsonResponse({'error': 4004, 'msg': '密码不符合规范'})

        new_student = Student()
        new_student.user_name = user_name
        new_student.password = password1
        new_student.student_id = student_id
        new_student.telephone = telephone

        new_student.save()

        token = create_token(user_name)
        return JsonResponse({'error': 0,
                             'msg': '注册成功!',
                             'data': {
                                 'userid': new_student.id,
                                 'username': new_student.user_name,
                                 'authorization': token,
                                 'telephone': new_student.telephone,
                                 'student_id': new_student.student_id
                             }
                             })

    else:
        return JsonResponse({'error': 2001, 'msg': '请求方式错误'})


class StudentLoginForm(forms.Form):
    user_name = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput())
    password = forms.CharField(label="密码", max_length=128, widget=forms.PasswordInput())


@csrf_exempt
def student_login(request):
    if request.method == 'POST':
        login_form = StudentLoginForm(request.POST)
        print("登录111")
        print(login_form)
        if login_form.is_valid():
            user_name = login_form.cleaned_data.get('user_name')
            password = login_form.cleaned_data.get('password')
            print(user_name)
            try:
                student = Student.objects.get(user_name=user_name)
            except:
                return JsonResponse({'error': 4001, 'msg': '学生不存在'})
            if student.password != password:
                return JsonResponse({'error': 4002, 'msg': '密码错误'})

            token = create_token(user_name)
            return JsonResponse({
                'error': 0,
                'msg': "登录成功!",
                'data': {
                    'userid': student.id,
                    'username': student.user_name,
                    'authorization': token,
                    'student_id': student.student_id,
                    'telephone': student.telephone
                }
            })
        else:
            return JsonResponse({'error': 3001, 'msg': '表单信息验证失败'})

    else:
        return JsonResponse({'error': 2001, 'msg': '请求方式错误'})


# 下单
@csrf_exempt
def order_add(request):
    if request.method == "POST":
        user_id = request.POST.get("userid")
        merchant_id = request.POST.get("merchant_id")
        food_id = request.POST.get("food_id")

        new_order = Order()
        new_order.merchant_id = merchant_id
        new_order.user_id = user_id
        new_order.food_id = food_id
        new_order.create_time = datetime.datetime.now()
        new_order.status = 0
        new_order.save()
        return JsonResponse({"error": 0, "msg": "下单成功"})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 订单完成
@csrf_exempt
def order_complete(request):
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        order = Order.objects.get(id=order_id)
        order.status = True
        order.arrive_time = datetime.datetime.now()
        order.save()
        return JsonResponse({"error": 0, "msg": "订单完成"})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 订单评论
class OrderComment(forms.Form):
    content = forms.CharField(label="评论内容", widget=forms.TextInput())
    score = forms.IntegerField(label="评分", widget=forms.NumberInput())
    # images = forms.ImageField(label="上传图片", widget=forms.MultipleFileInput(attrs={'multiple': True}),
    #                           required=False)


@csrf_exempt
def order_comment(request):
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        order = Order.objects.get(id=order_id)
        comment_form = OrderComment(request.POST, request.FILES)

        if comment_form.is_valid():
            content = comment_form.cleaned_data.get('content')
            score = comment_form.cleaned_data.get('score')

            new_comment = Comment.objects.create(order_id=order_id, user_id=order.user_id, content=content, score=score)

            # 处理多张图片的上传
            # images = request.FILES.getlist('images')
            # for image in images:
            #     Comment_Image.objects.create(comment_id=new_comment.id, image=image)

            order.comment_id = new_comment.id
            order.save()

            return JsonResponse({'error': 0, 'msg': '评论成功!',
                                 'data': {'comment_id': new_comment.id, 'content': new_comment.content,
                                          'score': new_comment.score}})
        else:
            return JsonResponse({'error': 2003, 'msg': '表单数据验证失败'})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 对订单进行投诉
@csrf_exempt
def order_complaint(request):
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        content = request.POST.get("content")
        new_complaint = Complaint()
        new_complaint.order_id = order_id
        new_complaint.time = datetime.datetime.now()
        new_complaint.content = content
        new_complaint.save()
        return JsonResponse({'error': 0,
                             'msg': '投诉成功!',
                             'data': {
                                 'complaint_id': new_complaint.id,
                                 'content': new_complaint.content,
                                 'time': new_complaint.time
                             }
                             })
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 查询学生历史订单
@csrf_exempt
def query_student_history(request):
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        results = list(Order.objects.filter(user_id=student_id).order_by('-create_time').values())
        return JsonResponse({'error': 0,
                             'msg': '查看历史订单成功!',
                             'data': {
                                 "results": results
                             }
                             })
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 查看购物车
@csrf_exempt
def query_student_cart(request):
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        results = list(Cart.objects.filter(user_id=student_id).order_by('-add_time').values())
        return JsonResponse({'error': 0,
                             'msg': '查看购物车成功!',
                             'data': {
                                 "results": results
                             }
                             })
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 添加食品到购物车
@csrf_exempt
def add_cart_item(request):
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        food_id = request.POST.get("food_id")  # 默认为1

        # 检查购物车中是否已存在相同食品
        cart_item = Cart.objects.filter(user_id=student_id, food_id=food_id).first()

        if cart_item:
            cart_item.cnt += 1
            cart_item.add_time = datetime.datetime.now()
            cart_item.save()
        else:
            # 如果不存在相同食品，创建新的购物车项
            new_cart_item = Cart(user_id=student_id, food_id=food_id)
            new_cart_item.save()

        return JsonResponse({'error': 0, 'msg': '添加购物车成功!'})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 在购物车中修改份数
@csrf_exempt
def change_cart_cnt(request):
    if request.method == "POST":
        cart_id = request.POST.get("cart_id")
        cnt = request.POST.get("cnt")
        cart_item = Cart.objects.filter(cart_id=cart_id)
        cart_item.cnt += cnt
        if cart_item.cnt <= 0:
            cart_item.delete()
        return JsonResponse({'error': 0, 'msg': '修改购物车次数成功!'})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 在购物车中删除项
@csrf_exempt
def delete_cart_item(request):
    if request.method == "POST":
        cart_id = request.POST.get("cart_id")

        # 检查购物车中是否存在指定的食品项
        cart_item = Cart.objects.filter(cart_id=cart_id)
        cart_item.delete()
        return JsonResponse({'error': 0, 'msg': '删除购物车项成功!'})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# Rider
class RiderRegisterForm(forms.Form):
    user_name = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput())
    password1 = forms.CharField(label="密码", max_length=128, widget=forms.PasswordInput())
    password2 = forms.CharField(label="确认密码", max_length=128, widget=forms.PasswordInput())
    telephone = forms.CharField(label="联系电话", max_length=128, widget=forms.TextInput())


@csrf_exempt
def rider_register(request):
    if request.method == 'POST':
        register_form = RiderRegisterForm(request.POST)
        # if register_form.is_valid():
        print(register_form)
        user_name = register_form.cleaned_data.get('userName')
        password1 = register_form.cleaned_data.get('password1')
        password2 = register_form.cleaned_data.get('password2')
        telephone = register_form.cleaned_data.get('telephone')

        repeated_name = Rider.objects.filter(user_name=user_name)
        if repeated_name.exists():
            return JsonResponse({'error': 4001, 'msg': '棋手名已存在'})
        # 检测两次密码是否一致
        if password1 != password2:
            return JsonResponse({'error': 4003, 'msg': '两次输入的密码不一致'})
        # 检测密码不符合规范：8-18，英文字母+数字
        if not re.match('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,18}$', password1):
            return JsonResponse({'error': 4004, 'msg': '密码不符合规范'})

        new_rider = Rider()
        new_rider.user_name = user_name
        new_rider.password = password1
        new_rider.telephone = telephone

        new_rider.save()

        token = create_token(user_name)
        return JsonResponse({'error': 0,
                             'msg': '注册成功!',
                             'data': {
                                 'userid': new_rider.id,
                                 'username': new_rider.user_name,
                                 'authorization': token,
                                 'telephone': new_rider.telephone
                             }
                             })

    else:
        return JsonResponse({'error': 2001, 'msg': '请求方式错误'})


class RiderLoginForm(forms.Form):
    user_name = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput())
    password = forms.CharField(label="密码", max_length=128, widget=forms.PasswordInput())


@csrf_exempt
def rider_login(request):
    if request.method == 'POST':
        login_form = RiderLoginForm(request.POST)
        print("登录111")
        print(login_form)
        if login_form.is_valid():
            user_name = login_form.cleaned_data.get('user_name')
            password = login_form.cleaned_data.get('password')
            print(user_name)
            try:
                rider = Rider.objects.get(user_name=user_name)
            except:
                return JsonResponse({'error': 4001, 'msg': '骑手不存在'})
            if rider.password != password:
                return JsonResponse({'error': 4002, 'msg': '密码错误'})

            token = create_token(user_name)
            return JsonResponse({
                'error': 0,
                'msg': "登录成功!",
                'data': {
                    'userid': rider.id,
                    'username': rider.user_name,
                    'authorization': token,
                    'telephone': rider.telephone
                }
            })
        else:
            return JsonResponse({'error': 3001, 'msg': '表单信息验证失败'})

    else:
        return JsonResponse({'error': 2001, 'msg': '请求方式错误'})


# 骑手接单
@csrf_exempt
def order_get_rider(request):
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        rider_id = request.POST.get("rider_id")
        order = Order.objects.get(order_id=order_id)
        order.rider_id = rider_id
        order.ride_time = datetime.datetime.now()
        order.status = 2
        order.save()
        return JsonResponse({"error": 0, "msg": "骑手接单成功"})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 骑手订单送达
@csrf_exempt
def order_complete_rider(request):
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        order = Order.objects.get(order_id=order_id)
        order.status = 3
        order.save()
        return JsonResponse({"error": 0, "msg": "骑手已送达"})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 查询骑手历史订单
@csrf_exempt
def query_rider_history(request):
    if request.method == "POST":
        rider_id = request.POST.get("rider_id")
        results = list(Order.objects.filter(rider_id=rider_id).order_by('-create_time').values())
        return JsonResponse({'error': 0,
                             'msg': '查看骑手历史订单成功!',
                             'data': {
                                 "results": results
                             }
                             })
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# Merchant
class MerchantRegisterForm(forms.Form):
    user_name = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput())
    password1 = forms.CharField(label="密码", max_length=128, widget=forms.PasswordInput())
    password2 = forms.CharField(label="确认密码", max_length=128, widget=forms.PasswordInput())
    telephone = forms.CharField(label="联系电话", max_length=128, widget=forms.TextInput())


@csrf_exempt
def merchant_register(request):
    if request.method == 'POST':
        register_form = MerchantRegisterForm(request.POST)
        # if register_form.is_valid():
        print(register_form)
        user_name = register_form.cleaned_data.get('userName')
        password1 = register_form.cleaned_data.get('password1')
        password2 = register_form.cleaned_data.get('password2')
        telephone = register_form.cleaned_data.get('telephone')

        repeated_name = Student.objects.filter(user_name=user_name)
        if repeated_name.exists():
            return JsonResponse({'error': 4001, 'msg': '商户名已存在'})
        # 检测两次密码是否一致
        if password1 != password2:
            return JsonResponse({'error': 4003, 'msg': '两次输入的密码不一致'})
        # 检测密码不符合规范：8-18，英文字母+数字
        if not re.match('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,18}$', password1):
            return JsonResponse({'error': 4004, 'msg': '密码不符合规范'})

        new_merchant = Merchant()
        new_merchant.user_name = user_name
        new_merchant.password = password1
        new_merchant.telephone = telephone

        new_merchant.save()

        token = create_token(user_name)
        return JsonResponse({'error': 0,
                             'msg': '注册成功!',
                             'data': {
                                 'userid': new_merchant.id,
                                 'username': new_merchant.user_name,
                                 'authorization': token,
                                 'telephone': new_merchant.telephone
                             }
                             })

    else:
        return JsonResponse({'error': 2001, 'msg': '请求方式错误'})


class MerchantLoginForm(forms.Form):
    user_name = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput())
    password = forms.CharField(label="密码", max_length=128, widget=forms.PasswordInput())


@csrf_exempt
def merchant_login(request):
    if request.method == 'POST':
        login_form = MerchantLoginForm(request.POST)
        print("登录111")
        print(login_form)
        if login_form.is_valid():
            user_name = login_form.cleaned_data.get('user_name')
            password = login_form.cleaned_data.get('password')
            print(user_name)
            try:
                merchant = Merchant.objects.get(user_name=user_name)
            except:
                return JsonResponse({'error': 4001, 'msg': '商家不存在'})
            if merchant.password != password:
                return JsonResponse({'error': 4002, 'msg': '密码错误'})

            token = create_token(user_name)
            return JsonResponse({
                'error': 0,
                'msg': "登录成功!",
                'data': {
                    'userid': merchant.id,
                    'username': merchant.user_name,
                    'authorization': token,
                    'telephone': merchant.telephone
                }
            })
        else:
            return JsonResponse({'error': 3001, 'msg': '表单信息验证失败'})

    else:
        return JsonResponse({'error': 2001, 'msg': '请求方式错误'})


# 商家接单
@csrf_exempt
def order_get_merchant(request):
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        merchant_id = request.POST.get("merchant_id")
        order = Order.objects.get(order_id=order_id)
        order.merchant_id = merchant_id
        order.status = 1
        order.save()
        return JsonResponse({"error": 0, "msg": "商家接单成功"})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 商家添加菜品
@csrf_exempt
def add_food(request):
    if request.method == "POST":
        merchant_id = request.POST.get("merchant_id")
        name = request.POST.get("name")
        price = request.POST.get("price")
        type = request.POST.get("type")
        new_food = Food()
        new_food.merchant_id = merchant_id
        new_food.name = name
        new_food.price = price
        new_food.type = type
        new_food.save()
        return JsonResponse({"error": 0, "msg": "商家添加菜品成功"})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})
