from django.contrib import admin
from .models import FoodDef, CourseDef


class FoodDefInlineAdmin(admin.TabularInline):
    model = FoodDef

class CourseDefAdmin(admin.ModelAdmin):
    inlines = [FoodDefInlineAdmin]

admin.site.register(CourseDef, CourseDefAdmin)
