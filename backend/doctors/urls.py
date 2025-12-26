from django.urls import path
from . import views

urlpatterns = [
    path('files/', views.files_list_view, name='doctors_files_api'),
]

