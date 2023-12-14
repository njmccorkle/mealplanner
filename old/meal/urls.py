from django.urls import include, path
from rest_framework import routers

from .apiviews import *
from .views import *

router = routers.DefaultRouter()
router.register(r"meal", MealViewSet)
router.register(r"mealitem", MealItemViewSet)


urlpatterns = [
    # path("mealitem/<int:pk>/", create_mealitem, name="create-mealitem"),
    # path("htmx/mealitem/<int:pk>/", detail_mealitem, name="detail-mealitem"),
    # path("htmx/mealitem/<int:pk>/update/", update_mealitem, name="update-mealitem"),
    # path("htmx/mealitem/<int:pk>/delete/", delete_mealitem, name="delete-mealitem"),
    # # path(
    # #     "htmx/create-mealitem-form/",
    # #     create_mealitem_form,
    # #     name="create-mealitem-form",
    # # ),
    # path(
    #     "htmx/create-mealitem-form/<int:pk>",
    #     create_mealitem_form,
    #     name="create-mealitem-form",
    # ),
    # path("manage_meals/", manage_meals, name="manage-meals"),
    # path("htmx/meal/<int:pk>/", detail_meal, name="detail-meal"),
    # path("htmx/meal/<int:pk>/update/", update_meal, name="update-meal"),
    # path(
    #     "htmx/create-meal-form/",
    #     create_meal_form,
    #     name="create-meal-form",
    # ),
    # path("htmx/meal/<int:pk>/delete/", delete_meal, name="delete-meal"),
    # path(
    #     "htmx/meal/get-mealitems/<int:pk>",
    #     get_mealitems,
    #     name="get-mealitems",
    # ),
    path("api/", include(router.urls)),
]
