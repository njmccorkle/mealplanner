from rest_framework import viewsets
from .serializers import CourseDefSerializer, FoodDefSerializer
from .models import CourseDef, FoodDef


class CourseDefViewSet(viewsets.ModelViewSet):
    queryset = CourseDef.objects.all()
    serializer_class = CourseDefSerializer


class FoodDefViewSet(viewsets.ModelViewSet):
    queryset = FoodDef.objects.all()
    serializer_class = FoodDefSerializer
