from django.shortcuts import render


def home(request):
    # foodtypes = FoodType.objects.all()
    # context = {"foodtypes": foodtypes}
    # return render(request, "food/home.html", context)
    return "Food Home"
