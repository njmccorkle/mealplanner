from crispy_forms.helper import FormHelper
from django import forms

from .models import Course, Food, Meal


class MealForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Meal
        fields = ["name", "description", "courses"]


class CourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if kwargs.get("instance"):
            meal_ids = [t.pk for t in kwargs["instance"].meals.all()]

            kwargs["initial"] = {
                "meals": meal_ids,
            }
        super().__init__(*args, **kwargs)

    # https://stackoverflow.com/questions/49932426/save-many-to-many-field-django-forms
    def save(self, commit=True):
        # Get the unsaved Pizza instance
        instance = forms.ModelForm.save(self, False)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m

        def save_m2m():
            old_save_m2m()
            # This is where we actually link the course with the meals
            instance.meals.clear()
            for meal in self.cleaned_data["meals"]:
                instance.meals.add(meal)

        self.save_m2m = save_m2m

        instance.save()
        self.save_m2m()

        return instance

    foods = forms.ModelMultipleChoiceField(
        queryset=Food.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Allows user to deselect ALL checkboxes
    )

    meals = forms.ModelMultipleChoiceField(
        queryset=Meal.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Allows user to deselect ALL checkboxes
    )

    class Meta:
        model = Course
        fields = ["name", "description", "foods", "meals"]

    foods = forms.ModelMultipleChoiceField(
        queryset=Food.objects.all().order_by("name"),
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Allows user to deselect ALL checkboxes
    )

    class Meta:
        model = Course
        fields = ["name", "description", "foods"]
        # fields = "__all__"


class FoodForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if kwargs.get("instance"):
            course_ids = [t.pk for t in kwargs["instance"].courses.all()]

            kwargs["initial"] = {
                "courses": course_ids,
            }
        super().__init__(*args, **kwargs)

    # https://stackoverflow.com/questions/49932426/save-many-to-many-field-django-forms
    def save(self, commit=True):
        # Get the unsaved Pizza instance
        instance = forms.ModelForm.save(self, False)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m

        def save_m2m():
            old_save_m2m()
            # This is where we actually link the food with the courses
            instance.courses.clear()
            for course in self.cleaned_data["courses"]:
                instance.courses.add(course)

        self.save_m2m = save_m2m

        instance.save()
        self.save_m2m()

        return instance

    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Allows user to deselect ALL checkboxes
    )

    class Meta:
        model = Food
        fields = ["name", "description", "courses"]
