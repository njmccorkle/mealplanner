from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import Food, FoodType
from .forms import FoodForm


def create_food(request, pk):
    foodtype = FoodType.objects.get(id=pk)
    print(f"foodtype = {foodtype}")
    food = Food.objects.filter(food_type=foodtype)
    print(f"food = {food}")
    print(f"request.post = {request.POST}")
    form = FoodForm(request.POST or None)

    print(f"request is {request}")
    if request.method == "POST":
        print("posting")
        if form.is_valid():
            print("form is valid")
            food = form.save(commit=False)
            food.food_type = foodtype
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


def create_food_form(request):
    form = FoodForm()
    context = {"form": form}
    return render(request, "food/partials/food_form.html", context)
