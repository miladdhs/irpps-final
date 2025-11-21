from django.urls import path
from . import views

urlpatterns = [
    path('admin/stats/', views.admin_dashboard, name='admin_dashboard'),
]

