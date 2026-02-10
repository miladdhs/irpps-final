from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_api'),
    path('register/', views.register_view, name='register_api'),
    path('logout/', views.logout_view, name='logout_api'),
    path('profile/', views.profile_view, name='profile_api'),
    path('profile/update/', views.update_profile_view, name='update_profile_api'),
    path('upload-profile-image/', views.upload_profile_image_view, name='upload_profile_image_api'),
    path('delete-profile-image/', views.delete_profile_image_view, name='delete_profile_image_api'),
    path('update-resume/', views.update_resume_view, name='update_resume_api'),
    path('members/', views.members_list_view, name='members_list_api'),
    
    # Membership management endpoints (admin only)
    path('members/pending/', views.pending_members_view, name='pending_members_api'),
    path('members/<int:user_id>/approve/', views.approve_member_view, name='approve_member_api'),
    path('members/<int:user_id>/reject/', views.reject_member_view, name='reject_member_api'),
]

