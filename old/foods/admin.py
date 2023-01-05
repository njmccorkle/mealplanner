from django.contrib import admin

# Register your models here.
from .models import Food, FoodType

admin.site.register(Food)
admin.site.register(FoodType)
