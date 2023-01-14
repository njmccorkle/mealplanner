from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import Food, FoodType
from .forms import FoodForm  # , FoodTypeForm, FoodFormSet

from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.db import transaction
from django.forms.models import (
    inlineformset_factory,
    modelform_factory,
    modelformset_factory,
)

# def home(request):
#     foodtypes = FoodType.objects.all()
#     context = {"foodtypes": foodtypes}
#     return render(request, "food/home.html", context)


# def list_foods(request):
#     foods = (
#         Food.objects.select_related("food_type")
#         .order_by("food_type__name", "name")
#         .all()
#     )
#     context = {"foods": foods}
#     return render(request, "food/food_list.html", context)


# def create_food(request):
#     title = "Add new food"
#     form = FoodForm()
#     if request.method == "POST":
#         form = FoodForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#     context = {"form": form, "title": title}
#     return render(request, "food/food_form.html", context)


# def edit_food(request, pk):
#     title = "Edit a food"
#     food = Food.objects.get(id=pk)
#     form = FoodForm(instance=food)
#     if request.method == "POST":
#         form = FoodForm(request.POST, instance=food)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#     context = {"form": form, "food": food}
#     return render(request, "food/food_form.html", context)


# def delete_food(request, pk):
#     food = Food.objects.get(id=pk)
#     context = {"obj": food}
#     if request.method == "POST":
#         food.delete()
#         return redirect("home")
#     return render(request, "food/delete.html", context)


# def view_foodtype(request, foodtype_id):
#     foodtype = FoodType.objects.get(id=foodtype_id)
#     context = {"foodtype": foodtype}
#     return render(request, "food/foodtype.html", context)


# def create_foodtype(request):
#     title = "Create a new food type"
#     form = FoodTypeForm()
#     if request.method == "POST":
#         form = FoodTypeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#     context = {"form": form, "title": title}
#     return render(request, "food/food_form.html", context)


# def edit_foodtype(request, pk):
#     food = FoodType.objects.get(id=pk)
#     form = FoodTypeForm(instance=food)
#     if request.method == "POST":
#         form = FoodForm(request.POST, instance=food)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#     context = {"form": form}
#     return render(request, "food/food_form.html", context)


# def delete_foodtype(request, pk):
#     food = Food.objects.get(id=pk)
#     context = {"obj": food}
#     if request.method == "POST":
#         food.delete()
#         return redirect("home")
#     return render(request, "food/delete.html", context)


# def formset_food(request, pk):

#     foodtype = FoodType.objects.get(id=pk)
#     title = foodtype.name
#     food = Food.objects.filter(food_type=foodtype)
#     formset = FoodFormSet(request.POST or None)

#     if request.method == "POST":
#         if formset.is_valid():
#             formset.instance = foodtype
#             formset.save()
#             return redirect("formset-food", pk=foodtype.id)
#     context = {"formset": formset, "foodtype": foodtype, "food": food, "title": title}
#     return render(request, "food/formset_food.html", context)


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


### this is not posting for some reason. even when not nested inside the other form
def create_food_form(request):
    form = FoodForm()
    context = {"form": form}
    return render(request, "food/partials/food_form.html", context)


def update_food(request, pk):
    food = Food.objects.get(id=pk)
    form = FoodForm(request.POST or None, instance=food)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("detail-food", pk=food.id)

    context = {"form": form, "food": food}

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
    context = {"food": food}
    return render(request, "food/partials/food_detail.html", context)
