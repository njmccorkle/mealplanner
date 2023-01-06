from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodType

# foodtypes = [
#     {"id": 1, "name": "Vegetable"},
#     {"id": 2, "name": "Carb"},
#     {"id": 3, "name": "Main Course"},
#     {"id": 4, "name": "Dessert"},
# ]


def home(request):
    foodtypes = FoodType.objects.all()
    context = {"foodtypes": foodtypes}
    return render(request, "base/home.html", context)


def foodtype(request, foodtype_id):
    foodtype = FoodType.objects.get(id=foodtype_id)
    context = {"foodtype": foodtype}
    return render(request, "base/foodtype.html", context)
