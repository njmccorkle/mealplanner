from django.urls import path
from . import views

urlpatterns = [
    path("mealitem/<int:pk>/", views.create_mealitem, name="create-mealitem"),
    path("htmx/mealitem/<int:pk>/", views.detail_mealitem, name="detail-mealitem"),
    path(
        "htmx/mealitem/<int:pk>/update/", views.update_mealitem, name="update-mealitem"
    ),
    path(
        "htmx/mealitem/<int:pk>/delete/", views.delete_mealitem, name="delete-mealitem"
    ),
    # path(
    #     "htmx/create-mealitem-form/",
    #     views.create_mealitem_form,
    #     name="create-mealitem-form",
    # ),
    path(
        "htmx/create-mealitem-form/<int:pk>",
        views.create_mealitem_form,
        name="create-mealitem-form",
    ),
    path("manage_meals/", views.manage_meals, name="manage-meals"),
    path("htmx/meal/<int:pk>/", views.detail_meal, name="detail-meal"),
    path("htmx/meal/<int:pk>/update/", views.update_meal, name="update-meal"),
    path(
        "htmx/create-meal-form/",
        views.create_meal_form,
        name="create-meal-form",
    ),
    path("htmx/meal/<int:pk>/delete/", views.delete_meal, name="delete-meal"),
    path(
        "htmx/meal/get-mealitems/<int:pk>",
        views.get_mealitems,
        name="get-mealitems",
    ),
]
