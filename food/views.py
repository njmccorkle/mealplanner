from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import FoodDef, Course

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

# from .forms import FoodDefForm, CourseForm


# def CourseList(request):
#     print(f"CourseList")
#     courses = Course.objects.all()  # .order_by('-name')
#     print(f"courses #: {len(courses)}")
#     return render(request, "course_list.html", {"courses": courses})


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
