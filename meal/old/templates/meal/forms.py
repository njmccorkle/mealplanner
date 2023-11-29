from django import forms
from .models import Meal, MealItems
from crispy_forms.helper import FormHelper


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False  # form tag is added in template
        self.helper.disable_csrf = True  # no need, request is sent via htmx


class MealItemForm(forms.ModelForm):
    class Meta:
        model = MealItems
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False  # form tag is added in template
        self.helper.disable_csrf = True  # no need, request is sent via htmx
