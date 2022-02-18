from . import views
from django.urls import path


urlpatterns =[
    path('',views.super_types_list),
    #path('<int:pk>/', views.super_type_detail),  # for setup of delete or edit but not logic in views currently
]