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

    def __str__(self):
        day_name = calendar.day_name[self.menu_date.weekday()]
        return self.menu_date.strftime(f"%d %B, %Y - {day_name}")


class MenuItem(MealPlannerBaseModel):
    menu_id = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    meal_id = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True)
    food_id = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
