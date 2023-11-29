from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import FoodDef, CourseDef

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

# from .forms import FoodDefForm, CourseDefForm


class CourseDefList(ListView):
    model = CourseDef
    template_name = "coursedef_list.html"
    context_object_name = "courdefs"


class CourseDefDetail(DetailView):
    model = CourseDef
    template_name = "coursedef_detail.html"
    context_object_name = "coursedef"


class CourseDefCreate(CreateView):
    model = CourseDef
    template_name = "coursedef_form.html"
    fields = ["title", "description", "image"]
    success_url = reverse_lazy("coursedef_list")


class CourseDefUpdate(UpdateView):
    model = CourseDef
    template_name = "coursedef_update.html"
    fields = ["title", "description", "image"]
    success_url = reverse_lazy("coursedef_list")


class CourseDefDelete(DeleteView):
    model = CourseDef
    template_name = "coursedef_confirm_delete.html"
    success_url = reverse_lazy("coursedef_list")
