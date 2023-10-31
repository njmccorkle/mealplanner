from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="food/home.html"), name="create-food"),
    path("<int:pk>/", views.create_food, name="create-food"),
    path("htmx/food/<int:pk>/", views.detail_food, name="detail-food"),
    path("htmx/food/<int:pk>/update/", views.update_food, name="update-food"),
    path("htmx/food/<int:pk>/delete/", views.delete_food, name="delete-food"),
    path("htmx/create-food-form/", views.create_food_form, name="create-food-form"),
    path(
        "htmx/create-food-form/<int:pk>",
        views.create_food_form,
        name="create-food-form",
    ),
    path("manage_foodtypes/", views.manage_foodtypes, name="manage-foodtypes"),
    path("htmx/foodtype/<int:pk>/", views.detail_foodtype, name="detail-foodtype"),
    path(
        "htmx/foodtype/<int:pk>/update/", views.update_foodtype, name="update-foodtype"
    ),
    path(
        "htmx/create-foodtype-form/",
        views.create_foodtype_form,
        name="create-foodtype-form",
    ),
    path(
        "htmx/foodtype/<int:pk>/delete/", views.delete_foodtype, name="delete-foodtype"
    ),
    path(
        "htmx/foodtype/foodtype-top-foods/<int:pk>",
        views.get_top_foods,
        name="foodtype-top-foods",
    ),
]
