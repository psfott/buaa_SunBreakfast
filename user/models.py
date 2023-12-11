from django.db import models


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    student_id = models.CharField(max_length=128)
    building_id = models.CharField(max_length=128)
    room_id = models.CharField(max_length=128)
    telephone = models.CharField(max_length=128)
    image = models.ImageField(upload_to='student_images/', null=True, blank=True)

    class Meta:
        db_table = "students"


class Merchant(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    telephone = models.CharField(max_length=128)
    score = models.FloatField(default=5)
    average = models.FloatField(default=0)
    image = models.ImageField(upload_to='merchant_images/', null=True, blank=True)

    class Meta:
        db_table = "merchants"


class Rider(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    telephone = models.CharField(max_length=128)

    class Meta:
        db_table = "riders"


class Food(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    merchant_id = models.IntegerField(default=0)
    score = models.FloatField(default=0)
    price = models.FloatField(default=0)
    type_id = models.IntegerField(default=0)
    image = models.ImageField(upload_to='food_images/', null=True, blank=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "foods"


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, default="")
    merchant_id = models.IntegerField(default=0)

    class Meta:
        db_table = "types"
