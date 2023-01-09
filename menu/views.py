from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Menu, MenuMeal, MenuMealItem
from .forms import MenuForm, MenuMealForm, MenuMealItemForm

# from .forms import MenuMealFormSet


def home(request):
    menus = Menu.objects.all()
    context = {"menus": menus}
    return render(request, "menu/home.html", context)


def create_menu(request):
    form = MenuForm()
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create-menumeal")
    context = {"form": form}
    return render(request, "menu/menu_form.html", context)


def create_menumeal(request):
    form = MenuMealForm()
    if request.method == "POST":
        form = MenuMealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create-menumealitem")
    context = {"form": form}
    return render(request, "menu/menu_form.html", context)


def create_menumealitem(request):
    form = MenuMealItemForm()
    if request.method == "POST":
        form = MenuMealItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {"form": form}
    return render(request, "menu/menu_form.html", context)


# def edit_food(request, food_id):
#     food = Food.objects.get(id=food_id)
#     form = FoodForm(instance=food)
#     if request.method == "POST":
#         form = FoodForm(request.POST, instance=food)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#     context = {"form": form}
#     return render(request, "food/food_form.html", context)


# class MenuInline:
#     form_class = MenuForm
#     model = Menu
#     template_name = "menu/menu_create_or_update.html"

#     def form_valid(self, form):
#         named_formsets = self.get_named_formsets()
#         if not all((x.is_valid() for x in named_formsets.values())):
#             return self.render_to_response(self.get_context_data(form=form))
#         self.object = form.save()
#         # for every formset, attempt to find a specific formset save function
#         # otherwise, just save.
#         for name, formset in named_formsets.items():
#             formset_save_func = getattr(self, "formset_{0}_valid".format(name), None)
#             if formset_save_func is not None:
#                 formset_save_func(formset)
#             else:
#                 formset.save()
#         return redirect("home")

#     def formset_menumeals_valid(self, formset):
#         menumeals = formset.save(commit=False)
#         for obj in formset.deleted_objects:
#             obj.delete()
#         for menumeal in menumeals:
#             menumeal.menu_id = self.object
#             menumeal.save()


# class MenuCreate(MenuInline, CreateView):
#     def get_context_data(self, **kwargs):
#         context = super(MenuCreate, self).get_context_data(**kwargs)
#         context["named_formsets"] = self.get_named_formsets()
#         return context

#     def get_named_formsets(self):
#         if self.request.method == "GET":
#             return {"menumeals": MenuMealFormSet(prefix="menumeals")}
#         else:
#             return {
#                 "menumeals": MenuMealFormSet(
#                     self.request.POST or None,
#                     self.request.FILES or None,
#                     prefix="menumeals",
#                 )
#             }


# class MenuUpdate(MenuInline, UpdateView):
#     def get_context_data(self, **kwargs):
#         context = super(MenuUpdate, self).get_context_data(**kwargs)
#         context["named_formsets"] = self.get_named_formsets()
#         return context

#     def get_named_formsets(self):
#         return {
#             "menumeals": MenuMealFormSet(
#                 self.request.POST or None,
#                 self.request.FILES or None,
#                 instance=self.object,
#                 prefix="menumeals",
#             )
#         }


# class MenuList(ListView):
#     model = Menu
#     # template = "menu/menu_list.html"
#     # context_object_name = "menus"


# def delete_menumeal(request, pk):
#     try:
#         menumeal = MenuMeal.objects.get(id=pk)
#     except MenuMeal.DoesNotExist:
#         messages.success(request, "Object does not exist")
#         return redirect("menus:update_menu", pk=menumeal.menu_id.id)
#     menumeal.delete()
#     messages.success(request, "Menu Meal deleted successfully")

#     return redirect("menus:update_menu", pk=menumeal.menu_id.id)
