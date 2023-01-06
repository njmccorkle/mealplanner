from django.contrib import admin
from .models import Food, FoodType
from .models import Meal, MealType, MealTypeDefinition

admin.site.register(Food)
admin.site.register(FoodType)
admin.site.register(Meal)
admin.site.register(MealType)
admin.site.register(MealTypeDefinition)
