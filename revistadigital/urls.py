from django.urls import path
from . import views
from .views import home


urlpatterns = [
    path("", home.as_view(), name = "home"),
    path("integrantes", views.integrantes, name = "integrantes"),
    path("bibliografia", views.bibliografia, name = "bibliografia"),
]