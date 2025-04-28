from django.urls import path

from . import views

app_name = "user_interface"

urlpatterns = [
    path("", views.home, name="home"),
    path("intro", views.intro, name="intro"),
]
