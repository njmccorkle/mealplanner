# Generated by Django 4.1.5 on 2023-01-10 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("meal", "0002_rename_meal_type_mealdefinition_meal_id"),
        ("food", "0004_rename_food_type_id_food_food_type"),
        ("base", "0001_initial"),
        ("menu", "0007_rename_food_id_menumealitem_food"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="MenuMealItem",
            new_name="MenuItem",
        ),
        migrations.AlterModelOptions(
            name="menu",
            options={},
        ),
        migrations.RenameField(
            model_name="menuitem",
            old_name="food",
            new_name="food_id",
        ),
        migrations.RemoveField(
            model_name="menuitem",
            name="menu_meal_id",
        ),
        migrations.AddField(
            model_name="menu",
            name="meal_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="menu_meals",
                to="meal.meal",
            ),
        ),
        migrations.AddField(
            model_name="menuitem",
            name="the_menu",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="foods",
                to="menu.menu",
            ),
        ),
        migrations.DeleteModel(
            name="MenuMeal",
        ),
    ]
