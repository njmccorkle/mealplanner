from django import forms

from .models import Course, Meal
from crispy_forms.helper import FormHelper


class MealForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "first arg is the legend of the fieldset",
                "name",
                "description",
                InlineCheckBoxes("courses"),
            ),
            Submit("submit", "Submit", css_class="button white"),
        )

    class Meta:
        model = Meal
        fields = ["name", "description"]
