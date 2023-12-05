from django.contrib import admin
from .models import Food, Course


class FoodInlineAdmin(admin.TabularInline):
    model = Food


class CourseAdmin(admin.ModelAdmin):
    inlines = [FoodInlineAdmin]


admin.site.register(Course, CourseAdmin)
