from django.contrib.auth.models import User
from django.db import models

from base.models import MealPlannerBaseModel


class Course(MealPlannerBaseModel):
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.Meta.verbose_name


class Food(MealPlannerBaseModel):
    class Meta:
        verbose_name = "Food"
        verbose_name_plural = "Foods"

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey(
        Course, related_name="foods", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name

    def get_name(self):
        return self.Meta.verbose_name


# defines the meals that will be planned - supper, lunch, breakfast, dinner, etc
class Meal(MealPlannerBaseModel):
    class Meta:
        verbose_name = "Meal"
        verbose_name_plural = "Meals"

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
