from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.models import User

from food.models import Course, Food

from .models import Menu, MenuItem


class DateInput(forms.DateInput):
    input_type = "date"


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"
        widgets = {
            "menu_date": DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False  # form tag is added in template
        self.helper.disable_csrf = True  # no need, request is sent via htmx


# class MenuItemForm(forms.Form):
#     menu = forms.ModelChoiceField(queryset=Menu.objects.all())
#     course = forms.ModelChoiceField(queryset=Course.objects.all())
#     food = forms.ModelChoiceField(queryset=Food.objects.all())
#     created_by = forms.ModelChoiceField(queryset=User.objects.all())

# def clean(self):
#     cleaned_data = super(MenuItemForm, self).clean()
#     menu = cleaned_data.get("menu")
#     course = cleaned_data.get("course")
#     food = cleaned_data.get("food")
# if not name and not email and not message:
#     raise forms.ValidationError("You have to write something!")


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"
        # exclude = ["course", "food"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False  # form tag is added in template
        self.helper.disable_csrf = True  # no need, request is sent via htmx
