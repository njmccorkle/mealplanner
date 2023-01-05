from django.db import models
from django.utils import timezone


class FoodType(models.Model):
    name = models.CharField(max_length=200)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=200)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
