from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:food_type_id>/", views.foodtype, name="food type"),
    path("<int:food_id>/", views.food, name="food"),
]
