from django.db import models
from django.contrib.auth.models import User
from base.models import MealPlannerBaseModel


class FoodType(MealPlannerBaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Food(MealPlannerBaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    foodtype = models.ForeignKey(
        FoodType, related_name="foods", on_delete=models.SET_NULL, null=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
