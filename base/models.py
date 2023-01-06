from django.db import models
from django.contrib.auth.models import User


# class MealPlannerBaseClass(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField(null=True, blank=True)
#     created_datetime = models.DateTimeField(auto_now_add=True)
#     modified_datetime = models.DateTimeField(auto_now=True)
#     created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
# modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Meal(models.Model):
    name = models.CharField(max_length=200)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # TODO: this should return a summary of the meal
    def __str__(self):
        return self.name


class MealType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # modified_by = models.ForeignKey(User)
    def __str__(self):
        return self.name


class MealTypeDefinition(models.Model):
    meal_type = models.ForeignKey(MealType, on_delete=models.SET_NULL, null=True)
    food_type = models.ForeignKey("FoodType", on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # modified_by = models.ForeignKey(User)
    def __str__(self):
        return f"{self.meal_type} - {self.food_type}"


class FoodType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # modified_by = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    food_type = models.ForeignKey(FoodType, on_delete=models.SET_NULL, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # modified_by = models.ForeignKey(User)

    def __str__(self):
        return self.name
