from django.contrib import admin
from .models import Food, FoodType


class FoodInlineAdmin(admin.TabularInline):
    model = Food


class FoodTypeAdmin(admin.ModelAdmin):
    inlines = [FoodInlineAdmin]


admin.site.register(FoodType, FoodTypeAdmin)
