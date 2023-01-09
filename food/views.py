from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Food, FoodType
from .forms import FoodForm, FoodTypeForm

# def home(request):
#     foodtypes = FoodType.objects.all()
#     context = {"foodtypes": foodtypes}
#     return render(request, "food/home.html", context)


def list_foods(request):
    foods = (
        Food.objects.select_related("food_type_id")
        .order_by("food_type_id__name", "name")
        .all()
    )
    context = {"foods": foods}
    return render(request, "food/food_list.html", context)


def create_food(request):
    title = "Add new food"
    form = FoodForm()
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form, "title": title}
    return render(request, "food/food_form.html", context)


def edit_food(request, pk):
    title = "Edit a food"
    food = Food.objects.get(id=pk)
    form = FoodForm(instance=food)
    if request.method == "POST":
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form, "food": food}
    return render(request, "food/food_form.html", context)


def delete_food(request, pk):
    food = Food.objects.get(id=pk)
    context = {"obj": food}
    if request.method == "POST":
        food.delete()
        return redirect("home")
    return render(request, "delete.html", context)


def view_foodtype(request, foodtype_id):
    foodtype = FoodType.objects.get(id=foodtype_id)
    context = {"foodtype": foodtype}
    return render(request, "food/foodtype.html", context)


def create_foodtype(request):
    title = "Create a new food type"
    form = FoodTypeForm()
    if request.method == "POST":
        form = FoodTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form, "title": title}
    return render(request, "food/food_form.html", context)


def edit_foodtype(request, pk):
    food = FoodType.objects.get(id=pk)
    form = FoodTypeForm(instance=food)
    if request.method == "POST":
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "food/food_form.html", context)


def delete_foodtype(request, pk):
    food = Food.objects.get(id=pk)
    context = {"obj": food}
    if request.method == "POST":
        food.delete()
        return redirect("home")
    return render(request, "delete.html", context)
