from django.contrib import admin

from .models import Menu, MenuItem


class MenuItemInlineAdmin(admin.TabularInline):
    model = MenuItem
    fk_name = "menu"


class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInlineAdmin]


admin.site.register(Menu, MenuAdmin)
