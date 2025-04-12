# users/urls.py

from django.urls import path
from . import views  # importing the whole views module

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
]
