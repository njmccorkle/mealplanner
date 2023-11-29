from django import forms
from .models import Food, Course
from crispy_forms.helper import FormHelper


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False  # form tag is added in template
        self.helper.disable_csrf = True  # no need, request is sent via htmx


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False  # form tag is added in template
        self.helper.disable_csrf = True  # no need, request is sent via htmx
