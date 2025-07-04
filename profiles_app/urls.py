from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.HelloAPI.as_view())
]
