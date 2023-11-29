from rest_framework import serializers
from .models import CourseDef, FoodDef


class FoodDefSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodDef
        fields = "__all__"
        # fields = ("name", "description", "foodtype")


class CourseDefSerializer(serializers.ModelSerializer):
    foods = FoodDefSerializer(many=True, read_only=True)

    class Meta:
        model = CourseDef
        fields = "__all__"
        # fields = ("name", "description", "foods")
