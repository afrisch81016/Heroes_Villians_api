from . import views
from django.urls import path


urlpatterns =[
    path('',views.supers_list),
    path('<int:pk>/', views.superheroes_detail), 
]