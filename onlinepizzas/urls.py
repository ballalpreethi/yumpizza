from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register_view, name="register_view"),
    path("login", views.login_view, name="login_view"),
    path("menu", views.menu_view, name="menu_view"),
    path("confirm_order", views.confirm_order, name="confirm_order"),
    path("order", views.place_order, name="place_order"),
    path("my_orders", views.user_orders_view, name="user_orders_view"),
    path("logout", views.logout_view, name="logout_view")
]
