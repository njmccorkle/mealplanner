from django.urls import path
from . import views

urlpatterns = [
    path("menuitem/<int:pk>/", views.create_menuitem, name="create-menuitem"),
    path("htmx/menuitem/<int:pk>/", views.detail_menuitem, name="detail-menuitem"),
    path(
        "htmx/menuitem/<int:pk>/update/", views.update_menuitem, name="update-menuitem"
    ),
    path(
        "htmx/menuitem/<int:pk>/delete/", views.delete_menuitem, name="delete-menuitem"
    ),
    path(
        "htmx/create-menuitem-form/<int:pk>",
        views.create_menuitem_form,
        name="create-menuitem-form",
    ),
    path("manage_menus/", views.manage_menus, name="manage-menus"),
    path("htmx/menu/<int:pk>/", views.detail_menu, name="detail-menu"),
    path("htmx/menu/<int:pk>/update/", views.update_menu, name="update-menu"),
    path(
        "htmx/create-menu-form/",
        views.create_menu_form,
        name="create-menu-form",
    ),
    path(
        "create-menu/",
        views.create_menu,
        name="create-menu",
    ),
    path("htmx/menu/<int:pk>/delete/", views.delete_menu, name="delete-menu"),
    # path("htmx/menu/get-menuitems/<int:pk>", views.get_menuitems, name="get-menuitems"),
    path("htmx/menu/get-menuitems/", views.get_menuitems, name="get-menuitems"),
    path("htmx/menu/get-menuitems/<int:pk>", views.get_menuitems, name="get-menuitems"),
]
