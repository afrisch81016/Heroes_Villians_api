from . import views
from django.urls import path


urlpatterns =[
    path('',views.supers),
    path('<int:pk>/', views.supers_details)
]