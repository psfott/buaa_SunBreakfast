import datetime

from django.db import models


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default="0")
    rider_id = models.IntegerField(default="0")
    comment_id = models.IntegerField(default="0")
    merchant_id = models.IntegerField(default="0")
    # 下单时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 送达时间
    arrive_time = models.DateTimeField(default=datetime.datetime.now())
    # 开始配送时间
    ride_time = models.DateTimeField(default=datetime.datetime.now())
    # 交易完成状态
    status = models.BooleanField(default=False)

    class Meta:
        db_table = "orders"


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default="0")
    order_id = models.IntegerField(default="0")
    content = models.TextField(default="")
    # 评分
    score = models.IntegerField(default="0")

    class Meta:
        db_table = "comments"


# 投诉
class Complaint(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(default="")
    time = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = "complaints"


class History(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="0")
    price = models.FloatField(default="0")

    class Meta:
        db_table = "histories"


class order_food(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=0)
    food_id = models.IntegerField(default=0)
    cnt = models.IntegerField(default=0)

    class Meta:
        db_table = "order_foods"
