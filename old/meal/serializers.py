from rest_framework import serializers

from .models import Meal, MealItems


class MealItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealItems
        fields = "__all__"
        # fields = ("name", "foodtype", "quantityt")


class MealSerializer(serializers.ModelSerializer):
    mealitems = MealItemSerializer(many=True, read_only=True)

    class Meta:
        model = Meal
        fields = "__all__"
        # fields = ("name", "description")
