from django import forms
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import MealForm
from .models import Course, Food, Meal


class CourseList(ListView):
    model = Course
    template_name = "course_list.html"
    context_object_name = "courses"


# not currently used
# class CourseDetail(DetailView):
#     model = Course
#     template_name = "course_detail.html"
#     context_object_name = "course"


class CourseCreate(CreateView):
    model = Course
    template_name = "course_form.html"
    fields = ["name", "description"]
    success_url = reverse_lazy("course_list")


class CourseUpdate(UpdateView):
    model = Course
    template_name = "course_form.html"
    fields = ["name", "description"]
    success_url = reverse_lazy("course_list")


class CourseDelete(DeleteView):
    model = Course
    template_name = "course_confirm_delete.html"
    success_url = reverse_lazy("course_list")


class FoodList(ListView):
    model = Food
    template_name = "food_list.html"
    context_object_name = "food"
    ordering = ["course", "name"]


class FoodCreate(CreateView):
    model = Food
    template_name = "food_form.html"
    fields = ["name", "description", "course"]
    success_url = reverse_lazy("food_list")


class FoodUpdate(UpdateView):
    model = Food
    template_name = "food_form.html"
    fields = ["name", "description", "course"]
    success_url = reverse_lazy("food_list")


class FoodDelete(DeleteView):
    model = Food
    template_name = "food_confirm_delete.html"
    success_url = reverse_lazy("food_list")


class MealList(ListView):
    model = Meal
    template_name = "meal_list.html"
    context_object_name = "meals"
    ordering = ["name"]


class MealCreate(CreateView):
    model = Meal
    template_name = "meal_form.html"
    form_class = MealForm
    # fields = ["name", "description", "course"]
    # fields = "__all__"
    success_url = reverse_lazy("meal_list")


class MealUpdate(UpdateView):
    model = Meal
    form = MealForm
    template_name = "meal_form.html"
    # fields = ["name", "description", "course"]
    fields = "__all__"
    success_url = reverse_lazy("meal_list")


class MealDelete(DeleteView):
    model = Meal
    template_name = "meal_confirm_delete.html"
    success_url = reverse_lazy("meal_list")


# https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024
