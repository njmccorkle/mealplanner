from django.db import models

from django.contrib.auth.models import User
from base.models import MealPlannerBaseModel


class CourseDef(MealPlannerBaseModel):
    class Meta:
        verbose_name = "Course Def"
        verbose_name_plural = "Course Defs"

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.Meta.verbose_name


class FoodDef(MealPlannerBaseModel):
    class Meta:
        verbose_name = "Food Def"
        verbose_name_plural = "Food Defs"

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey(
        CourseDef, related_name="foods", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name

    def get_name(self):
        return self.Meta.verbose_name
