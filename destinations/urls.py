from django.urls import path
from . import views

urlpatterns = [
    path('destinations/list/', views.destination_list, name='destination_list'),
    path('destinations/detail/<int:destination_id>/', views.destination_detail, name='destination_detail'),
]
