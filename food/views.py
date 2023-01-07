from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodType


def home(request):
    foodtypes = FoodType.objects.all()
    context = {"foodtypes": foodtypes}
    return render(request, "food/home.html", context)


def foodtype(request, foodtype_id):
    foodtype = FoodType.objects.get(id=foodtype_id)
    context = {"foodtype": foodtype}
    return render(request, "base/foodtype.html", context)
