from rest_framework import viewsets
from .serializers import FoodTypeSerializer, FoodSerializer
from .models import FoodType, Food


class FoodTypeViewSet(viewsets.ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
