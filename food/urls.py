from django.urls import path
from django.http import HttpResponse
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # path("", views.home, name="home"),
    # path("food/", views.list_foods, name="list-foods"),
    # path("food/new", views.create_food, name="create-food"),
    # path("food/edit/<int:pk>", views.edit_food, name="edit-food"),
    # path("food/delete/<int:pk>", views.delete_food, name="delete-food"),
    # path("foodtype/new", views.create_foodtype, name="create-foodtype"),
    # path("foodtype/edit/<int:pk>/", views.edit_foodtype, name="edit-foodtype"),
    # path("foodtype/delete/<int:pk>", views.delete_food, name="delete-foodtype"),
    # # this is working basic formset
    # path("formset_food/<int:pk>", views.formset_food, name="formset-food"),
    # this is working basic formset
    # path("formset_create/", views.create_foodtype_formset, name="formset_create"),
    # path("formset_update/", views.update_foodtype_formset, name="formset_update"),
    # path("manage-food/", views.maage_food, name="manage-food"),
    # htmx
    path("", TemplateView.as_view(template_name="food/home.html"), name="create-food"),
    path("<pk>/", views.create_food, name="create-food"),
    path("htmx/food/<pk>/", views.detail_food, name="detail-food"),
    path("htmx/food/<pk>/update/", views.update_food, name="update-food"),
    path("htmx/food/<pk>/delete/", views.delete_food, name="delete-food"),
    path("htmx/create-food-form/", views.create_food_form, name="create-food-form"),
]
