from django.forms import ModelForm, DateInput, inlineformset_factory
from .models import Menu, MenuMeal, MenuMealItem


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"
        widgets = {"menu_date": DateInput(attrs={"type": "date"})}


class MenuMealForm(ModelForm):
    class Meta:
        model = MenuMeal
        fields = "__all__"


class MenuMealItemForm(ModelForm):
    class Meta:
        model = MenuMealItem
        fields = "__all__"


# MenuMealFormSet = inlineformset_factory(
#     Menu,
#     MenuMeal,
#     form=MenuMealForm,
#     extra=1,
#     can_delete=True,
#     can_delete_extra=True,
#     fk_name="menu_id",
# )
