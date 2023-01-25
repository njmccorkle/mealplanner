from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import Menu, MenuItem
from .forms import MenuForm, MenuItemForm
from meal.models import Meal, MealItems
from food.models import Food, FoodType


def create_menu_form(request):
    print(f"---create_menu_form")
    form = MenuForm()
    context = {"form": form}
    return render(request, "menu/partials/menu_form.html", context)


def manage_menus(request, pk=None):
    print(f"---manage_menus")
    if pk is None:
        menu = Menu.objects.all()
    else:
        menu = Menu.objects.get(id=pk)
    form = MenuForm(request.POST or None)

    if request.method == "POST":
        print("posting")
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            return redirect("detail-menu", pk=menu.id)
        else:
            return render(
                request, "menu/partials/menu_form.html", context={"form": form}
            )

    context = {"form": form, "menu": menu}
    return render(request, "menu/manage_menus.html", context)


def create_menu(request):
    print(f"---create_menu")
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            newmenu = form.save()
            mealitems = MealItems.objects.filter(meal=request.POST["meal"])
            # newmenu.save()
            for mealitem in mealitems:
                new = MenuItem()
                new.created_by = newmenu.created_by
                new.menu = newmenu
                new.foodtype = mealitem.foodtype
                new.save()
            return redirect("detail-menu", pk=newmenu.id)
        else:
            return render(
                request, "menu/partials/menu_form.html", context={"form": form}
            )

    # context = {"form": form, "menu": menu}
    # print("returning manage_menus.html")
    # return render(request, "menu/manage_menus.html", context)


def detail_menu(request, pk):
    print(f"---detail_menu")
    menu = get_object_or_404(Menu, id=pk)
    context = {"m": menu}
    return render(request, "menu/partials/menu_detail.html", context)


def update_menu(request, pk):
    print(f"---update_menu")
    menu = Menu.objects.get(id=pk)
    form = MenuForm(request.POST or None, instance=menu)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("detail-menu", pk=menu.id)

    context = {"form": form, "menu": menu}
    return render(request, "menu/partials/menu_form.html", context)


def delete_menu(request, pk):
    print(f"---delete_menu")
    menu = get_object_or_404(Menu, id=pk)

    if request.method == "POST":
        menu.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


########################################################
def create_menuitem(request, pk):
    print(f"---create_menuitem")
    menu = Menu.objects.get(id=pk)
    menuitems = MenuItem.objects.filter(menu=menu)
    form = MenuItemForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            menuitem = form.save(commit=False)
            menuitem.menu = menu
            menuitem.foodtype = FoodType.objects.get(pk=request.POST.get("foodtype"))
            menuitem.food = Food.objects.get(pk=request.POST.get("food"))
            menuitem.save()
            return redirect("detail-menuitem", pk=menuitem.id)
        else:
            return render(
                request, "menu/partials/menuitem_form.html", context={"form": form}
            )

    context = {"form": form, "menu": menu, "menuitems": menuitems}
    return render(request, "menu/create_menuitem.html", context)


def create_menuitem_form(request, pk=None):
    print(f"-----create_menuitem_form")
    form = MenuItemForm()

    foodtypes = FoodType.objects.all()
    if pk is not None:
        form.fields["menu"].widget = forms.HiddenInput()
        form.fields["menu"].initial = pk
    context = {
        "form": form,
        "foodtypes": foodtypes,
    }
    return render(request, "menu/partials/menuitem_form.html", context)


def update_menuitem(request, pk):
    print(f"---update_menuitem")
    menuitem = MenuItem.objects.get(id=pk)
    form = MenuItemForm(request.POST or None, instance=menuitem)
    foodtypes = FoodType.objects.all()
    form.fields["menu"].widget = forms.HiddenInput()
    form.fields["menu"].initial = pk
    form.fields["created_by"].widget = forms.HiddenInput()
    form.fields["created_by"].initial = menuitem.created_by

    if menuitem.foodtype is not None:
        foods = Food.objects.filter(foodtype=menuitem.foodtype)

    if request.method == "POST":
        print(f"posting")
        if form.is_valid():
            print(f"form is valid")
            form.save()
            print(f"returning detail-menuitem")
            return redirect("detail-menuitem", pk=menuitem.id)

    context = {
        "form": form,
        "menuitem": menuitem,
        "foodtypes": foodtypes,
        "foods": foods,
        "selected_foodtype": menuitem.foodtype,
        "selected_food": menuitem.food,
    }
    print(f"context = {context}")
    return render(request, "menu/partials/menuitem_form.html", context)


def get_menuitems(request):
    print(f"---get_menuitems")
    foodtype = FoodType.objects.get(id=request.GET.get("foodtype"))
    foods = Food.objects.filter(foodtype=foodtype.id)
    context = {"foods": foods}
    return render(request, "menu/partials/menuitem_options.html", context)


def delete_menuitem(request, pk):
    print(f"---delete_menuitem")
    menuitem = get_object_or_404(MenuItem, id=pk)

    if request.method == "POST":
        menuitem.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


def detail_menuitem(request, pk):
    print(f"---detail_menuitem")
    menuitem = get_object_or_404(MenuItem, id=pk)
    context = {"menuitem": menuitem}
    return render(request, "menu/partials/menuitem_detail.html", context)
