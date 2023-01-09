from django.db import models
from django.contrib.auth.models import User
from base.models import MealPlannerBaseModel
from meal.models import Meal
from food.models import Food
from datetime import date
import calendar

# Represents a the food for a single day
class Menu(MealPlannerBaseModel):
    menu_date = models.DateField()

    def get_menu_day_text(self):
        return calendar.day_name[self.menu_date.weekday()]

    def __str__(self):
        # return self.menu_date.strftime(f"{self.get_menu_day_text()}, %B %-d, %Y")
        return self.menu_date.strftime(f"%A, %B %d, %Y")

    class Meta:
        ordering = ["menu_date"]


# A meal for a given menu (dSay)
class MenuMeal(MealPlannerBaseModel):
    menu_id = models.ForeignKey(
        Menu, related_name="meals", on_delete=models.CASCADE, null=True
    )
    meal_id = models.ForeignKey(
        Meal, related_name="menu_meals", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        # day_name = calendar.day_name[self.menu_date.weekday()]
        return f"{self.meal_id}"


# The foods chosen for a meal on a menu
class MenuMealItem(MealPlannerBaseModel):
    menu_meal_id = models.ForeignKey(
        MenuMeal, related_name="foods", on_delete=models.CASCADE, null=True
    )
    food_id = models.ForeignKey(
        Food, related_name="menu_foods", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return f"{self.food_id}"
