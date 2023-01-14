from django import forms
from .models import Food, FoodType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML, Field
from .custom_layout_object import Formset


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False  # form tag is added in template
        self.helper.disable_csrf = True  # no need, request is sent via htmx

    # def __init__(self, *args, **kwargs):
    #     super(FoodForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_id = "id-FoodForm"
    #     self.helper.form_class = "blueForms"
    #     self.helper.form_method = "post"
    #     # self.helper.form_action = "submit"
    #     self.helper.layout = Layout(
    #         Fieldset(
    #             "Add a new food", "name", "description", "food_type", "created_by"
    #         ),
    #         # Submit("submit", "Submit"),
    #         # HTML("""<a href="{{request.META.HTTP_REFERER}}">Go back</a>"""),
    #     )


# class FoodTypeForm(forms.ModelForm):
#     class Meta:
#         model = FoodType
#         fields = "__all__"

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_id = "id-exampleForm"
#         self.helper.form_class = "blueForms"
#         self.helper.form_method = "post"
#         self.helper.layout = Layout(
#             Fieldset("Add a new food type", "name", "description", "created_by"),
#             Submit("submit", "Submit"),
#             HTML("""<a href="{{request.META.HTTP_REFERER}}">Go back</a>"""),
#         )


class FoodTypeForm(forms.ModelForm):
    class Meta:
        model = FoodType
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(FoodTypeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3 create-label"
        self.helper.field_class = "col-md-9"

        self.helper.layout = Layout(
            Field("name"),
            Field("description"),
            Field("created_by"),
            Fieldset("Add foods", Formset("foods")),
            # Fieldset("Add a new food type", "name", "description", "created_by"),
            HTML("<br>"),
            # Submit("submit", "Submit"),
            # HTML("""<a href="{{request.META.HTTP_REFERER}}">Go back</a>"""),
        )


# FoodFormSet = inlineformset_factory(
#     FoodType,
#     Food,
#     form=FoodForm,
#     # fields=["name", "description", "created_by"],
#     extra=1,
#     can_delete=True,
# )
