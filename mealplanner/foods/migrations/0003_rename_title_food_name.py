# Generated by Django 4.1.5 on 2023-01-03 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("foods", "0002_rename_title_food_title"),
    ]

    operations = [
        migrations.RenameField(
            model_name="food",
            old_name="title",
            new_name="name",
        ),
    ]
