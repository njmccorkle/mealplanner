# Generated by Django 4.1.5 on 2023-10-20 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("meal", "0003_delete_mealdefinition"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mealitems",
            name="meal",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mealitems",
                to="meal.meal",
            ),
        ),
    ]
