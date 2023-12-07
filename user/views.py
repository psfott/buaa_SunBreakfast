from django import forms
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from order.models import *

import re

from user.models import Student


class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput())
    password1 = forms.CharField(label="密码", max_length=128, widget=forms.PasswordInput())
    password2 = forms.CharField(label="确认密码", max_length=128, widget=forms.PasswordInput())
    telephone = forms.CharField(label="联系电话", widget=forms.TextInput())
    studentId = forms.CharField(label="学号", max_length=128, widget=forms.TextInput())


class LoginForm(forms.Form):
    userName = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput())
    password = forms.CharField(label="密码", max_length=128, widget=forms.PasswordInput())


@csrf_exempt
def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        # if register_form.is_valid():
        print(register_form)
        user_name = register_form.cleaned_data.get('userName')
        password1 = register_form.cleaned_data.get('password1')
        password2 = register_form.cleaned_data.get('password2')
        telephone = register_form.cleaned_data.get('telephone')
        student_id = register_form.cleaned_data.get('studentId')

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

        # token = create_token(username)
        return JsonResponse({'error': 0,
                             'msg': '注册成功!',
                             'data': {
                                 'userid': new_student.id,
                                 'username': new_student.user_name,
                                 # 'authorization': token,
                                 'telephone': new_student.telephone,
                                 'student_id': new_student.student_id
                             }
                             })

    else:
        return JsonResponse({'error': 2001, 'msg': '请求方式错误'})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        print("登录111")
        print(login_form)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('userName')
            password = login_form.cleaned_data.get('password')
            print(username)
            try:
                student = Student.objects.get(user_name=username)
            except:
                return JsonResponse({'error': 4001, 'msg': '用户名不存在'})
            if student.userPassword != password:
                return JsonResponse({'error': 4002, 'msg': '密码错误'})

            # token = create_token(username)
            return JsonResponse({
                'error': 0,
                'msg': "登录成功!",
                'data': {
                    'userid': student.userId,
                    'username': student.user_name,
                    # 'authorization': token,
                    'student_id': student.student_id,
                    'telephone': student.telephone
                }
            })
        else:
            return JsonResponse({'error': 3001, 'msg': '表单信息验证失败'})

    else:
        return JsonResponse({'error': 2001, 'msg': '请求方式错误'})


@csrf_exempt
# 下单
def order_add(request):
    if request.method == "POST":
        user_id = request.POST.get("userid")
        merchant_id = request.POST.get("merchant_id")
        food_id = request.POST.get("food_id")

        new_order = Order()
        new_order.merchant_id = merchant_id
        new_order.user_id = user_id
        new_order.food_id = food_id
        # new_order.create_time = datetime.now()
        new_order.status = False
        new_order.save()
        return JsonResponse({"error": 0, "msg": "下单成功"})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})
