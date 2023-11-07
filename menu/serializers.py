from rest_framework import serializers
from .models import Menu, MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"
        # fields = ("menu", "foodtype", "food")


class MenuSerializer(serializers.ModelSerializer):
    menu_itmes = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = "__all__"
        # fields = ("menu_date", "meal")
