from django.http import HttpResponse
from .models import Food


def index(request):
    latest_foods_added = Food.objects.order_by("created_datetime")[:5]
    output = ", ".join([f.name for f in latest_foods_added])
    return HttpResponse(output)


# def index(request):
#     return HttpResponse("Hello, world. You're at the foods index.")


def food(request, food_id):
    return HttpResponse("This is food %s" % food_id)


def foodtype(request, food_type_id):
    return HttpResponse("This is food type %s" % food_type_id)
