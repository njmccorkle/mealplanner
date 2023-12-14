from django.contrib import admin

from .models import Course, Food, Meal


class FoodAdmin(admin.ModelAdmin):
    model = Food


class FoodInlineAdmin(admin.TabularInline):
    model = Food


class CourseAdmin(admin.ModelAdmin):
    inlines = [FoodInlineAdmin]


class MealAdmin(admin.ModelAdmin):
    model = Meal


admin.site.register(Food, FoodAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Meal, MealAdmin)
