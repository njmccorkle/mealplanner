from django.db import models


class FoodType(models.Model):
    name = models.CharField(max_length=200)


class Food(models.Model):
    name = models.CharField(max_length=200)
    foodtype = models.ForeignKey(FoodType, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
