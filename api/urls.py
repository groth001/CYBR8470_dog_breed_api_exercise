#from django.urls import path
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from api import controllers

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'^dog/', controllers.DogList.as_view()),
    url(r'^dog/<int:pk>/', controllers.DogDetail.as_view()),
    url(r'^breed/', controllers.BreedList.as_view()),
    url(r'^breed/<int:pk>/', controllers.BreedDetail.as_view()),
    url(r'^', include(router.urls)),
]
