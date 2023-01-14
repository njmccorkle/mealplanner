from django.contrib import admin
from .models import Food, FoodType

# from .models import Meal, MealType, MealTypeDefinition

# admin.site.register(Food)
# admin.site.register(FoodType)


class FoodInlineAdmin(admin.TabularInline):
    model = Food


class FoodTypeAdmin(admin.ModelAdmin):
    inlines = [FoodInlineAdmin]


admin.site.register(FoodType, FoodTypeAdmin)
