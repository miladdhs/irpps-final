from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('create/', views.event_create, name='event_create'),
    path('<int:id>/register/', views.event_register, name='event_register'),
    path('<int:id>/update/', views.event_update, name='event_update'),
    path('<int:id>/delete/', views.event_delete, name='event_delete'),
    path('<slug:slug>/', views.event_detail, name='event_detail'),
]

