from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    # path("", views.home, name="home"),
    path("food/", views.list_foods, name="list-foods"),
    path("food/new", views.create_food, name="create-food"),
    path("food/edit/<int:pk>", views.edit_food, name="edit-food"),
    path("food/delete/<int:pk>", views.delete_food, name="delete-food"),
    path("foodtype/new", views.create_foodtype, name="create-foodtype"),
    path("foodtype/edit/<int:pk>/", views.edit_foodtype, name="edit-foodtype"),
    path("foodtype/delete/<int:pk>", views.delete_food, name="delete-foodtype"),
]
