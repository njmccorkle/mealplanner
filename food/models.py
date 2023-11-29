from django.db import models
from django.contrib.auth.models import User
from base.models import MealPlannerBaseModel


class CourseDef(MealPlannerBaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class FoodDef(MealPlannerBaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey(
        CourseDef, related_name="foods", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name
