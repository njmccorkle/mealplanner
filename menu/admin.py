from django.contrib import admin

from .models import Menu, MenuItem


class MenuItemInlineAdmin(admin.TabularInline):
    model = MenuItem
    fk_name = "the_menu"


class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInlineAdmin]


admin.site.register(Menu, MenuAdmin)
