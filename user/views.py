import json

from django import forms
from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from order.models import *
from django.core.serializers import serialize
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

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
        user_name = register_form.data.get('user_name')
        password1 = register_form.data.get('password1')
        password2 = register_form.data.get('password2')
        telephone = register_form.data.get('telephone')
        student_id = register_form.data.get('student_id')

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
            user_name = login_form.data.get('user_name')
            password = login_form.data.get('password')
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
        food_id_list = request.POST.getlist("food_id")
        cnt_list = request.POST.getlist("cnt")
        if len(food_id_list) != len(cnt_list):
            return JsonResponse({"error": 2002, "msg": "food_id和cnt数量不一致"})

        new_order = Order()
        new_order.merchant_id = merchant_id
        new_order.user_id = user_id
        new_order.create_time = datetime.datetime.now()
        new_order.status = 0
        new_order.save()

        for food_id, cnt in zip(food_id_list, cnt_list):
            new_order_food = order_food()
            new_order_food.order_id = new_order.id
            new_order_food.food_id = food_id
            new_order_food.cnt = cnt
            new_order_food.save()

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
            content = comment_form.data.get('content')
            score = comment_form.data.get('score')

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
        user_id = request.POST.get("user_id")
        page_num = request.POST.get("page_num")
        page_size = request.POST.get("page_size")
        orders = Order.objects.filter(user_id=user_id).order_by('-create_time').values()
        paginator = Paginator(orders, page_size)

        try:
            current_page = paginator.page(page_num)
        except EmptyPage:
            return JsonResponse({"error": 2002, "msg": "无效的页码"})
        total = orders.count()
        current_orders = serialize('json', current_page.object_list)

        return JsonResponse({'error': 0,
                             'msg': '查看历史订单成功!',
                             'data': {
                                 "current_order": current_orders,
                                 "total": total
                             }
                             })
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 查看购物车
@csrf_exempt
def query_student_cart(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        page_num = request.POST.get("page_num")
        page_size = request.POST.get("page_size")
        carts = Cart.objects.filter(user_id=user_id).order_by('-add_time')
        paginator = Paginator(carts, page_size)
        try:
            current_page = paginator.page(page_num)
        except EmptyPage:
            return JsonResponse({"error": 2002, "msg": "无效的页码"})
        total = carts.count()
        current_carts = serialize('json', current_page.object_list)

        return JsonResponse({'error': 0,
                             'msg': '查看购物车成功!',
                             'data': {
                                 "current_carts": current_carts,
                                 "total": total
                             }
                             })
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 添加食品到购物车
@csrf_exempt
def new_cart_item(request):
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


# 查询学生个人信息
@csrf_exempt
def query_student_identity(request):
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        student = Student.objects.get(id=student_id)
        return JsonResponse({'error': 0,
                             'msg': '查看个人信息成功!',
                             'data': {
                                 "user_name": student.user_name,
                                 "building_id": student.building_id,
                                 "room_id": student.room_id,
                                 "telephone": student.telephone,
                                 "image": student.image
                             }
                             })
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 修改学生个人信息
@csrf_exempt
def change_student_identity(request):
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        student = Student.objects.get(id=student_id)
        student.user_name = request.POST.get("user_name")
        student.building_id = request.POST.get("building_id")
        student.room_id = request.POST.get("room_id")
        student.telephone = request.POST.get("telephone")
        student.image = request.POST.get("image")
        student.save()
        return JsonResponse({'error': 0, 'msg': '修改个人信息成功!'})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 获取商家选项
def get_merchants(request):
    if request.method == "POST":
        page_num = request.POST.get("page_num")
        page_size = request.POST.get("page_size")

        merchants = Merchant.objects.filter().order_by('id')
        paginator = Paginator(merchants, page_size)

        try:
            current_page = paginator.page(page_num)
        except EmptyPage:
            return JsonResponse({"error": 2002, "msg": "无效的页码"})
        total = merchants.count()
        # 获取当前页的类型数据
        current_merchants_json = serialize('json', current_page.object_list)
        current_merchants = json.loads(current_merchants_json)
        # print(current_types)
        # for item in current_foods:
        #     food_id = int(item['pk'])
        #     # 假设 Type 对象的主键是 'pk'
        #     # order_count = Order.objects.filter(food_id=food_id).count()
        #     order_count = order_food.objects.filter(food_id=food_id).count()
        #     item['fields']['order_count'] = order_count
        #     item['fields']['id'] = food_id
        return JsonResponse({"error": 0,
                             "data": {
                                 "current_page": current_merchants,
                                 "total_page": total
                             }})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


def get_all_merchants(request):
    if request.method == "POST":
        merchants = Merchant.objects.filter().order_by('id')
        for item in merchants:
            merchant_id = int(item['pk'])
            order_count = order_food.objects.filter(merchant_id=merchant_id).count()
            item['fields']['order_count'] = order_count
            item['fields']['id'] = merchant_id
        merchants = merchants.order_by('order_count')
        total = merchants.count()
        return JsonResponse({"error": 0,
                             "data": {
                                 "merchants": merchants,
                                 "total": total
                             }})
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
        user_name = register_form.data.get('user_name')
        password1 = register_form.data.get('password1')
        password2 = register_form.data.get('password2')
        telephone = register_form.data.get('telephone')

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
            user_name = login_form.data.get('user_name')
            password = login_form.data.get('password')
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
        page_num = request.POST.get("page_num")
        page_size = request.POST.get("page_size")
        orders = Order.objects.filter(rider_id=rider_id).order_by('-create_time').values()
        paginator = Paginator(orders, page_size)

        try:
            current_page = paginator.page(page_num)
        except EmptyPage:
            return JsonResponse({"error": 2002, "msg": "无效的页码"})
        total = orders.count()
        current_orders = serialize('json', current_page.object_list)

        return JsonResponse({'error': 0,
                             'msg': '查看骑手历史订单成功!',
                             'data': {
                                 "current_order": current_orders,
                                 "total": total
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
        user_name = register_form.data.get('user_name')
        password1 = register_form.data.get('password1')
        password2 = register_form.data.get('password2')
        telephone = register_form.data.get('telephone')

        repeated_name = Merchant.objects.filter(user_name=user_name)
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
    print(forms.Form)
    user_name = forms.CharField(label="账号", max_length=128, widget=forms.TextInput())
    password = forms.CharField(label="密码", max_length=128, widget=forms.PasswordInput())


@csrf_exempt
def merchant_login(request):
    if request.method == 'POST':
        login_form = MerchantLoginForm(request.POST)
        print(login_form)
        print("尝试登录")
        if login_form.is_valid():
            print(login_form.data.get("user_name") + "尝试登录")
            user_name = login_form.data.get("user_name")
            password = login_form.data.get("password")
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


# 商家获取餐品列表
@csrf_exempt
def get_foods(request):
    if request.method == "POST":
        merchant_id = request.POST.get("merchant_id")
        page_num = request.POST.get("page_num")
        page_size = request.POST.get("page_size")
        # print(merchant_id)
        foods = Food.objects.filter(merchant_id=merchant_id).order_by('id')
        paginator = Paginator(foods, page_size)

        try:
            current_page = paginator.page(page_num)
        except EmptyPage:
            return JsonResponse({"error": 2002, "msg": "无效的页码"})
        total = foods.count()
        # 获取当前页的类型数据
        # current_types = serialize('json', current_page.object_list)
        current_foods_json = serialize('json', current_page.object_list)
        current_foods = json.loads(current_foods_json)
        # print(current_types)
        for item in current_foods:
            food_id = int(item['pk'])
            # 假设 Type 对象的主键是 'pk'
            order_count = order_food.objects.filter(food_id=food_id).count()
            item['fields']['order_count'] = order_count
        return JsonResponse({"error": 0,
                             "data": {
                                 "current_page": current_foods,
                                 "total_page": total
                             }})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 商家添加菜品
@csrf_exempt
def add_food(request):
    if request.method == "POST":
        merchant_id = request.POST.get("merchant_id")
        name = request.POST.get("name")
        price = request.POST.get("price")
        type_id = request.POST.get("type_id")
        status = request.POST.get("status")

        if 'image' in request.FILES:
            image = request.FILES['image']
        else:
            image = None

        repeated_name = Food.objects.filter(name=name, merchant_id=merchant_id)
        if repeated_name.exists():
            return JsonResponse({"error": 4001, "msg": "菜品名已存在"})
        else:
            new_food = Food()
            new_food.merchant_id = merchant_id
            new_food.name = name
            new_food.price = price
            new_food.type_id = type_id
            new_food.status = status

            if image:
                # Save the file to the media root
                file_name = default_storage.save('food_images/' + image.name, ContentFile(image.read()))
                new_food.image = 'food_images/' + file_name

            new_food.save()
            return JsonResponse({"error": 0, "msg": "商家添加菜品成功"})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 商家获取标签列表
@csrf_exempt
def get_type(request):
    if request.method == "POST":
        merchant_id = request.POST.get("merchant_id")
        page_num = request.POST.get("page_num")
        page_size = request.POST.get("page_size")
        # print(merchant_id)
        types = Type.objects.filter(merchant_id=merchant_id).order_by('id')
        paginator = Paginator(types, page_size)

        try:
            current_page = paginator.page(page_num)
        except EmptyPage:
            return JsonResponse({"error": 2002, "msg": "无效的页码"})
        total = types.count()
        # 获取当前页的类型数据
        # current_types = serialize('json', current_page.object_list)
        current_types_json = serialize('json', current_page.object_list)
        current_types = json.loads(current_types_json)
        # print(current_types)
        for item in current_types:
            type_id = int(item['pk'])
            # 假设 Type 对象的主键是 'pk'
            food_count = Food.objects.filter(type_id=type_id).count()
            item['fields']['food_count'] = food_count
        return JsonResponse({"error": 0,
                             "data": {
                                 "current_page": current_types,
                                 "total_page": total
                             }})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 商家添加标签
@csrf_exempt
def add_type(request):
    if request.method == "POST":
        name = request.POST.get("name")
        merchant_id = request.POST.get("merchant_id")
        repeated_name = Type.objects.filter(name=name, merchant_id=merchant_id)
        if repeated_name.exists():
            return JsonResponse({'error': 4001, 'msg': '标签名已存在'})
        else:
            new_type = Type()
            new_type.name = name
            new_type.merchant_id = merchant_id
            new_type.save()
            return JsonResponse({"error": 0, "msg": "商家添加标签成功"})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


@csrf_exempt
def change_type_name(request):
    if request.method == "POST":
        name = request.POST.get("name")
        type_id = request.POST.get("type_id")
        type = Type.objects.filter(type_id=type_id)
        type.name = name
        type.save()
        return JsonResponse({"error": 0, "msg": "商家修改标签名成功"})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 商家删除标签
@csrf_exempt
def delete_type(request):
    if request.method == "POST":
        type_id = request.POST.get("type_id")
        type_ = Type.objects.filter(type_id=type_id)
        type_.delete()
        return JsonResponse({'error': 0, 'msg': '删除标签成功!'})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 商家修改菜品信息
@csrf_exempt
def change_food(request):
    if request.method == "POST":
        food_id = request.POST.get("food_id")
        food = Food.objects.get(id=food_id)
        name = request.POST.get("name")
        price = request.POST.get("price")
        type_id = request.POST.get("type_id")
        status = request.POST.get("status")
        food.name = name
        food.price = price
        food.type_id = type_id
        food.status = status
        food.save()
        return JsonResponse({"error": 0, "msg": "商家修改菜品信息成功"})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# 查询商家历史订单
@csrf_exempt
def query_merchant_history(request):
    if request.method == "POST":
        merchant_id = request.POST.get("merchant_id")
        page_num = request.POST.get("page_num")
        page_size = request.POST.get("page_size")
        orders = Order.objects.filter(merchant_id=merchant_id).order_by('-create_time').values()
        paginator = Paginator(orders, page_size)

        try:
            current_page = paginator.page(page_num)
        except EmptyPage:
            return JsonResponse({"error": 2002, "msg": "无效的页码"})
        total = orders.count()
        current_orders = serialize('json', current_page.object_list)

        return JsonResponse({'error': 0,
                             'msg': '查看商家历史订单成功!',
                             'data': {
                                 "current_order": current_orders,
                                 "total": total
                             }
                             })
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})


# Food

# 查询菜品历史评价
@csrf_exempt
def query_food_comments(request):
    if request.method == "POST":
        food_id = request.POST.get("food_id")
        page_num = request.POST.get("page_num")
        page_size = request.POST.get("page_size")

        order_foods = order_food.objects.filter(food_id=food_id).order_by('-create_time')

        comments = []
        for order_food_item in order_foods:
            comment = Comment.objects.filter(order_id=order_food_item.order_id).values()
            if comment.exists() and comment not in comments:
                comments.append(comment)

        paginator = Paginator(comments, page_size)

        try:
            current_page = paginator.page(page_num)
        except EmptyPage:
            return JsonResponse({"error": 2002, "msg": "无效的页码"})
        total = len(comments)

        current_comments = serialize('json', current_page)

        return JsonResponse({'error': 0,
                             'msg': '查看菜品历史评价成功!',
                             'data': {
                                 "current_comments": current_comments,
                                 "total": total
                             }
                             })
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})
