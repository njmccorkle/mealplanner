from django.contrib import admin

from .models import Meal, MealItems


class MealItemInlineAdmin(admin.TabularInline):
    model = MealItems


class MealAdmin(admin.ModelAdmin):
    inlines = [MealItemInlineAdmin]


admin.site.register(Meal, MealAdmin)
