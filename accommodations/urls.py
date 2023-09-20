from django.urls import path
from . import views

urlpatterns = [
    path('accommodations/', views.accommodation_list, name='accommodation_list'),
    path('accommodations/<int:accommodation_id>/', views.accommodation_detail, name='accommodation_detail'),
]
