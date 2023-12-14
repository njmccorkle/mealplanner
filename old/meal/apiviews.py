from rest_framework import viewsets

from .models import Meal, MealItems
from .serializers import MealItemSerializer, MealSerializer


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class MealItemViewSet(viewsets.ModelViewSet):
    queryset = MealItems.objects.all()
    serializer_class = MealItemSerializer
