from django.db import models
from django.contrib.auth.models import User
from food.models import CourseDef
from base.models import MealPlannerBaseModel


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
    course = models.ForeignKey(CourseDef, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.meal_id} - {self.course}"
