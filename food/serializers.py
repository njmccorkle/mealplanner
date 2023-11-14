from rest_framework import serializers
from .models import FoodType, Food


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        # fields = "__all__"
        fields = ("name", "description", "foodtype")


class FoodTypeSerializer(serializers.HyperlinkedModelSerializer):
    # foods = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = FoodType
        # fields = "__all__"
        fields = ("name", "description", "foods")
