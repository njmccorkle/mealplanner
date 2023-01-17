from django.db import models
from django.contrib.auth.models import User


class MealPlannerBaseModel(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # modified_by = models.ForeignKey(User)

    class Meta:
        abstract = True
