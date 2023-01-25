from django.db import models
from base.models import MealPlannerBaseModel
from meal.models import Meal
from food.models import Food, FoodType
import calendar

# A meal for a given menu (day)
class Menu(MealPlannerBaseModel):
    menu_date = models.DateField()
    meal = models.ForeignKey(
        Meal, related_name="menu_meals", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        day_name = calendar.day_name[self.menu_date.weekday()]
        month_name = calendar.month_name[self.menu_date.month]
        day = self.menu_date.day
        year = self.menu_date.year
        return f"{self.meal} - {day_name}, {month_name} {day}, {year}"

        # return f"{self.meal_id}"

    # def get_title(self):


# The foods chosen for a meal on a menu
class MenuItem(MealPlannerBaseModel):
    menu = models.ForeignKey(
        Menu,
        related_name="menuitems",
        on_delete=models.CASCADE,
        null=True,
    )
    foodtype = models.ForeignKey(FoodType, on_delete=models.CASCADE, null=True)
    food = models.ForeignKey(
        Food, related_name="food", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return f"{self.food}"
