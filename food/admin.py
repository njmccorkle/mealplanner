from django.contrib import admin
from .models import FoodDef, Course


class FoodDefInlineAdmin(admin.TabularInline):
    model = FoodDef


class CourseAdmin(admin.ModelAdmin):
    inlines = [FoodDefInlineAdmin]


admin.site.register(Course, CourseAdmin)
