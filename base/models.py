from django.contrib.auth.models import User
from django.db import models


class MealPlannerBaseModel(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, default="1"
    )
    # modified_by = models.ForeignKey(User)

    class Meta:
        abstract = True
