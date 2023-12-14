from django import forms

from .models import Course, Meal


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ["name", "description"]
