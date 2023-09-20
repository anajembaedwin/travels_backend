from django.urls import path
from . import views

urlpatterns = [
    path('activities/', views.activity_list, name='activity_list'),
    path('activities/<int:activity_id>/', views.activity_detail, name='activity_detail'),
]

