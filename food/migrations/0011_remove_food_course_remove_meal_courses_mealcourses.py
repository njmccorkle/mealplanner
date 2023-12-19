# Generated by Django 5.0 on 2023-12-17 06:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("food", "0010_alter_course_created_by_alter_food_created_by_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="food",
            name="course",
        ),
        migrations.RemoveField(
            model_name="meal",
            name="courses",
        ),
        migrations.CreateModel(
            name="MealCourses",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_datetime", models.DateTimeField(auto_now_add=True)),
                ("modified_datetime", models.DateTimeField(auto_now=True)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="food.course"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default="1",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "meal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="food.meal"
                    ),
                ),
            ],
            options={
                "verbose_name": "MealCourses",
                "verbose_name_plural": "MealCourses",
            },
        ),
    ]