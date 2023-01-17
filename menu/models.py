from django.db import models
from django.contrib.auth.models import User
from base.models import MealPlannerBaseModel
from meal.models import Meal
from food.models import Food
from datetime import date
import calendar

# A meal for a given menu (day)
class Menu(MealPlannerBaseModel):
    menu_date = models.DateField()
    meal = models.ForeignKey(
        Meal, related_name="menu_meals", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        # day_name = calendar.day_name[self.menu_date.weekday()]
        return f"{self.meal_id}"


# The foods chosen for a meal on a menu
class MenuItem(MealPlannerBaseModel):
    menu = models.ForeignKey(
        Menu,
        related_name="foods",
        on_delete=models.CASCADE,
        null=True,
    )
    food = models.ForeignKey(
        Food, related_name="menu_foods", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return f"{self.food_id}"
