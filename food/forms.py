# from django.forms import ModelForm
from django import forms
from .models import Food, FoodType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django.http import HttpResponseRedirect
from django.urls import reverse


class FormActionMixin(object):
    def post(self, request, *args, **kwargs):
        """Add 'Cancel' button redirect."""
        if "cancel" in request.POST:
            url = reverse(self.get_success_url())  # or reverse("index")
            return HttpResponseRedirect(url)
        else:
            return super(FormActionMixin, self).post(request, *args, **kwargs)


class FoodForm(FormActionMixin, forms.ModelForm):
    class Meta:
        model = Food
        fields = "__all__"
        # fields = ["name", "food_type_id", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-FoodForm"
        self.helper.form_class = "blueForms"
        self.helper.form_method = "post"
        # self.helper.form_action = "submit"
        self.helper.add_input(Submit("submit", "Submit"))
        self.helper.add_input(Button())


class FoodTypeForm(FormActionMixin, forms.ModelForm):
    # class FoodTypeForm(forms.Form):
    class Meta:
        model = FoodType
        fields = "__all__"
        # fields = ["name", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-exampleForm"
        self.helper.form_class = "blueForms"
        self.helper.form_method = "post"
        # self.helper.form_action = "submit"
        self.helper.add_input(Submit("submit", "Submit"))
        self.helper.add_input(
            Submit(
                "cancel",
                "Cancel",
                css_class="btn-danger",
                formnovalidate=True,
            )
        )
