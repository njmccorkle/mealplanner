from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import Food, Course

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy


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


# https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024
