from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse("Home page")
    return render(request, "home.html")


def room(request):
    # return HttpResponse("room")
    return render(request, "room.html")
