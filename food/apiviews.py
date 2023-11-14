from rest_framework import viewsets, permissions
from .serializers import FoodTypeSerializer, FoodSerializer
from .models import FoodType, Food


class FoodTypeViewSet(viewsets.ModelViewSet):
    queryset = FoodType.objects.all().order_by("name")
    serializer_class = FoodTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticated]
