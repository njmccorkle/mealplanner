from rest_framework import viewsets
from .serializers import MealSerializer, MealItemSerializer
from .models import Meal, MealItems


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class MealItemViewSet(viewsets.ModelViewSet):
    queryset = MealItems.objects.all()
    serializer_class = MealItemSerializer
