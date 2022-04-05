from argparse import Namespace
from django.urls import path
from . import views

app_name = "lotto"
urlpatterns = [
    path("", views.home, name="home"),
    path("challenge1/", views.challenge1, name="challenge1"),
    path("challenge2/", views.challenge2, name="challenge2"),
    path("challenge2/result/", views.challenge2_result, name="result"),
]
