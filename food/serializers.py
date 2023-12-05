from rest_framework import serializers
from .models import Course, FoodDef


class FoodDefSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodDef
        fields = "__all__"
        # fields = ("name", "description", "foodtype")


class CourseSerializer(serializers.ModelSerializer):
    foods = FoodDefSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"
        # fields = ("name", "description", "foods")
