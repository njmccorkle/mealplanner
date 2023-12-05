from rest_framework import viewsets
from .serializers import CourseSerializer, FoodDefSerializer
from .models import Course, FoodDef


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class FoodDefViewSet(viewsets.ModelViewSet):
    queryset = FoodDef.objects.all()
    serializer_class = FoodDefSerializer
