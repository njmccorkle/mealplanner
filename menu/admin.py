from django.contrib import admin

# from .models import Menu, MenuItem
from .models import Menu, MenuMeal, MenuMealItem

admin.site.register(Menu)
admin.site.register(MenuMeal)
admin.site.register(MenuMealItem)
