from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import Meal, MealItems
from .forms import MealForm, MealItemForm


def create_meal_form(request):
    print(f"---create_meal_form")
    form = MealForm()
    context = {"form": form}
    return render(request, "meal/partials/meal_form.html", context)


def manage_meals(request, pk=None):
    print(f"---manage_meals")
    print(f"pk = {pk}")
    if pk is None:
        print(f"getting all meals")
        meal = Meal.objects.all()
    else:
        print(f"getting one meal")
        meal = Meal.objects.get(id=pk)
    print(f"meal = {meal}")
    print(f"request.post = {request.POST}")
    form = MealForm(request.POST or None)

    print(f"request is {request}")
    if request.method == "POST":
        print("posting")
        if form.is_valid():
            print("form is valid")
            meal = form.save(commit=False)
            # food.food_type = meal
            meal.save()
            return redirect("detail-meal", pk=meal.id)
        else:
            print("form is not valid")
            return render(
                request, "meal/partials/meal_form.html", context={"form": form}
            )

    context = {"form": form, "meal": meal}
    print("returning manage_meals.html")
    return render(request, "meal/manage_meals.html", context)


def detail_meal(request, pk):
    print(f"---detail_meal")
    meal = get_object_or_404(Meal, id=pk)
    context = {"m": meal}
    return render(request, "meal/partials/meal_detail.html", context)


def update_meal(request, pk):
    print(f"---update_meal")
    meal = Meal.objects.get(id=pk)
    print(f"request.post or none = {request.POST or None}")
    print(f"request is = {request}")
    print(f"request.method is = {request.method}")
    print(f"request.POST is = {request.POST}")
    form = MealForm(request.POST or None, instance=meal)

    if request.method == "POST":
        print("posting")
        if form.is_valid():
            print("form is valid")
            form.save()
            return redirect("detail-meal", pk=meal.id)
        print("form is not valid")

    context = {"form": form, "meal": meal}
    print("returning meal form")
    return render(request, "meal/partials/meal_form.html", context)


def delete_meal(request, pk):
    print(f"---delete_meal")
    meal = get_object_or_404(Meal, id=pk)

    if request.method == "POST":
        meal.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


########################################################
def create_mealitem(request, pk):
    meal = Meal.objects.get(id=pk)
    print(f"meal = {meal}")
    mealitem = MealItems.objects.filter(meal=meal)
    print(f"mealitem = {mealitem}")
    print(f"request.post = {request.POST}")
    form = MealItemForm(request.POST or None)

    print(f"request is {request}")
    if request.method == "POST":
        print("posting")
        if form.is_valid():
            print("form is valid")
            mealitem = form.save(commit=False)
            mealitem.meal = meal
            mealitem.save()
            return redirect("detail-mealitem", pk=mealitem.id)
        else:
            print("form is not valid")
            return render(
                request, "meal/partials/mealitem_form.html", context={"form": form}
            )

    context = {"form": form, "meal": meal, "mealitem": mealitem}
    print("returning create_mealitem.html")
    return render(request, "meal/create_mealitem.html", context)


def update_mealitem(request, pk):
    mealitem = MealItems.objects.get(id=pk)
    print(f"request.post or none = {request.POST or None}")
    print(f"request is = {request}")
    print(f"request.method is = {request.method}")
    print(f"request.POST is = {request.POST}")
    form = MealItemForm(request.POST or None, instance=mealitem)
    form.fields["meal"].widget = forms.HiddenInput()
    form.fields["meal"].initial = pk

    if request.method == "POST":
        print("posting")
        if form.is_valid():
            print("form is valid")
            form.save()
            return redirect("detail-mealitem", pk=mealitem.id)
        print("form is not valid")

    context = {"form": form, "mealitem": mealitem}
    print("returning mealitem form")
    return render(request, "meal/partials/mealitem_form.html", context)


def delete_mealitem(request, pk):
    mealitem = get_object_or_404(MealItems, id=pk)

    if request.method == "POST":
        mealitem.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


def detail_mealitem(request, pk):
    mealitem = get_object_or_404(MealItems, id=pk)
    context = {"mi": mealitem}
    return render(request, "meal/partials/mealitem_detail.html", context)


def create_mealitem_form(request, pk=None):
    form = MealItemForm()
    if pk is not None:
        form.fields["meal"].widget = forms.HiddenInput()
        form.fields["meal"].initial = pk
    context = {"form": form}
    return render(request, "meal/partials/mealitem_form.html", context)
