from django.urls import path, include
from rest_framework import routers
from .views import *
from .apiviews import *

from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r"foodtype", FoodTypeViewSet)
router.register(r"food", FoodViewSet)

urlpatterns = [
    # path("", TemplateView.as_view(template_name="food/home.html"), name="create-food"),
    path("<int:pk>/", create_food, name="create-food"),
    path("htmx/food/<int:pk>/", detail_food, name="detail-food"),
    path("htmx/food/<int:pk>/update/", update_food, name="update-food"),
    path("htmx/food/<int:pk>/delete/", delete_food, name="delete-food"),
    path("htmx/create-food-form/", create_food_form, name="create-food-form"),
    path(
        "htmx/create-food-form/<int:pk>",
        create_food_form,
        name="create-food-form",
    ),
    path("manage_foodtypes/", manage_foodtypes, name="manage-foodtypes"),
    path("htmx/foodtype/<int:pk>/", detail_foodtype, name="detail-foodtype"),
    path("htmx/foodtype/<int:pk>/update/", update_foodtype, name="update-foodtype"),
    path(
        "htmx/create-foodtype-form/",
        create_foodtype_form,
        name="create-foodtype-form",
    ),
    path("htmx/foodtype/<int:pk>/delete/", delete_foodtype, name="delete-foodtype"),
    path(
        "htmx/foodtype/foodtype-top-foods/<int:pk>",
        get_top_foods,
        name="foodtype-top-foods",
    ),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
