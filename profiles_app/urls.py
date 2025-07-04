from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewset, basename= 'hello-viewset-url')
router.register('profiles', views.UserProfileViewSet)


urlpatterns = [
    path('hello-apiview/', views.HelloAPI.as_view()),
    path('', include(router.urls))
]
