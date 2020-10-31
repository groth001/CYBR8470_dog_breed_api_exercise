from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('dog/', views.DogList.as_view()),
    path('dog/<int:pk>/', views.DogDetail.as_view()),
    path('breed/', views.BreedList.as_view()),
    path('breed/<int:pk>/', views.BreedDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
