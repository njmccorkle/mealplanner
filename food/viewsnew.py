from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import Food, FoodType
from .forms import FoodForm, FoodTypeForm

from django.views.generic import ListView, DetailView


class FoodListView(ListView):
    model = Food
    template_name = "foodnew/food_list.html"
    context_object_name = "food_list"

    def get_queryset(self):
        return Food.objects.all()

    # # also could do
    # def get_queryset(self, **kwargs):
    #     context = super(FoodListView, self).get_context_data(**kwargs)
    #     context["new_stuff"] = "This is new stuff"
    #     return context


class FoodDetalView(DetailView):
    model = Food
    template_name = "foodnew/food_detail.html"
    context_object_name = "food"


# or manually...
# def food_detail_view(request, primary_key):
#     try:
#         food = Food.objects.get(pk=primary_key)
#     except Food.DoesNotExist:
#         raise Http404('Book does not exist')

#     return render(request, 'food_detail.html', context={'food': food})

# or
# class food_detail_view(request, pk):
#     food = get_object_or_404(Food, id=pk)
#     return render(request, "foodnew/food_detail.html", {"food": food})
