from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<slug:slug>/', views.event_detail, name='event_detail'),
    path('<int:id>/register/', views.event_register, name='event_register'),
    path('create/', views.event_create, name='event_create'),
]

