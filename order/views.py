from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def test(request):
    if request.method == "POST":

        return JsonResponse({"error": 0, "msg": "成功"})
    else:
        return JsonResponse({"error": 2001, "msg": "请求方式错误"})