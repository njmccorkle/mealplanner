from django.urls import include, path
from rest_framework import routers

from .apiviews import *
from .views import *

router = routers.DefaultRouter()
router.register(r"menu", MenuViewSet)
router.register(r"menuitems", MenuItemViewSet)

urlpatterns = [
    path("menuitem/<int:pk>/", create_menuitem, name="create-menuitem"),
    path("htmx/menuitem/<int:pk>/", detail_menuitem, name="detail-menuitem"),
    path("htmx/menuitem/<int:pk>/update/", update_menuitem, name="update-menuitem"),
    path("htmx/menuitem/<int:pk>/delete/", delete_menuitem, name="delete-menuitem"),
    path(
        "htmx/create-menuitem-form/<int:pk>",
        create_menuitem_form,
        name="create-menuitem-form",
    ),
    path("manage_menus/", manage_menus, name="manage-menus"),
    path("htmx/menu/<int:pk>/", detail_menu, name="detail-menu"),
    path("htmx/menu/<int:pk>/update/", update_menu, name="update-menu"),
    path(
        "htmx/create-menu-form/",
        create_menu_form,
        name="create-menu-form",
    ),
    path(
        "create-menu/",
        create_menu,
        name="create-menu",
    ),
    path("htmx/menu/<int:pk>/delete/", delete_menu, name="delete-menu"),
    # path("htmx/menu/get-menuitems/<int:pk>", get_menuitems, name="get-menuitems"),
    path("htmx/menu/get-menuitems/", get_menuitems, name="get-menuitems"),
    path("htmx/menu/get-menuitems/<int:pk>", get_menuitems, name="get-menuitems"),
    path("api/", include(router.urls)),
]
