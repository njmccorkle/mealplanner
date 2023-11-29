from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import Food, Course
from .forms import FoodForm, CourseForm


def create_food(request, pk):
    course = Course.objects.get(id=pk)
    print(f"course = {course}")
    food = Food.objects.filter(course=course)
    print(f"food = {food}")
    print(f"request.post = {request.POST}")
    form = FoodForm(request.POST or None)

    print(f"request is {request}")
    if request.method == "POST":
        print("posting")
        if form.is_valid():
            print("form is valid")
            food = form.save(commit=False)
            food.course = course
            food.save()
            return redirect("detail-food", pk=food.id)
        else:
            print("form is not valid")
            return render(
                request, "food/partials/food_form.html", context={"form": form}
            )

    context = {"form": form, "course": course, "food": food}
    print("returning create_food.html")
    return render(request, "food/create_food.html", context)


def update_food(request, pk):
    food = Food.objects.get(id=pk)
    print(f"request.post or none = {request.POST or None}")
    print(f"request is = {request}")
    print(f"request.method is = {request.method}")
    print(f"request.POST is = {request.POST}")
    form = FoodForm(request.POST or None, instance=food)
    form.fields["course"].widget = forms.HiddenInput()
    form.fields["course"].initial = food.course

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
        form.fields["course"].widget = forms.HiddenInput()
        form.fields["course"].initial = pk
    context = {"form": form}
    return render(request, "food/partials/food_form.html", context)


def create_course_form(request):
    print(f"---create_course_form")
    form = CourseForm()
    context = {"form": form}
    return render(request, "food/partials/course_form.html", context)


def manage_courses(request, pk=None):
    print(f"---manage_courses")
    if pk is None:
        print(f"getting all courses")
        course = Course.objects.all()
    else:
        print(f"getting one course")
        course = Course.objects.get(id=pk)
    print(f"course = {course}")
    print(f"request.post = {request.POST}")
    form = CourseForm(request.POST or None)

    print(f"request is {request}")
    if request.method == "POST":
        print("posting")
        if form.is_valid():
            print("form is valid")
            course = form.save(commit=False)
            # food.food_type = course
            course.save()
            return redirect("detail-course", pk=course.id)
        else:
            print("form is not valid")
            return render(
                request, "food/partials/course_form.html", context={"form": form}
            )

    context = {"form": form, "course": course}
    print("returning manage_courses.html")
    return render(request, "food/manage_courses.html", context)


def detail_course(request, pk):
    print(f"---detail_course")
    course = get_object_or_404(Course, id=pk)
    context = {"f": course}
    return render(request, "food/partials/course_detail.html", context)


def get_top_foods(request, pk):
    print(f"---get_top_foods")
    course = Course.objects.get(id=pk)
    topfoods = course.foods.all().order_by("name")  # [:4]
    context = {"topfoods": topfoods}
    return render(request, "food/partials/course_top_foods.html", context)


def update_course(request, pk):
    print(f"---update_course")
    course = Course.objects.get(id=pk)
    print(f"request.post or none = {request.POST or None}")
    print(f"request is = {request}")
    print(f"request.method is = {request.method}")
    print(f"request.POST is = {request.POST}")
    form = CourseForm(request.POST or None, instance=course)

    if request.method == "POST":
        print("posting")
        if form.is_valid():
            print("form is valid")
            form.save()
            return redirect("detail-food", pk=course.id)
        print("form is not valid")

    context = {"form": form, "course": course}
    print("returning course form")
    return render(request, "food/partials/course_form.html", context)


def delete_course(request, pk):
    print(f"---delete_course")
    food = get_object_or_404(Course, id=pk)

    if request.method == "POST":
        food.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )
