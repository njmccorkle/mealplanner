from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers

from .apiviews import *
from .views import *

router = routers.DefaultRouter()
router.register(r"course", CourseViewSet)
router.register(r"food", FoodViewSet)

urlpatterns = [
    # path("", TemplateView.as_view(template_name="food/home.html"), name="create-food"),
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
    path("api/", include(router.urls)),
]
