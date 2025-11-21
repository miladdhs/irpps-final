from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_api'),
    path('register/', views.register_view, name='register_api'),
    path('logout/', views.logout_view, name='logout_api'),
    path('profile/', views.profile_view, name='profile_api'),
    path('profile/update/', views.update_profile_view, name='update_profile_api'),
    path('profile/image/upload/', views.upload_profile_image_view, name='upload_profile_image_api'),
    path('profile/image/delete/', views.delete_profile_image_view, name='delete_profile_image_api'),
    path('profile/resume/update/', views.update_resume_view, name='update_resume_api'),
    path('members/', views.members_list_view, name='members_list_api'),
]

