from rest_framework import serializers

from .models import Course, Food, Meal


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"
        # fields = ("name", "description", "foodtype")


class CourseSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"
        # fields = ("name", "description", "foods")


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"
        # fields = ("name", "description")
