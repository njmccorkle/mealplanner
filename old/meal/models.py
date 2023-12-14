from django.contrib.auth.models import User
from django.db import models

from base.models import MealPlannerBaseModel
from food.models import Course


# defines the meals that will be planned - supper, lunch, breakfast, dinner, etc
class Meal(MealPlannerBaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# assigns courses that should make up a meal
class MealItems(MealPlannerBaseModel):
    meal = models.ForeignKey(
        Meal, related_name="mealitems", on_delete=models.CASCADE, null=True
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.meal_id} - {self.course}"
