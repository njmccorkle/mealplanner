from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("menu/<str:menu_id>/", views.menu, name="menu"),
    # path("create-menu/", views.create_menu, name="create-menu"),
    # path("create-menumeal/", views.create_menumeal, name="create-menumeal"),
    # path("create-menumealitem/", views.create_menumealitem, name="create-menumealitem"),
    # path("menus/", views.MenuList.as_view(), name="list_menus"),
    # path("create/", views.MenuCreate.as_view(), name="create_menu"),
    # path("update/<int:pk>", views.MenuUpdate.as_view(), name="update_menu"),
    # path("delete-menumeal/<int:pk>/", views.delete_menumeal, name="delete-menumeal"),
]
