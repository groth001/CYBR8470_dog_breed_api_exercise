from django.urls import include, path
#from django.conf.urls import include, url
from rest_framework import routers
from api import controllers

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('dog/', controllers.DogList.as_view()),
    path('dog/<int:pk>/', controllers.DogDetail.as_view()),
    path('breed/', controllers.BreedList.as_view()),
    path('breed/<int:pk>/', controllers.BreedDetail.as_view()),
    path('', include(router.urls)),
]
