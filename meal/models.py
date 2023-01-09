from django.db import models
from django.contrib.auth.models import User
from food.models import FoodType


class Meal(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # modified_by = models.ForeignKey(User)
    def __str__(self):
        return self.name


class MealDefinition(models.Model):
    meal_id = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True)
    food_type = models.ForeignKey(FoodType, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # modified_by = models.ForeignKey(User)
    def __str__(self):
        return f"{self.meal_id} - {self.food_type}"
