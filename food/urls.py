from django.urls import path, include
from rest_framework import routers
from . import views, apiviews

from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r"course", apiviews.CourseViewSet)
router.register(r"foodDef", apiviews.FoodViewSet)

urlpatterns = [
    # path("", TemplateView.as_view(template_name="food/home.html")),
    # path("<int:pk>/", create_food, name="create-food"),
    # path("htmx/food/<int:pk>/", detail_food, name="detail-food"),
    # path("htmx/food/<int:pk>/update/", update_food, name="update-food"),
    # path("htmx/food/<int:pk>/delete/", delete_food, name="delete-food"),
    # path("htmx/create-food-form/", create_food_form, name="create-food-form"),
    # path(
    #     "htmx/create-food-form/<int:pk>",
    #     create_food_form,
    #     name="create-food-form",
    # ),
    # path("manage_courses/", manage_courses, name="manage-courses"),
    # path("htmx/course/<int:pk>/", detail_course, name="detail-course"),
    # path("htmx/course/<int:pk>/update/", update_course, name="update-course"),
    # path(
    #     "htmx/create-course-form/",
    #     create_course_form,
    #     name="create-course-form",
    # ),
    # path("htmx/course/<int:pk>/delete/", delete_course, name="delete-course"),
    # path(
    #     "htmx/course/course-top-foods/<int:pk>",
    #     get_top_foods,
    #     name="course-top-foods",
    # ),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("api/", include(router.urls)),
    path("course", views.CourseList.as_view(), name="course_list"),
    path("course/new", views.CourseCreate.as_view(), name="course_create"),
    # not currently used
    # path(
    #     "course/<int:pk>",
    #     views.CourseDetail.as_view(),
    #     name="course_detail",
    # ),
    path(
        "course/edit/<int:pk>",
        views.CourseUpdate.as_view(),
        name="course_update",
    ),
    path(
        "course/delete/<int:pk>",
        views.CourseDelete.as_view(),
        name="course_delete",
    ),
    ######
    path("food", views.FoodList.as_view(), name="food_list"),
    path("food/new", views.FoodCreate.as_view(), name="food_create"),
    # not currently used
    # path(
    #     "course/<int:pk>",
    #     views.CourseDetail.as_view(),
    #     name="course_detail",
    # ),
    path(
        "food/edit/<int:pk>",
        views.FoodUpdate.as_view(),
        name="food_update",
    ),
    path(
        "food/delete/<int:pk>",
        views.FoodDelete.as_view(),
        name="food_delete",
    ),
]
