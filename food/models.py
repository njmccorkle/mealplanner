from django.contrib.auth.models import User
from django.db import models
from django.db.models.functions import Lower

from base.models import MealPlannerBaseModel


class Food(MealPlannerBaseModel):
    class Meta:
        ordering = [Lower("name")]
        verbose_name = "Food"
        verbose_name_plural = "Foods"

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.Meta.verbose_name


class Course(MealPlannerBaseModel):
    class Meta:
        ordering = [Lower("name")]
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    foods = models.ManyToManyField(
        Food, through="CourseFoods", blank=True, related_name="courses"
    )

    def __str__(self):
        return self.name

    def get_name(self):
        return self.Meta.verbose_name


class CourseFoods(MealPlannerBaseModel):
    class Meta:
        verbose_name = "CourseFood"
        verbose_name_plural = "CourseFoods"

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="courses")
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="foods")

    def __str__(self):
        return self.course.name + " - " + self.food.name


# defines the meals that will be planned - supper, lunch, breakfast, dinner, etc
class Meal(MealPlannerBaseModel):
    class Meta:
        ordering = [Lower("name")]
        verbose_name = "Meal"
        verbose_name_plural = "Meals"

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    courses = models.ManyToManyField(
        Course, through="MealCourses", blank=True, related_name="meals"
    )

    def __str__(self):
        return self.name


class MealCourses(MealPlannerBaseModel):
    class Meta:
        verbose_name = "MealCourses"
        verbose_name_plural = "MealCourses"

    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.meal.name + " - " + self.course.name
