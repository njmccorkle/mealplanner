from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import Food, FoodType
from .forms import FoodForm, FoodTypeForm


def create_food(request, pk):
    foodtype = FoodType.objects.get(id=pk)
    print(f"foodtype = {foodtype}")
    food = Food.objects.filter(foodtype=foodtype)
    print(f"food = {food}")
    print(f"request.post = {request.POST}")
    form = FoodForm(request.POST or None)

    print(f"request is {request}")
    if request.method == "POST":
        print("posting")
        if form.is_valid():
            print("form is valid")
            food = form.save(commit=False)
            food.foodtype = foodtype
            food.save()
            return redirect("detail-food", pk=food.id)
        else:
            print("form is not valid")
            return render(
                request, "food/partials/food_form.html", context={"form": form}
            )

    context = {"form": form, "foodtype": foodtype, "food": food}
    print("returning create_food.html")
    return render(request, "food/create_food.html", context)


def update_food(request, pk):
    food = Food.objects.get(id=pk)
    print(f"request.post or none = {request.POST or None}")
    print(f"request is = {request}")
    print(f"request.method is = {request.method}")
    print(f"request.POST is = {request.POST}")
    form = FoodForm(request.POST or None, instance=food)
    form.fields["foodtype"].widget = forms.HiddenInput()
    form.fields["foodtype"].initial = food.foodtype

    if request.method == "POST":
        print("posting")
        if form.is_valid():
            print("form is valid")
            form.save()
            return redirect("detail-food", pk=food.id)
        print("form is not valid")

    context = {"form": form, "food": food}
    print("returning food form")
    return render(request, "food/partials/food_form.html", context)


def delete_food(request, pk):
    food = get_object_or_404(Food, id=pk)

    if request.method == "POST":
        food.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


def detail_food(request, pk):
    food = get_object_or_404(Food, id=pk)
    context = {"f": food}
    return render(request, "food/partials/food_detail.html", context)


def create_food_form(request, pk=None):
    form = FoodForm()
    if pk is not None:
        form.fields["foodtype"].widget = forms.HiddenInput()
        form.fields["foodtype"].initial = pk
    context = {"form": form}
    return render(request, "food/partials/food_form.html", context)


def create_foodtype_form(request):
    print(f"---create_foodtype_form")
    form = FoodTypeForm()
    context = {"form": form}
    return render(request, "food/partials/foodtype_form.html", context)


def manage_foodtypes(request, pk=None):
    print(f"---manage_foodtypes")
    if pk is None:
        print(f"getting all foodtypes")
        foodtype = FoodType.objects.all()
    else:
        print(f"getting one foodtype")
        foodtype = FoodType.objects.get(id=pk)
    print(f"foodtype = {foodtype}")
    print(f"request.post = {request.POST}")
    form = FoodTypeForm(request.POST or None)

    print(f"request is {request}")
    if request.method == "POST":
        print("posting")
        if form.is_valid():
            print("form is valid")
            foodtype = form.save(commit=False)
            # food.food_type = foodtype
            foodtype.save()
            return redirect("detail-foodtype", pk=foodtype.id)
        else:
            print("form is not valid")
            return render(
                request, "food/partials/foodtype_form.html", context={"form": form}
            )

    context = {"form": form, "foodtype": foodtype}
    print("returning manage_foodtypes.html")
    return render(request, "food/manage_foodtypes.html", context)


def detail_foodtype(request, pk):
    print(f"---detail_foodtype")
    foodtype = get_object_or_404(FoodType, id=pk)
    context = {"f": foodtype}
    return render(request, "food/partials/foodtype_detail.html", context)


def update_foodtype(request, pk):
    print(f"---update_foodtype")
    foodtype = FoodType.objects.get(id=pk)
    print(f"request.post or none = {request.POST or None}")
    print(f"request is = {request}")
    print(f"request.method is = {request.method}")
    print(f"request.POST is = {request.POST}")
    form = FoodTypeForm(request.POST or None, instance=foodtype)

    if request.method == "POST":
        print("posting")
        if form.is_valid():
            print("form is valid")
            form.save()
            return redirect("detail-food", pk=foodtype.id)
        print("form is not valid")

    context = {"form": form, "foodtype": foodtype}
    print("returning foodtype form")
    return render(request, "food/partials/foodtype_form.html", context)


def delete_foodtype(request, pk):
    print(f"---delete_foodtype")
    food = get_object_or_404(FoodType, id=pk)

    if request.method == "POST":
        food.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )
